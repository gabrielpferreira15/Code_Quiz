import pytest
from django.db import IntegrityError, transaction
from setup.models import Linguagem, Assunto, Pergunta, Resposta, Dificuldade, PerguntaDificuldade


# Fixtures compartilhadas no nível do módulo
@pytest.fixture
def linguagem_python(db):
    """Fixture compartilhada para criar Linguagem Python"""
    return Linguagem.objects.get_or_create(nome="Python")[0]


@pytest.fixture
def linguagem_javascript(db):
    """Fixture para criar Linguagem JavaScript"""
    return Linguagem.objects.get_or_create(nome="JavaScript")[0]


@pytest.fixture
def assunto_basico(db, linguagem_python):
    """Fixture para criar Assunto básico de Python"""
    return Assunto.objects.create(nome="Básico", linguagem=linguagem_python)


@pytest.fixture
def dificuldade_facil(db):
    """Fixture para criar Dificuldade Fácil"""
    return Dificuldade.objects.get_or_create(nome="Fácil")[0]


@pytest.fixture
def dificuldade_medio(db):
    """Fixture para criar Dificuldade Médio"""
    return Dificuldade.objects.get_or_create(nome="Médio")[0]


@pytest.fixture
def dificuldade_dificil(db):
    """Fixture para criar Dificuldade Difícil"""
    return Dificuldade.objects.get_or_create(nome="Difícil")[0]


# Testes
@pytest.mark.django_db
class TestLinguagem:
    def test_create_linguagem(self):
        """Testa a criação de uma Linguagem"""
        linguagem = Linguagem.objects.create(nome="Ruby")
        assert linguagem.nome == "Ruby"
        assert linguagem.slug == "ruby"

    def test_linguagem_slug_auto_generate(self):
        """Testa que o slug é gerado automaticamente"""
        linguagem = Linguagem.objects.create(nome="C Sharp")
        assert linguagem.slug == "c-sharp"


@pytest.mark.django_db
class TestAssunto:
    def test_create_assunto(self, linguagem_python):
        """Testa a criação de um Assunto"""
        assunto = Assunto.objects.create(nome="Avançado", linguagem=linguagem_python)
        assert assunto.nome == "Avançado"

    @pytest.mark.django_db(transaction=True)
    def test_assunto_unique_together(self, linguagem_python, linguagem_javascript):
        """Testa que a combinação linguagem + nome deve ser única"""
        Assunto.objects.create(nome="Básico", linguagem=linguagem_python)
        
        with transaction.atomic():
            with pytest.raises(IntegrityError):
                Assunto.objects.create(nome="Básico", linguagem=linguagem_python)
        
        # Mesmo nome mas linguagem diferente deve funcionar
        assunto2 = Assunto.objects.create(nome="Básico", linguagem=linguagem_javascript)
        assert assunto2.nome == "Básico"

    def test_assunto_str(self, assunto_basico):
        """Testa o método __str__ do Assunto"""
        assert str(assunto_basico) == "Python - Básico"


@pytest.mark.django_db
class TestPergunta:
    def test_create_pergunta(self, assunto_basico):
        """Testa a criação de uma Pergunta"""
        pergunta = Pergunta.objects.create(
            texto="Qual é o tipo de dado para números inteiros em Python?",
            assunto=assunto_basico,
            explicacao="Em Python, o tipo int é usado para números inteiros."
        )
        assert pergunta.texto == "Qual é o tipo de dado para números inteiros em Python?"
        assert pergunta.assunto == assunto_basico
        assert pergunta.explicacao is not None

    def test_pergunta_str(self, assunto_basico):
        """Testa o método __str__ da Pergunta"""
        pergunta = Pergunta.objects.create(
            texto="Teste de pergunta muito longa que será truncada no __str__",
            assunto=assunto_basico
        )
        assert len(str(pergunta)) <= 50

    def test_pergunta_without_explicacao(self, assunto_basico):
        """Testa criação de pergunta sem explicação"""
        pergunta = Pergunta.objects.create(
            texto="Pergunta sem explicação",
            assunto=assunto_basico
        )
        assert pergunta.explicacao == ""


@pytest.mark.django_db
class TestResposta:
    @pytest.fixture
    def pergunta(self, assunto_basico):
        """Fixture que cria uma Pergunta para uso nos testes"""
        return Pergunta.objects.create(
            texto="Qual é o tipo de dado?",
            assunto=assunto_basico
        )

    def test_create_resposta_correta(self, pergunta):
        """Testa a criação de uma Resposta correta"""
        resposta = Resposta.objects.create(
            pergunta=pergunta,
            texto="int",
            correta=True
        )
        assert resposta.texto == "int"
        assert resposta.correta is True
        assert resposta.pergunta == pergunta

    def test_create_resposta_incorreta(self, pergunta):
        """Testa a criação de uma Resposta incorreta"""
        resposta = Resposta.objects.create(
            pergunta=pergunta,
            texto="string",
            correta=False
        )
        assert resposta.correta is False

    def test_resposta_str(self, pergunta):
        """Testa o método __str__ da Resposta"""
        resposta_correta = Resposta.objects.create(
            pergunta=pergunta,
            texto="int",
            correta=True
        )
        assert str(resposta_correta) == "int (Correta)"
        
        resposta_errada = Resposta.objects.create(
            pergunta=pergunta,
            texto="string",
            correta=False
        )
        assert str(resposta_errada) == "string (Errada)"

    def test_resposta_related_name(self, pergunta):
        """Testa o related_name 'alternativas'"""
        Resposta.objects.create(pergunta=pergunta, texto="A", correta=True)
        Resposta.objects.create(pergunta=pergunta, texto="B", correta=False)
        Resposta.objects.create(pergunta=pergunta, texto="C", correta=False)
        
        assert pergunta.alternativas.count() == 3


@pytest.mark.django_db
class TestDificuldade:
    def test_create_dificuldade(self):
        """Testa a criação de uma Dificuldade"""
        dificuldade = Dificuldade.objects.create(nome="Expert")
        assert dificuldade.nome == "Expert"
        assert str(dificuldade) == "Expert"

    def test_dificuldade_nivel_choices(self, dificuldade_facil, dificuldade_medio, dificuldade_dificil):
        """Testa os níveis válidos de dificuldade"""
        assert dificuldade_facil.nome == "Fácil"
        assert dificuldade_medio.nome == "Médio"
        assert dificuldade_dificil.nome == "Difícil"

    @pytest.mark.django_db(transaction=True)
    def test_dificuldade_unique_nome(self):
        """Testa que o nome da dificuldade deve ser único"""
        Dificuldade.objects.create(nome="Iniciante")
        
        with transaction.atomic():
            with pytest.raises(IntegrityError):
                Dificuldade.objects.create(nome="Iniciante")


@pytest.mark.django_db
class TestPerguntaDificuldade:
    @pytest.fixture
    def pergunta(self, assunto_basico):
        """Fixture que cria uma Pergunta"""
        return Pergunta.objects.create(
            texto="Qual é o tipo de dado?",
            assunto=assunto_basico
        )

    def test_create_pergunta_dificuldade(self, pergunta, dificuldade_facil):
        """Testa a criação de uma relação PerguntaDificuldade"""
        pd = PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade_facil
        )
        assert pd.pergunta == pergunta
        assert pd.dificuldade == dificuldade_facil

    @pytest.mark.django_db(transaction=True)
    def test_pergunta_dificuldade_unique(self, pergunta, dificuldade_facil):
        """Testa que a combinação pergunta-dificuldade deve ser única (OneToOne)"""
        PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade_facil
        )
        with transaction.atomic():
            with pytest.raises(IntegrityError):
                PerguntaDificuldade.objects.create(
                    pergunta=pergunta,
                    dificuldade=dificuldade_facil
                )

    def test_pergunta_dificuldade_str(self, pergunta, dificuldade_medio):
        """Testa o método __str__ de PerguntaDificuldade"""
        pd = PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade_medio
        )
        resultado_str = str(pd)
        assert "Médio" in resultado_str

    def test_pergunta_dificuldade_related_name(self, pergunta, dificuldade_dificil):
        """Testa o related_name 'dificuldade_link'"""
        pd = PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade_dificil
        )
        assert pergunta.dificuldade_link == pd