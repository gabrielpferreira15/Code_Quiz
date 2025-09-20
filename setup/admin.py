from django.contrib import admin
from .models import Linguagem, Assunto, Pergunta, Resposta 
class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 4 
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]
    list_display = ('texto', 'assunto') 

admin.site.register(Linguagem)
admin.site.register(Assunto)
admin.site.register(Pergunta, PerguntaAdmin)