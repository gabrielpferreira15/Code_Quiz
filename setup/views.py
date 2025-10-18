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
    assunto = get_object_or_404(Assunto, id=assunto_id)
    
    lista_perguntas = list(
        Pergunta.objects.filter(
            assunto_id=assunto_id,
            dificuldade_link__dificuldade_id=dificuldade_id
        ).values_list('id', flat=True)
    )

    if not lista_perguntas:
        messages.error(request, "Não foram encontradas perguntas para a seleção de assunto e dificuldade informada.")
        return redirect('configurar_quiz')

    request.session['lista_perguntas'] = lista_perguntas
    request.session['placar'] = 0
    request.session['perguntas_erradas_info'] = []
    
    return redirect('jogar_quiz', assunto_id=assunto_id)


def jogar_quiz(request, assunto_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    lista_perguntas_ids = request.session.get('lista_perguntas', [])
    placar = request.session.get('placar', 0)
    perguntas_erradas_ids = request.session.get('perguntas_erradas_ids', [])

    if not lista_perguntas_ids:
        total_perguntas_concluidas = Pergunta.objects.filter(assunto=assunto).count()
        acertou_mais_da_metade = placar > (total_perguntas_concluidas // 2)
        perguntas_erradas_info = request.session.get('perguntas_erradas_info', [])
        
        revisao_data = []
        for item in perguntas_erradas_info:
            pergunta = Pergunta.objects.prefetch_related('alternativas').get(id=item['pergunta_id'])
            resposta_selecionada = Resposta.objects.get(id=item['resposta_selecionada_id'])
            resposta_correta = pergunta.alternativas.filter(correta=True).first()

            revisao_data.append({
                'pergunta': pergunta,
                'resposta_correta_texto': resposta_correta.texto if resposta_correta else "N/A",
                'resposta_selecionada_texto': resposta_selecionada.texto if resposta_selecionada else "Não respondida"
            })

        contexto_final = {
            'score': placar,
            'total_perguntas': total_perguntas_concluidas,
            'assunto': assunto,
            'acertou_mais_da_metade': acertou_mais_da_metade,
            'revisao_data': revisao_data,
        }
        
        return render(request, 'setup/resultado_quiz.html', contexto_final)
    
    id_pergunta_atual = lista_perguntas_ids[0]
    pergunta_atual = get_object_or_404(Pergunta, id=id_pergunta_atual)
    total_perguntas_quiz = Pergunta.objects.filter(assunto=assunto).count()
    pergunta_numero_atual = total_perguntas_quiz - len(lista_perguntas_ids) + 1
    
    contexto = {
        'assunto': assunto,
        'pergunta': pergunta_atual,
        'total_perguntas_quiz': total_perguntas_quiz,
        'pergunta_numero_atual': pergunta_numero_atual,
    }
    
    if request.method == 'POST':
        id_resposta_selecionada = request.POST.get('resposta')
        
        if id_resposta_selecionada:
            resposta_selecionada = get_object_or_404(Resposta, id=id_resposta_selecionada)
            
            if resposta_selecionada.correta:
                request.session['placar'] = placar + 1
            else:
                perguntas_erradas_info = request.session.get('perguntas_erradas_info', [])
                perguntas_erradas_info.append({
                    'pergunta_id': pergunta_atual.id,
                    'resposta_selecionada_id': resposta_selecionada.id
                })

                request.session['perguntas_erradas_info'] = perguntas_erradas_info
            
            request.session['lista_perguntas'] = lista_perguntas_ids[1:]
            
            contexto['show_feedback'] = True
            contexto['resposta_selecionada'] = resposta_selecionada
            contexto['resposta_correta'] = pergunta_atual.alternativas.filter(correta=True).first()
    
    return render(request, 'setup/iniciar_quiz.html', contexto)

def custom_logout(request):
    logout(request)
    return redirect('login')