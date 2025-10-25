from django.urls import path
from . import views

urlpatterns = [
    path('', views.configurar_quiz, name='configurar_quiz'), 
    path('api/assuntos/<int:linguagem_id>/', views.get_assuntos, name='get_assuntos'),
    path('contexto/<int:assunto_id>/<int:dificuldade_id>/', views.pagina_contexto, name='pagina_contexto'),
    path('iniciar/<int:assunto_id>/<int:dificuldade_id>/', views.iniciar_novo_quiz, name='iniciar_novo_quiz'),
    path('api/dificuldades/', views.get_dificuldades, name='get_dificuldades'),
    path('jogar/<int:assunto_id>/', views.jogar_quiz, name='jogar_quiz'),
]