from django.db import models
from django.utils.text import slugify 

class Linguagem(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Linguagens"
class Assunto(models.Model):
    linguagem = models.ForeignKey(Linguagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.linguagem.nome} {self.nome}")
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Assuntos"

    def __str__(self):
        return f"{self.linguagem.nome} - {self.nome}"
class Pergunta(models.Model):
    texto = models.TextField()
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    explicacao = models.TextField(blank=True, help_text="Explicação exibida após o usuário responder.")
    
    class Meta:
        verbose_name_plural = "Perguntas"

    def __str__(self):
        return self.texto[:50]
    
class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="alternativas")
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Respostas"

    def __str__(self):
        return f"{self.texto} ({'Correta' if self.correta else 'Errada'})"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
class Resultado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    assunto = models.ForeignKey('Assunto', on_delete=models.CASCADE, null=True, blank=True) 
    total_perguntas = models.IntegerField()  
    acertos = models.IntegerField()
    status = models.CharField(max_length=12, default='COMPLETO')       
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.acertos}/{self.total_perguntas} acertos"
class Dificuldade(models.Model):
    """
    Armazena os níveis de dificuldade de forma centralizada.
    Ex: "Fácil", "Médio", "Difícil"
    """
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Dificuldades"

class PerguntaDificuldade(models.Model):
    """
    Conecta uma Pergunta a um nível de Dificuldade.
    Este é o modelo "ponte" que não altera o modelo Pergunta original.
    """
    pergunta = models.OneToOneField(Pergunta, on_delete=models.CASCADE, related_name="dificuldade_link")
    dificuldade = models.ForeignKey(Dificuldade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pergunta.texto[:30]}... - {self.dificuldade.nome}"

    class Meta:
        verbose_name_plural = "Dificuldades das Perguntas"