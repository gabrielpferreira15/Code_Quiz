from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Linguagem, Assunto, Pergunta
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


def iniciar_quiz(request, assunto_id):
    assunto_atual = get_object_or_404(Assunto, id=assunto_id)
    perguntas = Pergunta.objects.filter(assunto=assunto_atual).prefetch_related('alternativas')

    if not perguntas.exists():
        messages.warning(request, f"Ainda não há perguntas para '{assunto_atual}'.")
        return redirect('configurar_quiz')

    if request.method == 'POST':
        score = 0
        total_perguntas = perguntas.count()
        for pergunta in perguntas:
            id_alternativa_selecionada = request.POST.get(f'pergunta_{pergunta.id}')
            if id_alternativa_selecionada:
                alternativa_correta = next((alt for alt in pergunta.alternativas.all() if alt.correta), None)
                if alternativa_correta and int(id_alternativa_selecionada) == alternativa_correta.id:
                    score += 1
        acertou_mais_da_metade = score > (total_perguntas // 2)
        
        acertou_mais_da_metade = score > (total_perguntas // 2)
        contexto_resultado = {
            'score': score, 
            'total_perguntas': total_perguntas, 
            'assunto': assunto_atual,
            'acertou_mais_da_metade': acertou_mais_da_metade
        }
        return render(request, 'setup/resultado_quiz.html', contexto_resultado)

    context = {'perguntas': perguntas, 'assunto': assunto_atual}
    return render(request, 'setup/iniciar_quiz.html', context)