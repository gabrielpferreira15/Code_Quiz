from django.contrib import admin
from django.contrib import admin
from .models import Linguagem, Assunto, Pergunta, Resposta 
# Register your models here.
admin.site.register(Linguagem)
admin.site.register(Assunto)
admin.site.register(Pergunta)
admin.site.register(Resposta)