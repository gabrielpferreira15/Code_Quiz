from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
    path('api/assuntos/<int:linguagem_id>/', views.get_assuntos, name='get_assuntos'),
    path('python/sintaxe-basica/', views.python_sb, name='python_sb'),
    path('python/repeticao/', views.python_er, name='python_er'),
    path('python/condicionais/', views.python_c, name='python_c'),
    path('c/sintaxe-basica/', views.c_sb, name='c_sb'),
    path('c/repeticao/', views.c_er, name='c_er'),
    path('c/condicionais/', views.c_c, name='c_c'),
]