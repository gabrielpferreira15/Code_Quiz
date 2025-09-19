from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
    path('python/sintaxe-basica/', views.quiz_python_sb, name='python_sb'),
    path('python/repeticao/', views.quiz_python_er, name='python_er'),

]
