from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Linguagem, Assunto

def configurar_quiz(request):
    linguagens = Linguagem.objects.all()
    assuntos = Assunto.objects.all()
    
    if request.method == 'POST':
        linguagem_id = request.POST.get('linguagem')
        assunto_id = request.POST.get('assunto')
        
        if not linguagem_id:
            messages.error(request, 'Por favor, selecione uma linguagem de programação.')
            return redirect('configurar_quiz')
            
        if not assunto_id:
            messages.error(request, 'Por favor, selecione um assunto.')
            return redirect('configurar_quiz')
            
   
        return render(request, 'quiz_gerado.html', {'linguagem': linguagem_id, 'assunto': assunto_id})
        
    return render(request, 'configurar_quiz.html', {'linguagens': linguagens, 'assuntos': assuntos})
def python_sb(request):
    try:
        assunto_atual = Assunto.objects.get(nome__iexact="Sintaxe Básica", linguagem__nome__iexact="Python")
    except Assunto.DoesNotExist:
        messages.error(request, "O quiz de 'Sintaxe Básica de Python' não está configurado.")
        return redirect('configurar_quiz')

    perguntas = Pergunta.objects.filter(assunto=assunto_atual)

    if not perguntas.exists():
        messages.warning(request, "Ainda não há perguntas para 'Sintaxe Básica de Python'.")
        return redirect('configurar_quiz')

    if request.method == 'POST':
        score = 0
        total_perguntas = len(perguntas)
        for pergunta in perguntas:
            id_alternativa_selecionada = request.POST.get(f'pergunta_{pergunta.id}')
            if id_alternativa_selecionada:
                alternativa_correta = pergunta.alternativas.filter(is_correta=True).first()
                if alternativa_correta and int(id_alternativa_selecionada) == alternativa_correta.id:
                    score += 1
        
        contexto_resultado = {'score': score, 'total_perguntas': total_perguntas, 'assunto': assunto_atual}
        return render(request, 'resultado_quiz.html', contexto_resultado)

    context = {'perguntas': perguntas, 'assunto': assunto_atual}
    return render(request, 'iniciar_quiz.html', context)


def python_er(request):
    try:
        assunto_atual = Assunto.objects.get(nome__iexact="Estrutura de Repetição", linguagem__nome__iexact="Python")
    except Assunto.DoesNotExist:
        messages.error(request, "O quiz de 'Estrutura de Repetição em Python' não está configurado.")
        return redirect('configurar_quiz')

    perguntas = Pergunta.objects.filter(assunto=assunto_atual)

    if not perguntas.exists():
        messages.warning(request, "Ainda não há perguntas para 'Estrutura de Repetição em Python'.")
        return redirect('configurar_quiz')

    if request.method == 'POST':
        score = 0
        total_perguntas = len(perguntas)
        for pergunta in perguntas:
            id_alternativa_selecionada = request.POST.get(f'pergunta_{pergunta.id}')
            if id_alternativa_selecionada:
                alternativa_correta = pergunta.alternativas.filter(is_correta=True).first()
                if alternativa_correta and int(id_alternativa_selecionada) == alternativa_correta.id:
                    score += 1
        
        contexto_resultado = {'score': score, 'total_perguntas': total_perguntas, 'assunto': assunto_atual}
        return render(request, 'resultado_quiz.html', contexto_resultado)

    context = {'perguntas': perguntas, 'assunto': assunto_atual}
    return render(request, 'iniciar_quiz.html', context)
def python_c(request):
    try:
        assunto_atual = Assunto.objects.get(nome__iexact="Condicionais", linguagem__nome__iexact="Python")
    except Assunto.DoesNotExist:
        messages.error(request, "O quiz de 'Condicionais em Python' não está configurado.")
        return redirect('configurar_quiz')

    perguntas = Pergunta.objects.filter(assunto=assunto_atual)

    if not perguntas.exists():
        messages.warning(request, "Ainda não há perguntas para 'Condicionais em Python'.")
        return redirect('configurar_quiz')

    if request.method == 'POST':
        score = 0
        total_perguntas = len(perguntas)
        for pergunta in perguntas:
            id_alternativa_selecionada = request.POST.get(f'pergunta_{pergunta.id}')
            if id_alternativa_selecionada:
                alternativa_correta = pergunta.alternativas.filter(is_correta=True).first()
                if alternativa_correta and int(id_alternativa_selecionada) == alternativa_correta.id:
                    score += 1
        
        contexto_resultado = {'score': score, 'total_perguntas': total_perguntas, 'assunto': assunto_atual}
        return render(request, 'resultado_quiz.html', contexto_resultado)

    context = {'perguntas': perguntas, 'assunto': assunto_atual}
    return render(request, 'iniciar_quiz.html', context)