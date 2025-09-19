from django.db import models

# Create your models here.
class Linguagem(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Assunto(models.Model):
    nome = models.CharField(max_length=100)
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.linguagem.nome}  -  {self.nome}"

class Perguntas(models.Model):
    texto = models.TextField()
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto[:50]