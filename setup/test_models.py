import pytest
from django.db import IntegrityError, transaction
from setup.models import Linguagem, Assunto, Pergunta, Resposta, Dificuldade, PerguntaDificuldade


@pytest.mark.django_db
class TestAssunto:
    def test_create_assunto(self):
        """Testa a criação de um Assunto"""
        linguagem = Linguagem.objects.create(nome="Python")
        assunto = Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)
        assert assunto.nome == "Python - Básico"

    @pytest.mark.django_db(transaction=True)
    def test_assunto_unique_together(self):
        """Testa que a combinação linguagem + nome deve ser única"""
        linguagem = Linguagem.objects.create(nome="Python")
        Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)
        
        with transaction.atomic():
            with pytest.raises(IntegrityError):
                Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)
        
        outra_linguagem = Linguagem.objects.create(nome="JavaScript")
        assunto2 = Assunto.objects.create(nome="Python - Básico", linguagem=outra_linguagem)
        assert assunto2.nome == "Python - Básico"


@pytest.mark.django_db
class TestPergunta:
    @pytest.fixture
    def assunto(self):
        """Fixture que cria um Assunto para uso nos testes"""
        linguagem = Linguagem.objects.create(nome="Python")
        return Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)

    def test_create_pergunta(self, assunto):
        """Testa a criação de uma Pergunta"""
        pergunta = Pergunta.objects.create(
            texto="Qual é o tipo de dado para números inteiros em Python?",
            assunto=assunto,
            explicacao="Em Python, o tipo int é usado para números inteiros."
        )
        assert pergunta.texto == "Qual é o tipo de dado para números inteiros em Python?"
        assert pergunta.assunto == assunto
        assert pergunta.explicacao is not None

    def test_pergunta_str(self, assunto):
        """Testa o método __str__ da Pergunta"""
        pergunta = Pergunta.objects.create(
            texto="Teste de pergunta",
            assunto=assunto
        )
        assert "Teste de pergunta" in str(pergunta)


@pytest.mark.django_db
class TestResposta:
    @pytest.fixture
    def pergunta(self):
        """Fixture que cria uma Pergunta para uso nos testes"""
        linguagem = Linguagem.objects.create(nome="Python")
        assunto = Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)
        return Pergunta.objects.create(
            texto="Qual é o tipo de dado?",
            assunto=assunto
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
        resposta = Resposta.objects.create(
            pergunta=pergunta,
            texto="int",
            correta=True
        )
        assert "int" in str(resposta)


@pytest.mark.django_db
class TestDificuldade:
    def test_create_dificuldade(self):
        """Testa a criação de uma Dificuldade"""
        dificuldade = Dificuldade.objects.create(nome="Fácil")
        assert dificuldade.nome == "Fácil"
        assert str(dificuldade) == "Fácil"

    def test_dificuldade_nivel_choices(self):
        """Testa os níveis válidos de dificuldade"""
        niveis_validos = ["Fácil", "Médio", "Difícil"]
        for nivel in niveis_validos:
            dificuldade = Dificuldade.objects.create(nome=nivel)
            assert dificuldade.nome == nivel


@pytest.mark.django_db
class TestPerguntaDificuldade:
    @pytest.fixture
    def pergunta(self):
        """Fixture que cria uma Pergunta"""
        linguagem = Linguagem.objects.create(nome="Python")
        assunto = Assunto.objects.create(nome="Python - Básico", linguagem=linguagem)
        return Pergunta.objects.create(
            texto="Qual é o tipo de dado?",
            assunto=assunto
        )

    @pytest.fixture
    def dificuldade(self):
        """Fixture que cria uma Dificuldade"""
        return Dificuldade.objects.create(nome="Fácil")

    def test_create_pergunta_dificuldade(self, pergunta, dificuldade):
        """Testa a criação de uma relação PerguntaDificuldade"""
        pd = PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade
        )
        assert pd.pergunta == pergunta
        assert pd.dificuldade == dificuldade

    @pytest.mark.django_db(transaction=True)
    def test_pergunta_dificuldade_unique(self, pergunta, dificuldade):
        """Testa que a combinação pergunta-dificuldade deve ser única"""
        PerguntaDificuldade.objects.create(
            pergunta=pergunta,
            dificuldade=dificuldade
        )
        with transaction.atomic():
            with pytest.raises(IntegrityError):
                PerguntaDificuldade.objects.create(
                    pergunta=pergunta,
                    dificuldade=dificuldade
                )