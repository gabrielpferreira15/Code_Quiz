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

class Pergunta(models.Model):
    texto = models.TextField()
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto[:50]
    
class Resposta(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE, related_name="respostas")
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.texto} ({'Correta' if self.correta else 'Errada'})"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Resultado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_perguntas = models.IntegerField()   
    acertos = models.IntegerField()         
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.acertos}/{self.total_perguntas} acertos"