from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Linguagem, Assunto, Pergunta, Resposta, Dificuldade, PerguntaDificuldade
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import logout

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('/quiz/')
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def configurar_quiz(request):
    linguagens = Linguagem.objects.all()
    return render(request, 'setup/configurar_quiz.html', {'linguagens': linguagens})

def get_dificuldades(request):
    dificuldades = Dificuldade.objects.all()
    dificuldades_lista = [{'id': d.id, 'nome': d.nome} for d in dificuldades]
    return JsonResponse(dificuldades_lista, safe=False)

def get_assuntos(request, linguagem_id):
    assuntos = Assunto.objects.filter(linguagem_id=linguagem_id)
    
    assuntos_lista = []
    for assunto in assuntos:
        assuntos_lista.append({
            'id': assunto.id,
            'nome': assunto.nome,
            'url': f'/quiz/iniciar/{assunto.id}/' 
        })

    return JsonResponse(assuntos_lista, safe=False)

def iniciar_novo_quiz(request, assunto_id, dificuldade_id):
    perguntas = Pergunta.objects.filter(
        assunto_id=assunto_id,
        dificuldade_link__dificuldade__id=dificuldade_id
    ).order_by('id')

    lista_perguntas_ids = list(perguntas.values_list('id', flat=True))

    if not lista_perguntas_ids:
        messages.error(request, "Não há perguntas disponíveis para este quiz.")
        return redirect('configurar_quiz')

    request.session['quiz_todas_as_perguntas'] = lista_perguntas_ids.copy()
    request.session['quiz_perguntas_restantes_ids'] = lista_perguntas_ids
    request.session['quiz_total_perguntas'] = len(lista_perguntas_ids)
    request.session['quiz_score'] = 0
    request.session['quiz_revisao_data'] = []

    return redirect('jogar_quiz', assunto_id=assunto_id)

def jogar_quiz(request, assunto_id):
    total_perguntas = request.session.get('quiz_total_perguntas', 0)
    assunto = get_object_or_404(Assunto, id=assunto_id)

    id_pergunta_respondida = request.session.get('quiz_id_pergunta_atual')

    if request.method == 'POST' and id_pergunta_respondida:
        pergunta_respondida = get_object_or_404(Pergunta, id=id_pergunta_respondida)
        id_resposta_selecionada = request.POST.get('resposta')
        resposta_selecionada = get_object_or_404(Resposta, id=id_resposta_selecionada)
        resposta_correta = pergunta_respondida.alternativas.get(correta=True)

        if resposta_selecionada.correta:
            request.session['quiz_score'] = request.session.get('quiz_score', 0) + 1
        else:
            revisao_data = request.session.get('quiz_revisao_data', [])
            revisao_data.append({
                'pergunta': pergunta_respondida.texto,
                'resposta_selecionada_texto': resposta_selecionada.texto,
                'resposta_correta_texto': resposta_correta.texto,
                'pergunta_id': pergunta_respondida.id,
                'explicacao': pergunta_respondida.explicacao,
            })
            request.session['quiz_revisao_data'] = revisao_data

        perguntas_restantes_ids_feedback = request.session.get('quiz_perguntas_restantes_ids', [])
        context = {
            'assunto': assunto,
            'pergunta': pergunta_respondida,
            'pergunta_numero_atual': total_perguntas - len(perguntas_restantes_ids_feedback),
            'total_perguntas_quiz': total_perguntas,
            'show_feedback': True,
            'resposta_selecionada': resposta_selecionada,
            'resposta_correta': resposta_correta,
        }

        return render(request, 'setup/iniciar_quiz.html', context)

    perguntas_restantes_ids = request.session.get('quiz_perguntas_restantes_ids', [])

    if not perguntas_restantes_ids:
        score = request.session.get('quiz_score', 0)
        revisao_data = request.session.get('quiz_revisao_data', [])
        
        for key in list(request.session.keys()):
            if key.startswith('quiz_'):
                del request.session[key]

        context = {
            'score': score,
            'total_perguntas': total_perguntas,
            'assunto': assunto,
            'acertou_mais_da_metade': score > total_perguntas / 2,
            'revisao_data': revisao_data,
        }
        return render(request, 'setup/resultado_quiz.html', context)

    proxima_pergunta_id = perguntas_restantes_ids.pop(0)
    request.session['quiz_perguntas_restantes_ids'] = perguntas_restantes_ids
    request.session['quiz_id_pergunta_atual'] = proxima_pergunta_id
    pergunta = get_object_or_404(Pergunta, id=proxima_pergunta_id)

    context = {
        'assunto': assunto,
        'pergunta': pergunta,
        'pergunta_numero_atual': total_perguntas - len(perguntas_restantes_ids),
        'total_perguntas_quiz': total_perguntas,
        'show_feedback': False,
    }
    return render(request, 'setup/iniciar_quiz.html', context)

def custom_logout(request):
    logout(request)
    return redirect('login')