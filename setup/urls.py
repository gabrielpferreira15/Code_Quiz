from django.urls import path
from . import views

urlpatterns = [
    path('configurar/', views.configurar_quiz, name='configurar_quiz'),
]