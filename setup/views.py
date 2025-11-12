from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Linguagem, Assunto, Pergunta, Resposta, Dificuldade, PerguntaDificuldade, ContextoAssunto, Resultado
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.utils import timezone

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('configurar_quiz')
        return super().dispatch(request, *args, **kwargs)

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('/quiz/')
    else:
        return redirect('login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('configurar_quiz')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def configurar_quiz(request):
    linguagens = Linguagem.objects.all()
    return render(request, 'setup/configurar_quiz.html', {'linguagens': linguagens})

@login_required
def get_dificuldades(request):
    dificuldades = Dificuldade.objects.all()
    dificuldades_lista = [{'id': d.id, 'nome': d.nome} for d in dificuldades]
    return JsonResponse(dificuldades_lista, safe=False)

@login_required
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

@login_required
def iniciar_novo_quiz(request, assunto_id, dificuldade_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    dificuldade = get_object_or_404(Dificuldade, id=dificuldade_id)
    perguntas_ids = list(PerguntaDificuldade.objects.filter(
        pergunta__assunto=assunto, 
        dificuldade=dificuldade
    ).order_by('pergunta__id')
    .values_list('pergunta__id', flat=True))
    
    perguntas_ids = perguntas_ids[:5] 

    request.session['quiz_perguntas_restantes_ids'] = perguntas_ids
    request.session['quiz_total_perguntas'] = len(perguntas_ids)
    request.session['quiz_score'] = 0
    request.session['quiz_revisao_data'] = []
    request.session['quiz_dificuldade_id'] = dificuldade_id
    request.session['quiz_start_time'] = timezone.now().isoformat()
    
    return redirect('jogar_quiz', assunto_id=assunto_id)

@login_required
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
                'pergunta_texto': pergunta_respondida.texto,
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
        total_perguntas = request.session.get('quiz_total_perguntas', 0)
        dificuldade_id = request.session.get('quiz_dificuldade_id')
        
        start_time_str = request.session.get('quiz_start_time')
        tempo_gasto = None
        dificuldade = None
        
        if dificuldade_id:
            dificuldade = Dificuldade.objects.get(id=dificuldade_id)

        if start_time_str:
            try:
                start_time = timezone.datetime.fromisoformat(start_time_str)
                end_time = timezone.now()
                tempo_gasto = end_time - start_time
            except (ValueError, TypeError):
                pass 
        
        if request.user.is_authenticated:
            defaults_para_atualizar = {
                'acertos': score,
                'total_perguntas': total_perguntas,
                'tempo_gasto': tempo_gasto,
                'data': timezone.now()
            }

            Resultado.objects.update_or_create(
                usuario=request.user,
                assunto=assunto,
                dificuldade=dificuldade,
                defaults=defaults_para_atualizar
            )

        for key in list(request.session.keys()):
            if key.startswith('quiz_'):
                del request.session[key]
        
        context = {
            'score': score,
            'total_perguntas': total_perguntas,
            'assunto': assunto, 
            'dificuldade': dificuldade,
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

@login_required
def pagina_contexto(request, assunto_id, dificuldade_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    dificuldade = get_object_or_404(Dificuldade, id=dificuldade_id)
    
    contexto_especifico = None
    try:
        contexto_especifico = ContextoAssunto.objects.get(assunto=assunto, dificuldade=dificuldade)
    except ContextoAssunto.DoesNotExist:
        pass

    context = {
        'assunto': assunto,
        'dificuldade': dificuldade,
        'contexto_especifico': contexto_especifico,
    }
    return render(request, 'setup/pagina_contexto.html', context)

@login_required
def ranking_quiz(request, assunto_id, dificuldade_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    dificuldade = get_object_or_404(Dificuldade, id=dificuldade_id)

    resultados = Resultado.objects.filter(assunto=assunto, dificuldade=dificuldade)

    context = {
        'assunto': assunto,
        'dificuldade': dificuldade,
        'resultados': resultados
    }
    return render(request, 'setup/ranking.html', context)

@login_required
def selecionar_ranking(request):
    linguagens = Linguagem.objects.all()
    context = {
        'linguagens': linguagens
    }
    return render(request, 'setup/selecionar_ranking.html', context)