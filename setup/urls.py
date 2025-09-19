from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
    path('python/sintaxe-basica/', views.quiz_python_sb, name='python_sb'),
    path('python/repeticao/', views.quiz_python_er, name='python_er'),
    path('python/condicionais/', views.quiz_python_c, name='python_c'),
    path('c/sintaxe-basica/', views.quiz_c_sb, name='c_sb'),
    path('c/repeticao/', views.quiz_c_er, name='c_er'),
    path('c/condicionais/', views.quiz_c_c, name='c_c'),



]
