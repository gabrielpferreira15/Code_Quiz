from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Linguagem, Assunto, Pergunta, Resposta
from django.http import JsonResponse

def configurar_quiz(request):
    linguagens = Linguagem.objects.all()
    return render(request, 'setup/configurar_quiz.html', {'linguagens': linguagens})


def get_assuntos(request, linguagem_id):
    assuntos = Assunto.objects.filter(linguagem_id=linguagem_id)
    
    assuntos_lista = []
    for assunto in assuntos:
        assuntos_lista.append({
            'id': assunto.id,
            'nome': assunto.nome,
            'url': f'/quiz/{assunto.id}/' 
        })
            
    return JsonResponse(assuntos_lista, safe=False)


def iniciar_novo_quiz(request, assunto_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    lista_perguntas = list(Pergunta.objects.filter(assunto=assunto).values_list('id', flat=True))
    request.session['lista_perguntas'] = lista_perguntas
    request.session['placar'] = 0
    
    return redirect('jogar_quiz', assunto_id=assunto_id)

def jogar_quiz(request, assunto_id):
    assunto = get_object_or_404(Assunto, id=assunto_id)
    lista_perguntas_ids = request.session.get('lista_perguntas', [])
    placar = request.session.get('placar', 0)
    if not lista_perguntas_ids:
        total_perguntas = Pergunta.objects.filter(assunto=assunto).count()
        acertou_mais_da_metade = placar > (total_perguntas // 2)
        contexto_final = {
            'score': placar,
            'total_perguntas': total_perguntas,
            'assunto': assunto,
            'acertou_mais_da_metade': acertou_mais_da_metade
        }
        return render(request, 'setup/resultado_quiz.html', contexto_final)
    
    id_pergunta_atual = lista_perguntas_ids[0]
    pergunta_atual = get_object_or_404(Pergunta, id=id_pergunta_atual)
    
    contexto = {
        'assunto': assunto,
        'pergunta': pergunta_atual,
        'total_perguntas_quiz': Pergunta.objects.filter(assunto=assunto).count(),
        'perguntas_restantes': len(lista_perguntas_ids)
    }

    if request.method == 'POST':
        id_resposta_selecionada = request.POST.get('resposta')
        
        if id_resposta_selecionada:
            resposta_selecionada = get_object_or_404(Resposta, id=id_resposta_selecionada)
            

            if resposta_selecionada.correta:
                request.session['placar'] = placar + 1
            
            request.session['lista_perguntas'] = lista_perguntas_ids[1:]
            
            contexto['show_feedback'] = True
            contexto['resposta_selecionada'] = resposta_selecionada
            contexto['resposta_correta'] = pergunta_atual.alternativas.filter(correta=True).first()
    
    return render(request, 'setup/iniciar_quiz.html', contexto)