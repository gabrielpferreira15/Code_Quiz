from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
    path('api/assuntos/<int:linguagem_id>/', views.get_assuntos, name='get_assuntos'),
    path('quiz/<int:assunto_id>/', views.iniciar_quiz, name='iniciar_quiz')
]