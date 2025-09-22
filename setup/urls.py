from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
    path('api/assuntos/<int:linguagem_id>/', views.get_assuntos, name='get_assuntos'),
    path('quiz/iniciar/<int:assunto_id>/', views.iniciar_novo_quiz, name='iniciar_novo_quiz'),
    path('quiz/jogar/<int:assunto_id>/', views.jogar_quiz, name='jogar_quiz'),
]