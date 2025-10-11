from django.db import migrations
from django.utils.text import slugify

def popular_dados(apps, schema_editor):
    # Obtendo acesso a todos os modelos necessários
    Linguagem = apps.get_model('setup', 'Linguagem')
    Assunto = apps.get_model('setup', 'Assunto')
    Pergunta = apps.get_model('setup', 'Pergunta')
    Resposta = apps.get_model('setup', 'Resposta')
    Dificuldade = apps.get_model('setup', 'Dificuldade')
    PerguntaDificuldade = apps.get_model('setup', 'PerguntaDificuldade')

    # Limpando os dados na ordem correta para evitar erros de referência
    Resposta.objects.all().delete()
    PerguntaDificuldade.objects.all().delete()
    Pergunta.objects.all().delete()
    Assunto.objects.all().delete()
    Linguagem.objects.all().delete()
    Dificuldade.objects.all().delete()

    # --- NÍVEIS DE DIFICULDADE ---
    facil = Dificuldade.objects.create(nome='Fácil')
    medio = Dificuldade.objects.create(nome='Médio')
    dificil = Dificuldade.objects.create(nome='Difícil')

    # --- LINGUAGENS ---
    python = Linguagem.objects.create(nome='Python', slug=slugify('Python'))
    c_lang = Linguagem.objects.create(nome='C', slug=slugify('C'))

    # ====================================================================
    # === QUIZ PYTHON: SINTAXE BÁSICA ===
    # ====================================================================
    assunto_py_sb_nome = 'Sintaxe Básica'
    assunto_py_sb = Assunto.objects.create(linguagem=python, nome=assunto_py_sb_nome, slug=slugify(f'{python.nome}-{assunto_py_sb_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p1 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Como você declara uma variável chamada idade com o valor 25 em Python?", explicacao="Python utiliza tipagem dinâmica...")
    PerguntaDificuldade.objects.create(pergunta=p1, dificuldade=facil)
    Resposta.objects.create(pergunta=p1, texto="int idade = 25", correta=False)
    Resposta.objects.create(pergunta=p1, texto="idade = 25", correta=True)
    Resposta.objects.create(pergunta=p1, texto="idade := 25", correta=False)
    Resposta.objects.create(pergunta=p1, texto="let idade = 25", correta=False)

    p2 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o símbolo usado para escrever um comentário de uma única linha em Python?", explicacao="Em Python, o caractere '#'... ")
    PerguntaDificuldade.objects.create(pergunta=p2, dificuldade=facil)
    Resposta.objects.create(pergunta=p2, texto="//", correta=False)
    Resposta.objects.create(pergunta=p2, texto="/* ... */", correta=False)
    Resposta.objects.create(pergunta=p2, texto="#", correta=True)
    Resposta.objects.create(pergunta=p2, texto="``", correta=False)

    p3 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual função é usada para imprimir uma mensagem no console em Python?", explicacao="A função `print()` é uma das...")
    PerguntaDificuldade.objects.create(pergunta=p3, dificuldade=facil)
    Resposta.objects.create(pergunta=p3, texto="console.log()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="System.out.println()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="echo()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="print()", correta=True)

    p4 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o tipo de dado de resultado = 10 / 2 em Python 3?", explicacao="Em Python 3, o operador de divisão `/` sempre retorna um float...")
    PerguntaDificuldade.objects.create(pergunta=p4, dificuldade=facil)
    Resposta.objects.create(pergunta=p4, texto="int", correta=False)
    Resposta.objects.create(pergunta=p4, texto="float", correta=True)
    Resposta.objects.create(pergunta=p4, texto="string", correta=False)
    Resposta.objects.create(pergunta=p4, texto="double", correta=False)

    p5 = Pergunta.objects.create(assunto=assunto_py_sb, texto='Como você converte uma string "100" para um número inteiro em Python?', explicacao="Python oferece funções de conversão...")
    PerguntaDificuldade.objects.create(pergunta=p5, dificuldade=facil)
    Resposta.objects.create(pergunta=p5, texto='(int)"100"', correta=False)
    Resposta.objects.create(pergunta=p5, texto='to_int("100")', correta=False)
    Resposta.objects.create(pergunta=p5, texto='int("100")', correta=True)
    Resposta.objects.create(pergunta=p5, texto='integer("100")', correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Sintaxe Básica' de Python
    # Exemplo:
    # p_medio_1 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual a diferença entre lista e tupla?")
    # PerguntaDificuldade.objects.create(pergunta=p_medio_1, dificuldade=medio)
    # Resposta.objects.create(pergunta=p_medio_1, texto="Listas são mutáveis, tuplas são imutáveis.", correta=True)
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Sintaxe Básica' de Python
    # ...


    # ====================================================================
    # === QUIZ PYTHON: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_py_er_nome = 'Estruturas de Repetição'
    assunto_py_er = Assunto.objects.create(linguagem=python, nome=assunto_py_er_nome, slug=slugify(f'{python.nome}-{assunto_py_er_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p6 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual estrutura de repetição é mais adequada para iterar sobre os itens de uma lista?", explicacao="O laço `for` em Python é projetado para...")
    PerguntaDificuldade.objects.create(pergunta=p6, dificuldade=facil)
    Resposta.objects.create(pergunta=p6, texto="O laço while", correta=False)
    Resposta.objects.create(pergunta=p6, texto="O laço do-while", correta=False)
    Resposta.objects.create(pergunta=p6, texto="O laço for", correta=True)
    Resposta.objects.create(pergunta=p6, texto="A recursão", correta=False)

    p7 = Pergunta.objects.create(assunto=assunto_py_er, texto="Como você cria um laço que executa 5 vezes usando a função range()?", explicacao="A função `range(5)` gera uma sequência...")
    PerguntaDificuldade.objects.create(pergunta=p7, dificuldade=facil)
    Resposta.objects.create(pergunta=p7, texto="for i in range(1, 5):", correta=False)
    Resposta.objects.create(pergunta=p7, texto="for i in range(5):", correta=True)
    Resposta.objects.create(pergunta=p7, texto="for i in range(0, 6):", correta=False)
    Resposta.objects.create(pergunta=p7, texto="for i in range(5-1):", correta=False)

    p8 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave é usada para parar completamente a execução de um laço?", explicacao="A instrução `break` interrompe a execução...")
    PerguntaDificuldade.objects.create(pergunta=p8, dificuldade=facil)
    Resposta.objects.create(pergunta=p8, texto="stop", correta=False)
    Resposta.objects.create(pergunta=p8, texto="exit", correta=False)
    Resposta.objects.create(pergunta=p8, texto="break", correta=True)
    Resposta.objects.create(pergunta=p8, texto="return", correta=False)

    p9 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave pula para a próxima iteração de um laço sem terminar o laço por completo?", explicacao="A instrução `continue` interrompe a iteração...")
    PerguntaDificuldade.objects.create(pergunta=p9, dificuldade=facil)
    Resposta.objects.create(pergunta=p9, texto="skip", correta=False)
    Resposta.objects.create(pergunta=p9, texto="next", correta=False)
    Resposta.objects.create(pergunta=p9, texto="pass", correta=False)
    Resposta.objects.create(pergunta=p9, texto="continue", correta=True)

    p10 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável contador for menor que 10?", explicacao="A sintaxe do `while` em Python começa...")
    PerguntaDificuldade.objects.create(pergunta=p10, dificuldade=facil)
    Resposta.objects.create(pergunta=p10, texto="while (contador < 10)", correta=False)
    Resposta.objects.create(pergunta=p10, texto="while contador < 10:", correta=True)
    Resposta.objects.create(pergunta=p10, texto="while: contador < 10", correta=False)
    Resposta.objects.create(pergunta=p10, texto="loop while contador < 10:", correta=False)
    
    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Estruturas de Repetição' de Python
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Estruturas de Repetição' de Python
    # ...


    # ====================================================================
    # === QUIZ PYTHON: CONDICIONAIS ===
    # ====================================================================
    assunto_py_c_nome = 'Condicionais'
    assunto_py_c = Assunto.objects.create(linguagem=python, nome=assunto_py_c_nome, slug=slugify(f'{python.nome}-{assunto_py_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p11 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual palavra-chave é usada para a parte "senão se" em uma estrutura condicional em Python?', explicacao="Python utiliza a contração `elif`...")
    PerguntaDificuldade.objects.create(pergunta=p11, dificuldade=facil)
    Resposta.objects.create(pergunta=p11, texto="else if", correta=False)
    Resposta.objects.create(pergunta=p11, texto="elif", correta=True)
    Resposta.objects.create(pergunta=p11, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p11, texto="elsif", correta=False)
   
    p12 = Pergunta.objects.create(assunto=assunto_py_c, texto='Como se escreve a condição "se a não for igual a b" em Python?', explicacao="O operador de desigualdade em Python é `!=`...")
    PerguntaDificuldade.objects.create(pergunta=p12, dificuldade=facil)
    Resposta.objects.create(pergunta=p12, texto="if a <> b:", correta=False)
    Resposta.objects.create(pergunta=p12, texto="if not(a == b):", correta=False)
    Resposta.objects.create(pergunta=p12, texto="if a != b:", correta=True)
    Resposta.objects.create(pergunta=p12, texto="if a is not b:", correta=False)

    p13 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é o operador lógico para "E" em Python?', explicacao="Python usa palavras em inglês para operadores...")
    PerguntaDificuldade.objects.create(pergunta=p13, dificuldade=facil)
    Resposta.objects.create(pergunta=p13, texto="&&", correta=False)
    Resposta.objects.create(pergunta=p13, texto="and", correta=True)
    Resposta.objects.create(pergunta=p13, texto="&", correta=False)
    Resposta.objects.create(pergunta=p13, texto="AND", correta=False)

    p14 = Pergunta.objects.create(assunto=assunto_py_c, texto="O que a seguinte expressão booleana retornaria: not (True and False)?", explicacao="A ordem de operação é...")
    PerguntaDificuldade.objects.create(pergunta=p14, dificuldade=facil)
    Resposta.objects.create(pergunta=p14, texto="True", correta=True)
    Resposta.objects.create(pergunta=p14, texto="False", correta=False)
    Resposta.objects.create(pergunta=p14, texto="None", correta=False)
    Resposta.objects.create(pergunta=p14, texto="Error", correta=False)

    p15 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é a sintaxe correta para um bloco if em Python que verifica se a variável nome é igual a "Ana"?', explicacao="A sintaxe de um `if` em Python exige...")
    PerguntaDificuldade.objects.create(pergunta=p15, dificuldade=facil)
    Resposta.objects.create(pergunta=p15, texto='if (nome == "Ana")', correta=False)
    Resposta.objects.create(pergunta=p15, texto='if nome = "Ana":', correta=False)
    Resposta.objects.create(pergunta=p15, texto='if nome == "Ana":', correta=True)
    Resposta.objects.create(pergunta=p15, texto='if nome is "Ana" then', correta=False)
    
    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Condicionais' de Python
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Condicionais' de Python
    # ...


    # ====================================================================
    # === QUIZ C: SINTAXE BÁSICA ===
    # ====================================================================
    assunto_c_sb_nome = 'Sintaxe Básica'
    assunto_c_sb = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_sb_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_sb_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p16 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você declara uma variável inteira chamada quantidade com o valor 50 em C?", explicacao="Em C, uma linguagem de tipagem estática...")
    PerguntaDificuldade.objects.create(pergunta=p16, dificuldade=facil)
    Resposta.objects.create(pergunta=p16, texto="quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p16, texto="int quantidade = 50;", correta=True)
    Resposta.objects.create(pergunta=p16, texto="integer quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p16, texto="var quantidade = 50;", correta=False)

    p17 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual é o símbolo usado para indicar o fim de uma instrução em C?", explicacao="O ponto e vírgula (`;`) é um terminador...")
    PerguntaDificuldade.objects.create(pergunta=p17, dificuldade=facil)
    Resposta.objects.create(pergunta=p17, texto=". (ponto final)", correta=False)
    Resposta.objects.create(pergunta=p17, texto=": (dois pontos)", correta=False)
    Resposta.objects.create(pergunta=p17, texto="; (ponto e vírgula)", correta=True)
    Resposta.objects.create(pergunta=p17, texto="O final da linha", correta=False)

    p18 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual função da biblioteca stdio.h é usada para imprimir texto formatado no console?", explicacao="A função `printf()` (print formatted) faz parte...")
    PerguntaDificuldade.objects.create(pergunta=p18, dificuldade=facil)
    Resposta.objects.create(pergunta=p18, texto="print()", correta=False)
    Resposta.objects.create(pergunta=p18, texto="cout <<", correta=False)
    Resposta.objects.create(pergunta=p18, texto="printf()", correta=True)
    Resposta.objects.create(pergunta=p18, texto="log()", correta=False)

    p19 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você escreve um comentário de múltiplas linhas em C?", explicacao="Em C, um comentário de bloco...")
    PerguntaDificuldade.objects.create(pergunta=p19, dificuldade=facil)
    Resposta.objects.create(pergunta=p19, texto="// ... //", correta=False)
    Resposta.objects.create(pergunta=p19, texto="# ... #", correta=False)
    Resposta.objects.create(pergunta=p19, texto="/* ... */", correta=True)
    Resposta.objects.create(pergunta=p19, texto='""" ... """', correta=False)

    p20 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual diretiva de pré-processador é necessária para usar a função printf?", explicacao="A diretiva `#include <stdio.h>` instrui...")
    PerguntaDificuldade.objects.create(pergunta=p20, dificuldade=facil)
    Resposta.objects.create(pergunta=p20, texto="#import <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p20, texto="#require <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p20, texto='#include "stdio.h"', correta=False)
    Resposta.objects.create(pergunta=p20, texto="#include <stdio.h>", correta=True)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Sintaxe Básica' de C
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Sintaxe Básica' de C
    # ...


    # ====================================================================
    # === QUIZ C: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_c_er_nome = 'Estruturas de Repetição'
    assunto_c_er = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_er_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_er_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p21 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe completa de um laço for em C que vai de 0 a 9?", explicacao="O laço for em C tem três partes...")
    PerguntaDificuldade.objects.create(pergunta=p21, dificuldade=facil)
    Resposta.objects.create(pergunta=p21, texto="for (int i=0; i < 10; i++)", correta=True)
    Resposta.objects.create(pergunta=p21, texto="for (i < 10; i++)", correta=False)
    Resposta.objects.create(pergunta=p21, texto="for (int i=0; i < 10)", correta=False)
    Resposta.objects.create(pergunta=p21, texto="for (int i=0 to 9)", correta=False)

    p22 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual laço em C garante que seu corpo seja executado pelo menos uma vez?", explicacao="O laço do-while é uma estrutura...")
    PerguntaDificuldade.objects.create(pergunta=p22, dificuldade=facil)
    Resposta.objects.create(pergunta=p22, texto="for", correta=False)
    Resposta.objects.create(pergunta=p22, texto="while", correta=False)
    Resposta.objects.create(pergunta=p22, texto="do-while", correta=True)
    Resposta.objects.create(pergunta=p22, texto="repeat-until", correta=False)
   
    p23 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável ativo for verdadeira (considerando 1 como verdadeiro)?", explicacao="A sintaxe do laço while em C requer...")
    PerguntaDificuldade.objects.create(pergunta=p23, dificuldade=facil)
    Resposta.objects.create(pergunta=p23, texto="while [ativo == 1]", correta=False)
    Resposta.objects.create(pergunta=p23, texto="while (ativo)", correta=True)
    Resposta.objects.create(pergunta=p23, texto="while {ativo}", correta=False)
    Resposta.objects.create(pergunta=p23, texto="while ativo is 1", correta=False)

    p24 = Pergunta.objects.create(assunto=assunto_c_er, texto="Dentro de um laço for, o que a terceira expressão (i++) geralmente representa?", explicacao="A terceira parte da declaração de um laço for...")
    PerguntaDificuldade.objects.create(pergunta=p24, dificuldade=facil)
    Resposta.objects.create(pergunta=p24, texto="A inicialização", correta=False)
    Resposta.objects.create(pergunta=p24, texto="A condição de parada", correta=False)
    Resposta.objects.create(pergunta=p24, texto="O incremento/decremento", correta=True)
    Resposta.objects.create(pergunta=p24, texto="A declaração da variável", correta=False)

    p25 = Pergunta.objects.create(assunto=assunto_c_er, texto="Como a palavra-chave break funciona dentro de um laço while em C?", explicacao="Assim como em Python, a instrução break em C...")
    PerguntaDificuldade.objects.create(pergunta=p25, dificuldade=facil)
    Resposta.objects.create(pergunta=p25, texto="Pula para a próxima iteração do laço.", correta=False)
    Resposta.objects.create(pergunta=p25, texto="Encerra a função atual.", correta=False)
    Resposta.objects.create(pergunta=p25, texto="Encerra o laço imediatamente.", correta=True)
    Resposta.objects.create(pergunta=p25, texto="Pausa a execução do laço temporariamente.", correta=False)
    
    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Estruturas de Repetição' de C
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Estruturas de Repetição' de C
    # ...


    # ====================================================================
    # === QUIZ C: ESTRUTURAS CONDICIONAIS ===
    # ====================================================================
    assunto_c_c_nome = 'Estruturas Condicionais'
    assunto_c_c = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_c_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p26 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é a sintaxe para a parte "senão se" em uma estrutura condicional em C?', explicacao="Em C, a estrutura para testar...")
    PerguntaDificuldade.objects.create(pergunta=p26, dificuldade=facil)
    Resposta.objects.create(pergunta=p26, texto="elif", correta=False)
    Resposta.objects.create(pergunta=p26, texto="else if", correta=True)
    Resposta.objects.create(pergunta=p26, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p26, texto="elsif", correta=False)

    p27 = Pergunta.objects.create(assunto=assunto_c_c, texto='Como se escreve a condição "se x é maior ou igual a y" em C?', explicacao="O operador relacional para 'maior ou igual a'...")
    PerguntaDificuldade.objects.create(pergunta=p27, dificuldade=facil)
    Resposta.objects.create(pergunta=p27, texto="if (x >= y)", correta=True)
    Resposta.objects.create(pergunta=p27, texto="if x >= y then", correta=False)
    Resposta.objects.create(pergunta=p27, texto="if [x >= y]", correta=False)
    Resposta.objects.create(pergunta=p27, texto="if (x >|= y)", correta=False)

    p28 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é o operador lógico para "OU" em C?', explicacao="O operador lógico 'OU' em C é representado...")
    PerguntaDificuldade.objects.create(pergunta=p28, dificuldade=facil)
    Resposta.objects.create(pergunta=p28, texto="or", correta=False)
    Resposta.objects.create(pergunta=p28, texto="||", correta=True)
    Resposta.objects.create(pergunta=p28, texto="|", correta=False)
    Resposta.objects.create(pergunta=p28, texto="OR", correta=False)

    p29 = Pergunta.objects.create(assunto=assunto_c_c, texto="Além de if-else, qual outra estrutura de seleção permite testar uma variável contra uma lista de valores?", explicacao="A estrutura switch permite...")
    PerguntaDificuldade.objects.create(pergunta=p29, dificuldade=facil)
    Resposta.objects.create(pergunta=p29, texto="select", correta=False)
    Resposta.objects.create(pergunta=p29, texto="case", correta=False)
    Resposta.objects.create(pergunta=p29, texto="match", correta=False)
    Resposta.objects.create(pergunta=p29, texto="switch", correta=True)

    p30 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual operador é usado para comparação de igualdade em C?", explicacao="Em C, o sinal de igual único (=) é para atribuição...")
    PerguntaDificuldade.objects.create(pergunta=p30, dificuldade=facil)
    Resposta.objects.create(pergunta=p30, texto="=", correta=False)
    Resposta.objects.create(pergunta=p30, texto=":=", correta=False)
    Resposta.objects.create(pergunta=p30, texto="eq", correta=False)
    Resposta.objects.create(pergunta=p30, texto="==", correta=True)
    
    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    # Adicione aqui as perguntas de nível MÉDIO para 'Estruturas Condicionais' de C
    # ...

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Estruturas Condicionais' de C
    # ...
class Migration(migrations.Migration):


    dependencies = [
        ('setup', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(popular_dados),
    ]

