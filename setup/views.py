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