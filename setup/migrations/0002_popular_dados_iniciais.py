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
    p1 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Como você declara uma variável chamada idade com o valor 25 em Python?", explicacao="Python utiliza tipagem dinâmica, então basta atribuir o valor à variável sem declarar seu tipo explicitamente.")
    PerguntaDificuldade.objects.create(pergunta=p1, dificuldade=facil)
    Resposta.objects.create(pergunta=p1, texto="int idade = 25", correta=False)
    Resposta.objects.create(pergunta=p1, texto="idade = 25", correta=True)
    Resposta.objects.create(pergunta=p1, texto="idade := 25", correta=False)
    Resposta.objects.create(pergunta=p1, texto="let idade = 25", correta=False)

    p2 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o símbolo usado para escrever um comentário de uma única linha em Python?", explicacao="Em Python, o caractere '#' (cerquilha) é usado para iniciar um comentário que vai até o final da linha.")
    PerguntaDificuldade.objects.create(pergunta=p2, dificuldade=facil)
    Resposta.objects.create(pergunta=p2, texto="//", correta=False)
    Resposta.objects.create(pergunta=p2, texto="/* ... */", correta=False)
    Resposta.objects.create(pergunta=p2, texto="#", correta=True)
    Resposta.objects.create(pergunta=p2, texto="``", correta=False)

    p3 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual função é usada para imprimir uma mensagem no console em Python?", explicacao="A função `print()` é uma das funções built-in mais comuns de Python, usada para exibir saídas no console.")
    PerguntaDificuldade.objects.create(pergunta=p3, dificuldade=facil)
    Resposta.objects.create(pergunta=p3, texto="console.log()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="System.out.println()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="echo()", correta=False)
    Resposta.objects.create(pergunta=p3, texto="print()", correta=True)

    p4 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o tipo de dado de resultado = 10 / 2 em Python 3?", explicacao="Em Python 3, o operador de divisão `/` sempre retorna um número de ponto flutuante (float), mesmo que a divisão seja exata.")
    PerguntaDificuldade.objects.create(pergunta=p4, dificuldade=facil)
    Resposta.objects.create(pergunta=p4, texto="int", correta=False)
    Resposta.objects.create(pergunta=p4, texto="float", correta=True)
    Resposta.objects.create(pergunta=p4, texto="string", correta=False)
    Resposta.objects.create(pergunta=p4, texto="double", correta=False)

    p5 = Pergunta.objects.create(assunto=assunto_py_sb, texto='Como você converte uma string "100" para um número inteiro em Python?', explicacao="Python oferece funções de conversão de tipo, como `int()`, `float()`, e `str()`, para converter entre diferentes tipos de dados.")
    PerguntaDificuldade.objects.create(pergunta=p5, dificuldade=facil)
    Resposta.objects.create(pergunta=p5, texto='(int)"100"', correta=False)
    Resposta.objects.create(pergunta=p5, texto='to_int("100")', correta=False)
    Resposta.objects.create(pergunta=p5, texto='int("100")', correta=True)
    Resposta.objects.create(pergunta=p5, texto='integer("100")', correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p6 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual será o valor da variável `c` após a execução do código `a, *b, c = [10, 20, 30, 40, 50]`?", explicacao="Esta sintaxe é chamada de 'desempacotamento estendido'. 'a' recebe o primeiro elemento (10), '*b' recebe todos os elementos do meio como uma lista ([20, 30, 40]), e 'c' recebe o último elemento (50).")
    PerguntaDificuldade.objects.create(pergunta=p6, dificuldade=medio)
    Resposta.objects.create(pergunta=p6, texto="30", correta=False)
    Resposta.objects.create(pergunta=p6, texto="[20, 30, 40]", correta=False)
    Resposta.objects.create(pergunta=p6, texto="50", correta=True)
    Resposta.objects.create(pergunta=p6, texto="[40, 50]", correta=False)

    p7 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o resultado da impressão do seguinte f-string: `valor = 12; print(f'O resultado é {valor:04d}')`?", explicacao="A formatação `:04d` significa: 'd' para tratar como decimal, '4' para ter uma largura total de 4 caracteres, e '0' para preencher com zeros à esquerda se o número for menor que a largura.")
    PerguntaDificuldade.objects.create(pergunta=p7, dificuldade=medio)
    Resposta.objects.create(pergunta=p7, texto="O resultado é 12", correta=False)
    Resposta.objects.create(pergunta=p7, texto="O resultado é 0012", correta=True)
    Resposta.objects.create(pergunta=p7, texto="O resultado é 1200", correta=False)
    Resposta.objects.create(pergunta=p7, texto="O resultado é {valor:04d}", correta=False)

    p8 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Considere o código: `lista_a = [1, 2]; lista_b = lista_a; lista_b.append(3)`. Qual será o conteúdo de `lista_a`?", explicacao="Listas são objetos mutáveis. `lista_b = lista_a` faz com que ambas as variáveis apontem para o mesmo objeto na memória. Portanto, uma alteração em `lista_b` também afeta `lista_a`.")
    PerguntaDificuldade.objects.create(pergunta=p8, dificuldade=medio)
    Resposta.objects.create(pergunta=p8, texto="[1, 2]", correta=False)
    Resposta.objects.create(pergunta=p8, texto="[1, 2, 3]", correta=True)
    Resposta.objects.create(pergunta=p8, texto="[3]", correta=False)
    Resposta.objects.create(pergunta=p8, texto="O código resultará em um erro.", correta=False)

    p9 = Pergunta.objects.create(assunto=assunto_py_sb, texto='Qual é a maneira mais "pythônica" de inverter a string `s = "python"`?', explicacao="A sintaxe de fatiamento (slicing) `[::-1]` é a forma idiomática e mais eficiente de criar uma cópia invertida de uma sequência em Python. `s.reverse()` não existe para strings.")
    PerguntaDificuldade.objects.create(pergunta=p9, dificuldade=medio)
    Resposta.objects.create(pergunta=p9, texto="s.reverse()", correta=False)
    Resposta.objects.create(pergunta=p9, texto="reversed(s)", correta=False)
    Resposta.objects.create(pergunta=p9, texto="s[::-1]", correta=True)
    Resposta.objects.create(pergunta=p9, texto="for c in s: s = c + s", correta=False)

    p10 = Pergunta.objects.create(assunto=assunto_py_sb, texto="O que a expressão `(1, 2, 3) + (4, 5)` produzirá?", explicacao="Embora as tuplas sejam imutáveis, o operador `+` pode ser usado para concatená-las. Isso não modifica as tuplas originais, mas cria uma nova tupla contendo os elementos de ambas.")
    PerguntaDificuldade.objects.create(pergunta=p10, dificuldade=medio)
    Resposta.objects.create(pergunta=p10, texto="(1, 2, 3, 4, 5)", correta=True)
    Resposta.objects.create(pergunta=p10, texto="(5, 7, 3)", correta=False)
    Resposta.objects.create(pergunta=p10, texto="Um TypeError, pois tuplas são imutáveis.", correta=False)
    Resposta.objects.create(pergunta=p10, texto="(1, 2, 3, [4, 5])", correta=False)

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Sintaxe Básica' de Python
    # ...

    # ====================================================================
    # === QUIZ PYTHON: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_py_er_nome = 'Estruturas de Repetição'
    assunto_py_er = Assunto.objects.create(linguagem=python, nome=assunto_py_er_nome, slug=slugify(f'{python.nome}-{assunto_py_er_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p11 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual estrutura de repetição é mais adequada para iterar sobre os itens de uma lista?", explicacao="O laço `for` em Python é projetado para iterar diretamente sobre os elementos de uma sequência (como uma lista, tupla ou string).")
    PerguntaDificuldade.objects.create(pergunta=p11, dificuldade=facil)
    Resposta.objects.create(pergunta=p11, texto="O laço while", correta=False)
    Resposta.objects.create(pergunta=p11, texto="O laço do-while", correta=False)
    Resposta.objects.create(pergunta=p11, texto="O laço for", correta=True)
    Resposta.objects.create(pergunta=p11, texto="A recursão", correta=False)

    p12 = Pergunta.objects.create(assunto=assunto_py_er, texto="Como você cria um laço que executa 5 vezes usando a função range()?", explicacao="A função `range(5)` gera uma sequência de números de 0 a 4 (cinco números no total), que é ideal para ser usada em um laço `for` para repetir uma ação 5 vezes.")
    PerguntaDificuldade.objects.create(pergunta=p12, dificuldade=facil)
    Resposta.objects.create(pergunta=p12, texto="for i in range(1, 5):", correta=False)
    Resposta.objects.create(pergunta=p12, texto="for i in range(5):", correta=True)
    Resposta.objects.create(pergunta=p12, texto="for i in range(0, 6):", correta=False)
    Resposta.objects.create(pergunta=p12, texto="for i in range(5-1):", correta=False)

    p13 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave é usada para parar completamente a execução de um laço?", explicacao="A instrução `break` interrompe a execução do laço mais interno (seja `for` ou `while`) e o programa continua na próxima linha após o laço.")
    PerguntaDificuldade.objects.create(pergunta=p13, dificuldade=facil)
    Resposta.objects.create(pergunta=p13, texto="stop", correta=False)
    Resposta.objects.create(pergunta=p13, texto="exit", correta=False)
    Resposta.objects.create(pergunta=p13, texto="break", correta=True)
    Resposta.objects.create(pergunta=p13, texto="return", correta=False)

    p14 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave pula para a próxima iteração de um laço sem terminar o laço por completo?", explicacao="A instrução `continue` interrompe a iteração atual e faz com que o laço pule imediatamente para o início da próxima iteração.")
    PerguntaDificuldade.objects.create(pergunta=p14, dificuldade=facil)
    Resposta.objects.create(pergunta=p14, texto="skip", correta=False)
    Resposta.objects.create(pergunta=p14, texto="next", correta=False)
    Resposta.objects.create(pergunta=p14, texto="pass", correta=False)
    Resposta.objects.create(pergunta=p14, texto="continue", correta=True)

    p15 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável contador for menor que 10?", explicacao="A sintaxe do `while` em Python começa com a palavra-chave `while`, seguida pela condição, e termina com dois pontos (`:`) para iniciar o bloco de código.")
    PerguntaDificuldade.objects.create(pergunta=p15, dificuldade=facil)
    Resposta.objects.create(pergunta=p15, texto="while (contador < 10)", correta=False)
    Resposta.objects.create(pergunta=p15, texto="while contador < 10:", correta=True)
    Resposta.objects.create(pergunta=p15, texto="while: contador < 10", correta=False)
    Resposta.objects.create(pergunta=p15, texto="loop while contador < 10:", correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p16 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que será impresso pelo código `for i in range(5): if i == 3: break; else: print('Fim do laço')`?", explicacao="A cláusula `else` de um laço `for` só é executada se o laço terminar naturalmente (sem ser interrompido por um `break`). Como o `break` é acionado, o `else` é ignorado.")
    PerguntaDificuldade.objects.create(pergunta=p16, dificuldade=medio)
    Resposta.objects.create(pergunta=p16, texto="Fim do laço", correta=False)
    Resposta.objects.create(pergunta=p16, texto="Nada será impresso.", correta=True)
    Resposta.objects.create(pergunta=p16, texto="0 1 2", correta=False)
    Resposta.objects.create(pergunta=p16, texto="O código resultará em um erro de sintaxe.", correta=False)

    p17 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual lista será gerada por: `[i*2 for i in range(5) if i % 2 != 0]`?", explicacao="A list comprehension itera de 0 a 4, a condição `if` filtra apenas os números ímpares (1 e 3), e a expressão `i*2` é aplicada a eles, resultando em 2 e 6.")
    PerguntaDificuldade.objects.create(pergunta=p17, dificuldade=medio)
    Resposta.objects.create(pergunta=p17, texto="[0, 2, 4, 6, 8]", correta=False)
    Resposta.objects.create(pergunta=p17, texto="[2, 6]", correta=True)
    Resposta.objects.create(pergunta=p17, texto="[1, 3]", correta=False)
    Resposta.objects.create(pergunta=p17, texto="[0, 1, 2, 3, 4]", correta=False)

    p18 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual a saída do código `count=0; for i in range(2): for j in range(3): if j==1: continue; count+=1; print(count)`?", explicacao="O laço externo roda 2 vezes. O laço interno roda 3 vezes, mas pula a iteração quando j==1. Portanto, o `count` é incrementado quando (j=0, j=2) para i=0, e (j=0, j=2) para i=1. Total de 4 incrementos.")
    PerguntaDificuldade.objects.create(pergunta=p18, dificuldade=medio)
    Resposta.objects.create(pergunta=p18, texto="6", correta=False)
    Resposta.objects.create(pergunta=p18, texto="5", correta=False)
    Resposta.objects.create(pergunta=p18, texto="4", correta=True)
    Resposta.objects.create(pergunta=p18, texto="3", correta=False)

    p19 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que a função `enumerate` faz em um laço `for`?", explicacao="`enumerate` é uma função que adiciona um contador a um iterável. Ela retorna tuplas contendo o índice e o valor de cada item, sendo a forma idiomática de obter ambos em um laço.")
    PerguntaDificuldade.objects.create(pergunta=p19, dificuldade=medio)
    Resposta.objects.create(pergunta=p19, texto="Enumera a quantidade de memória usada por cada item da lista.", correta=False)
    Resposta.objects.create(pergunta=p19, texto="Retorna uma tupla contendo um contador (índice) e o valor de cada item da sequência.", correta=True)
    Resposta.objects.create(pergunta=p19, texto="Verifica se os itens da lista são numéricos.", correta=False)
    Resposta.objects.create(pergunta=p19, texto="Executa o laço um número fixo de vezes, independentemente do tamanho da lista.", correta=False)

    p20 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que acontece no laço `letras=['a','b','c']; while letras: print(letras.pop(0))`?", explicacao="A condição `while letras:` é verdadeira enquanto a lista não estiver vazia. `letras.pop(0)` remove e retorna o primeiro elemento ('a', depois 'b', depois 'c'), esvaziando a lista e encerrando o laço.")
    PerguntaDificuldade.objects.create(pergunta=p20, dificuldade=medio)
    Resposta.objects.create(pergunta=p20, texto="Entra em um loop infinito.", correta=False)
    Resposta.objects.create(pergunta=p20, texto="Imprime 'a', 'b', e 'c', cada um em uma nova linha.", correta=True)
    Resposta.objects.create(pergunta=p20, texto="Imprime 'c', 'b', e 'a', cada um em uma nova linha.", correta=False)
    Resposta.objects.create(pergunta=p20, texto="Gera um IndexError.", correta=False)
    
    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Estruturas de Repetição' de Python
    # ...

    # ====================================================================
    # === QUIZ PYTHON: CONDICIONAIS ===
    # ====================================================================
    assunto_py_c_nome = 'Condicionais'
    assunto_py_c = Assunto.objects.create(linguagem=python, nome=assunto_py_c_nome, slug=slugify(f'{python.nome}-{assunto_py_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p21 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual palavra-chave é usada para a parte "senão se" em uma estrutura condicional em Python?', explicacao="Python utiliza a contração `elif` para 'else if', tornando o código mais conciso.")
    PerguntaDificuldade.objects.create(pergunta=p21, dificuldade=facil)
    Resposta.objects.create(pergunta=p21, texto="else if", correta=False)
    Resposta.objects.create(pergunta=p21, texto="elif", correta=True)
    Resposta.objects.create(pergunta=p21, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p21, texto="elsif", correta=False)
    
    p22 = Pergunta.objects.create(assunto=assunto_py_c, texto='Como se escreve a condição "se a não for igual a b" em Python?', explicacao="O operador de desigualdade em Python é `!=`. A expressão `a is not b` verifica se `a` e `b` são objetos diferentes na memória, o que é uma verificação mais estrita.")
    PerguntaDificuldade.objects.create(pergunta=p22, dificuldade=facil)
    Resposta.objects.create(pergunta=p22, texto="if a <> b:", correta=False)
    Resposta.objects.create(pergunta=p22, texto="if not(a == b):", correta=False)
    Resposta.objects.create(pergunta=p22, texto="if a != b:", correta=True)
    Resposta.objects.create(pergunta=p22, texto="if a is not b:", correta=False)

    p23 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é o operador lógico para "E" em Python?', explicacao="Python usa palavras em inglês (`and`, `or`, `not`) para operadores lógicos, em vez de símbolos como `&&` ou `||`.")
    PerguntaDificuldade.objects.create(pergunta=p23, dificuldade=facil)
    Resposta.objects.create(pergunta=p23, texto="&&", correta=False)
    Resposta.objects.create(pergunta=p23, texto="and", correta=True)
    Resposta.objects.create(pergunta=p23, texto="&", correta=False)
    Resposta.objects.create(pergunta=p23, texto="AND", correta=False)

    p24 = Pergunta.objects.create(assunto=assunto_py_c, texto="O que a seguinte expressão booleana retornaria: not (True and False)?", explicacao="A ordem de operação é: primeiro o que está dentro dos parênteses (`True and False` resulta em `False`), depois o `not` (`not False` resulta em `True`).")
    PerguntaDificuldade.objects.create(pergunta=p24, dificuldade=facil)
    Resposta.objects.create(pergunta=p24, texto="True", correta=True)
    Resposta.objects.create(pergunta=p24, texto="False", correta=False)
    Resposta.objects.create(pergunta=p24, texto="None", correta=False)
    Resposta.objects.create(pergunta=p24, texto="Error", correta=False)

    p25 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é a sintaxe correta para um bloco if em Python que verifica se a variável nome é igual a "Ana"?', explicacao="A sintaxe de um `if` em Python exige o operador de comparação `==`, e o bloco de código é iniciado por dois pontos (`:`).")
    PerguntaDificuldade.objects.create(pergunta=p25, dificuldade=facil)
    Resposta.objects.create(pergunta=p25, texto='if (nome == "Ana")', correta=False)
    Resposta.objects.create(pergunta=p25, texto='if nome = "Ana":', correta=False)
    Resposta.objects.create(pergunta=p25, texto='if nome == "Ana":', correta=True)
    Resposta.objects.create(pergunta=p25, texto='if nome is "Ana" then', correta=False)
    
    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p26 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual será o valor de `resultado` após a execução do código: `x = 0; resultado = "A" if x else "B"`?', explicacao="Este é o operador ternário do Python. A condição avalia a 'veracidade' de `x`. Em Python, `0` é considerado `False`, portanto, o valor após o `else` é retornado.")
    PerguntaDificuldade.objects.create(pergunta=p26, dificuldade=medio)
    Resposta.objects.create(pergunta=p26, texto='"A"', correta=False)
    Resposta.objects.create(pergunta=p26, texto='"B"', correta=True)
    Resposta.objects.create(pergunta=p26, texto="True", correta=False)
    Resposta.objects.create(pergunta=p26, texto="O código resultará em um erro.", correta=False)

    p27 = Pergunta.objects.create(assunto=assunto_py_c, texto='O que a expressão `[] or 0 or "Olá"` retornará?', explicacao="O operador `or` retorna o primeiro valor 'truthy' (verdadeiro) que encontrar. Uma lista vazia (`[]`) e o número `0` são 'falsy'. A string não vazia `\"Olá\"` é 'truthy', então ela é retornada.")
    PerguntaDificuldade.objects.create(pergunta=p27, dificuldade=medio)
    Resposta.objects.create(pergunta=p27, texto="False", correta=False)
    Resposta.objects.create(pergunta=p27, texto="[]", correta=False)
    Resposta.objects.create(pergunta=p27, texto='"Olá"', correta=True)
    Resposta.objects.create(pergunta=p27, texto="True", correta=False)

    p28 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual o resultado da expressão `True or False and not True`?", explicacao="A precedência de operadores é `not`, depois `and`, depois `or`. A expressão é avaliada como `True or (False and (not True))` -> `True or (False and False)` -> `True or False`, que resulta em `True`.")
    PerguntaDificuldade.objects.create(pergunta=p28, dificuldade=medio)
    Resposta.objects.create(pergunta=p28, texto="True", correta=True)
    Resposta.objects.create(pergunta=p28, texto="False", correta=False)
    Resposta.objects.create(pergunta=p28, texto="None", correta=False)
    Resposta.objects.create(pergunta=p28, texto="SyntaxError", correta=False)

    p29 = Pergunta.objects.create(assunto=assunto_py_c, texto="Considere `a = [1]; b = [1]`. Qual o resultado de `a == b` e `a is b`, respectivamente?", explicacao="O operador `==` compara o VALOR dos objetos (ambas as listas contêm `[1]`, então é `True`). O operador `is` compara a IDENTIDADE (se são o mesmo objeto na memória, o que não são, então é `False`).")
    PerguntaDificuldade.objects.create(pergunta=p29, dificuldade=medio)
    Resposta.objects.create(pergunta=p29, texto="True, True", correta=False)
    Resposta.objects.create(pergunta=p29, texto="False, False", correta=False)
    Resposta.objects.create(pergunta=p29, texto="True, False", correta=True)
    Resposta.objects.create(pergunta=p29, texto="False, True", correta=False)

    p30 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual será o valor de `y` no código `x=5; if 3<x<4: y=1; elif 4<x<6: y=2; else: y=3`?", explicacao="Python permite comparações encadeadas. A expressão `4 < x < 6` é o mesmo que `4 < x and x < 6`. Como `x` é 5, essa condição é verdadeira, e `y` recebe o valor 2.")
    PerguntaDificuldade.objects.create(pergunta=p30, dificuldade=medio)
    Resposta.objects.create(pergunta=p30, texto="1", correta=False)
    Resposta.objects.create(pergunta=p30, texto="2", correta=True)
    Resposta.objects.create(pergunta=p30, texto="3", correta=False)
    Resposta.objects.create(pergunta=p30, texto="A variável `y` não será definida.", correta=False)
    
    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Condicionais' de Python
    # ...

    # ====================================================================
    # === QUIZ C: SINTAXE BÁSICA ===
    # ====================================================================
    assunto_c_sb_nome = 'Sintaxe Básica'
    assunto_c_sb = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_sb_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_sb_nome}'))

# --- PERGUNTAS DE NÍVEL FÁCIL ---
    p31 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você declara uma variável inteira chamada quantidade com o valor 50 em C?", explicacao="Em C, uma linguagem de tipagem estática, você deve declarar o tipo da variável (`int`) antes de seu nome e, opcionalmente, inicializá-la.")
    PerguntaDificuldade.objects.create(pergunta=p31, dificuldade=facil)
    Resposta.objects.create(pergunta=p31, texto="quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p31, texto="int quantidade = 50;", correta=True)
    Resposta.objects.create(pergunta=p31, texto="integer quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p31, texto="var quantidade = 50;", correta=False)

    p32 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual é o símbolo usado para indicar o fim de uma instrução em C?", explicacao="O ponto e vírgula (`;`) é um terminador de instrução fundamental em C, sinalizando ao compilador que um comando foi concluído.")
    PerguntaDificuldade.objects.create(pergunta=p32, dificuldade=facil)
    Resposta.objects.create(pergunta=p32, texto=". (ponto final)", correta=False)
    Resposta.objects.create(pergunta=p32, texto=": (dois pontos)", correta=False)
    Resposta.objects.create(pergunta=p32, texto="; (ponto e vírgula)", correta=True)
    Resposta.objects.create(pergunta=p32, texto="O final da linha", correta=False)

    p33 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual função da biblioteca stdio.h é usada para imprimir texto formatado no console?", explicacao="A função `printf()` (print formatted) faz parte da biblioteca de entrada/saída padrão (standard input/output) e é a principal forma de exibir texto no console.")
    PerguntaDificuldade.objects.create(pergunta=p33, dificuldade=facil)
    Resposta.objects.create(pergunta=p33, texto="print()", correta=False)
    Resposta.objects.create(pergunta=p33, texto="cout <<", correta=False)
    Resposta.objects.create(pergunta=p33, texto="printf()", correta=True)
    Resposta.objects.create(pergunta=p33, texto="log()", correta=False)

    p34 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você escreve um comentário de múltiplas linhas em C?", explicacao="Em C, um comentário de bloco começa com `/*` e termina com `*/`, e tudo que estiver entre esses delimitadores é ignorado pelo compilador.")
    PerguntaDificuldade.objects.create(pergunta=p34, dificuldade=facil)
    Resposta.objects.create(pergunta=p34, texto="// ... //", correta=False)
    Resposta.objects.create(pergunta=p34, texto="# ... #", correta=False)
    Resposta.objects.create(pergunta=p34, texto="/* ... */", correta=True)
    Resposta.objects.create(pergunta=p34, texto='""" ... """', correta=False)

    p35 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual diretiva de pré-processador é necessária para usar a função printf?", explicacao="A diretiva `#include <stdio.h>` instrui o pré-processador a incluir o conteúdo do arquivo de cabeçalho da biblioteca padrão de entrada/saída, onde `printf` é declarada.")
    PerguntaDificuldade.objects.create(pergunta=p35, dificuldade=facil)
    Resposta.objects.create(pergunta=p35, texto="#import <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p35, texto="#require <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p35, texto='#include "stdio.h"', correta=False)
    Resposta.objects.create(pergunta=p35, texto="#include <stdio.h>", correta=True)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p36 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o resultado da expressão `(float) 5 / 2` em C?", explicacao="O 'type cast' `(float)` converte o inteiro 5 para um float. Quando um dos operandos da divisão é float, a operação inteira é promovida para uma divisão de ponto flutuante, resultando em 2.5.")
    PerguntaDificuldade.objects.create(pergunta=p36, dificuldade=medio)
    Resposta.objects.create(pergunta=p36, texto="2", correta=False)
    Resposta.objects.create(pergunta=p36, texto="2.5", correta=True)
    Resposta.objects.create(pergunta=p36, texto="2.0", correta=False)
    Resposta.objects.create(pergunta=p36, texto="O código não compila.", correta=False)

    p37 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o valor final de `x` no código `int x = 5; int y = x++;`?", explicacao="O operador de pós-incremento (`x++`) primeiro retorna o valor original de `x` (5, que é atribuído a `y`) e DEPOIS incrementa `x`. Portanto, ao final, `y` vale 5 e `x` vale 6.")
    PerguntaDificuldade.objects.create(pergunta=p37, dificuldade=medio)
    Resposta.objects.create(pergunta=p37, texto="4", correta=False)
    Resposta.objects.create(pergunta=p37, texto="5", correta=False)
    Resposta.objects.create(pergunta=p37, texto="6", correta=True)
    Resposta.objects.create(pergunta=p37, texto="`y` não pode ser inicializado dessa forma.", correta=False)

    p38 = Pergunta.objects.create(assunto=assunto_c_sb, texto="O que a macro `#define QUADRADO(a) a * a` fará com a expressão `QUADRADO(2 + 3)`?", explicacao="O pré-processador faz uma substituição textual, expandindo a macro para `2 + 3 * 2 + 3`. Devido à precedência de operadores (multiplicação antes da adição), o cálculo é `2 + 6 + 3`, que resulta em 11.")
    PerguntaDificuldade.objects.create(pergunta=p38, dificuldade=medio)
    Resposta.objects.create(pergunta=p38, texto="A expressão resultará em 25.", correta=False)
    Resposta.objects.create(pergunta=p38, texto="A expressão resultará em 11.", correta=True)
    Resposta.objects.create(pergunta=p38, texto="A expressão resultará em 10.", correta=False)
    Resposta.objects.create(pergunta=p38, texto="O código não compilará devido à macro.", correta=False)

    p39 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Se `ptr` é um ponteiro para um inteiro, o que a expressão `*ptr` acessa?", explicacao="O operador `*` (asterisco), quando usado em um ponteiro, é o operador de dereferência. Ele acessa o VALOR que está armazenado no endereço de memória para o qual o ponteiro aponta.")
    PerguntaDificuldade.objects.create(pergunta=p39, dificuldade=medio)
    Resposta.objects.create(pergunta=p39, texto="O endereço de memória do ponteiro `ptr`.", correta=False)
    Resposta.objects.create(pergunta=p39, texto="O endereço de memória para o qual `ptr` aponta.", correta=False)
    Resposta.objects.create(pergunta=p39, texto="O valor armazenado no endereço de memória para o qual `ptr` aponta.", correta=True)
    Resposta.objects.create(pergunta=p39, texto="O tamanho do tipo de dado inteiro.", correta=False)

    p40 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o valor da constante `TERCA` no `enum dia { DOMINGO, SEGUNDA, TERCA, QUARTA };`?", explicacao="Por padrão, os membros de uma enumeração (`enum`) em C recebem valores inteiros sequenciais começando em 0. Portanto, DOMINGO=0, SEGUNDA=1, e TERCA=2.")
    PerguntaDificuldade.objects.create(pergunta=p40, dificuldade=medio)
    Resposta.objects.create(pergunta=p40, texto="1", correta=False)
    Resposta.objects.create(pergunta=p40, texto="2", correta=True)
    Resposta.objects.create(pergunta=p40, texto="3", correta=False)
    Resposta.objects.create(pergunta=p40, texto="TERCA", correta=False)
    
    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Sintaxe Básica' de C
    # ...

    # ====================================================================
    # === QUIZ C: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_c_er_nome = 'Estruturas de Repetição'
    assunto_c_er = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_er_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_er_nome}'))

# --- PERGUNTAS DE NÍVEL FÁCIL ---
    p41 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe completa de um laço for em C que vai de 0 a 9?", explicacao="O laço for em C tem três partes entre parênteses, separadas por ponto e vírgula: inicialização, condição e incremento/decremento.")
    PerguntaDificuldade.objects.create(pergunta=p41, dificuldade=facil)
    Resposta.objects.create(pergunta=p41, texto="for (int i=0; i < 10; i++)", correta=True)
    Resposta.objects.create(pergunta=p41, texto="for (i < 10; i++)", correta=False)
    Resposta.objects.create(pergunta=p41, texto="for (int i=0; i < 10)", correta=False)
    Resposta.objects.create(pergunta=p41, texto="for (int i=0 to 9)", correta=False)

    p42 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual laço em C garante que seu corpo seja executado pelo menos uma vez?", explicacao="O laço `do-while` é uma estrutura de pós-teste; o corpo do laço é executado primeiro e a condição é verificada depois, garantindo ao menos uma execução.")
    PerguntaDificuldade.objects.create(pergunta=p42, dificuldade=facil)
    Resposta.objects.create(pergunta=p42, texto="for", correta=False)
    Resposta.objects.create(pergunta=p42, texto="while", correta=False)
    Resposta.objects.create(pergunta=p42, texto="do-while", correta=True)
    Resposta.objects.create(pergunta=p42, texto="repeat-until", correta=False)

    p43 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável ativo for verdadeira (considerando 1 como verdadeiro)?", explicacao="A sintaxe do laço `while` em C requer que a condição esteja entre parênteses. `while (ativo)` é equivalente a `while (ativo != 0)`.")
    PerguntaDificuldade.objects.create(pergunta=p43, dificuldade=facil)
    Resposta.objects.create(pergunta=p43, texto="while [ativo == 1]", correta=False)
    Resposta.objects.create(pergunta=p43, texto="while (ativo)", correta=True)
    Resposta.objects.create(pergunta=p43, texto="while {ativo}", correta=False)
    Resposta.objects.create(pergunta=p43, texto="while ativo is 1", correta=False)

    p44 = Pergunta.objects.create(assunto=assunto_c_er, texto="Dentro de um laço for, o que a terceira expressão (i++) geralmente representa?", explicacao="A terceira parte da declaração de um laço `for` é a expressão de passo, executada ao final de cada iteração, tipicamente para incrementar ou decrementar a variável de controle.")
    PerguntaDificuldade.objects.create(pergunta=p44, dificuldade=facil)
    Resposta.objects.create(pergunta=p44, texto="A inicialização", correta=False)
    Resposta.objects.create(pergunta=p44, texto="A condição de parada", correta=False)
    Resposta.objects.create(pergunta=p44, texto="O incremento/decremento", correta=True)
    Resposta.objects.create(pergunta=p44, texto="A declaração da variável", correta=False)

    p45 = Pergunta.objects.create(assunto=assunto_c_er, texto="Como a palavra-chave break funciona dentro de um laço while em C?", explicacao="A instrução `break` em C causa a terminação imediata do laço mais interno em que se encontra, transferindo o controle do programa para a instrução seguinte ao laço.")
    PerguntaDificuldade.objects.create(pergunta=p45, dificuldade=facil)
    Resposta.objects.create(pergunta=p45, texto="Pula para a próxima iteração do laço.", correta=False)
    Resposta.objects.create(pergunta=p45, texto="Encerra a função atual.", correta=False)
    Resposta.objects.create(pergunta=p45, texto="Encerra o laço imediatamente.", correta=True)
    Resposta.objects.create(pergunta=p45, texto="Pausa a execução do laço temporariamente.", correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p46 = Pergunta.objects.create(assunto=assunto_c_er, texto="Quantas vezes a palavra \"Teste\" será impressa? `int i=5; do{ printf(\"Teste\\n\"); }while(i>10);`", explicacao="O laço `do-while` sempre executa seu corpo pelo menos uma vez, pois a condição só é verificada no final. 'Teste' é impresso, então `5 > 10` é avaliado como falso e o laço termina.")
    PerguntaDificuldade.objects.create(pergunta=p46, dificuldade=medio)
    Resposta.objects.create(pergunta=p46, texto="0 vezes", correta=False)
    Resposta.objects.create(pergunta=p46, texto="1 vez", correta=True)
    Resposta.objects.create(pergunta=p46, texto="5 vezes", correta=False)
    Resposta.objects.create(pergunta=p46, texto="Infinitas vezes", correta=False)

    p47 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual o valor final de `j`? `int i,j; for(i=0,j=10; i<5; i++,j--){ /*vazio*/ }`", explicacao="O laço executa 5 vezes (para i de 0 a 4). A cada iteração, `j` é decrementado. Inicia em 10, e após 5 decrementos (para i=0,1,2,3,4), seu valor final será 5.")
    PerguntaDificuldade.objects.create(pergunta=p47, dificuldade=medio)
    Resposta.objects.create(pergunta=p47, texto="10", correta=False)
    Resposta.objects.create(pergunta=p47, texto="0", correta=False)
    Resposta.objects.create(pergunta=p47, texto="5", correta=True)
    Resposta.objects.create(pergunta=p47, texto="4", correta=False)

    p48 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a forma idiomática em C para criar um laço infinito?", explicacao="Todas as opções são formas válidas e comuns de criar um laço infinito. `while(1)` usa uma condição que é sempre verdadeira. `for(;;)` omite todas as partes do `for`, resultando em um laço sem condição de parada.")
    PerguntaDificuldade.objects.create(pergunta=p48, dificuldade=medio)
    Resposta.objects.create(pergunta=p48, texto="while (1)", correta=False)
    Resposta.objects.create(pergunta=p48, texto="for (;;)", correta=False)
    Resposta.objects.create(pergunta=p48, texto="do {} while(true);", correta=False)
    Resposta.objects.create(pergunta=p48, texto="Todas as alternativas estão corretas.", correta=True)

    p49 = Pergunta.objects.create(assunto=assunto_c_er, texto="O que a instrução `break` faz dentro de laços aninhados?", explicacao="A instrução `break` sempre se aplica apenas ao escopo do laço mais próximo (o mais interno) em que está contida. Ela não afeta os laços externos.")
    PerguntaDificuldade.objects.create(pergunta=p49, dificuldade=medio)
    Resposta.objects.create(pergunta=p49, texto="Interrompe a execução de ambos os laços `for`.", correta=False)
    Resposta.objects.create(pergunta=p49, texto="Interrompe a execução apenas do laço `for` mais interno (o de `j`).", correta=True)
    Resposta.objects.create(pergunta=p49, texto="Interrompe a execução apenas do laço `for` mais externo (o de `i`).", correta=False)
    Resposta.objects.create(pergunta=p49, texto="Pula a iteração atual de ambos os laços.", correta=False)

    p50 = Pergunta.objects.create(assunto=assunto_c_er, texto="O que este código faz? `int arr[]={10,20,30}; int *ptr=arr; while(ptr<arr+3){ printf(\"%d \",*ptr); ptr++; }`", explicacao="Isso demonstra a iteração sobre um array usando aritmética de ponteiros. `ptr` começa no primeiro elemento, e a cada iteração, o valor (`*ptr`) é impresso e o ponteiro (`ptr++`) avança para o próximo elemento.")
    PerguntaDificuldade.objects.create(pergunta=p50, dificuldade=medio)
    Resposta.objects.create(pergunta=p50, texto="Imprime os endereços de memória dos elementos do array.", correta=False)
    Resposta.objects.create(pergunta=p50, texto="Entra em um loop infinito.", correta=False)
    Resposta.objects.create(pergunta=p50, texto="Imprime os valores `10 20 30 `.", correta=True)
    Resposta.objects.create(pergunta=p50, texto="Gera um erro de compilação.", correta=False)

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    # Adicione aqui as perguntas de nível DIFÍCIL para 'Estruturas de Repetição' de C
    # ...


    # ====================================================================
    # === QUIZ C: ESTRUTURAS CONDICIONAIS ===
    # ====================================================================
    assunto_c_c_nome = 'Estruturas Condicionais'
    assunto_c_c = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_c_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p51 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é a sintaxe para a parte "senão se" em uma estrutura condicional em C?', explicacao="Em C, a estrutura para testar múltiplas condições sequencialmente é `if`, seguida por uma ou mais cláusulas `else if`, e opcionalmente um `else` no final.")
    PerguntaDificuldade.objects.create(pergunta=p51, dificuldade=facil)
    Resposta.objects.create(pergunta=p51, texto="elif", correta=False)
    Resposta.objects.create(pergunta=p51, texto="else if", correta=True)
    Resposta.objects.create(pergunta=p51, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p51, texto="elsif", correta=False)

    p52 = Pergunta.objects.create(assunto=assunto_c_c, texto='Como se escreve a condição "se x é maior ou igual a y" em C?', explicacao="O operador relacional para 'maior ou igual a' em C é `>=`. A condição deve estar entre parênteses na declaração `if`.")
    PerguntaDificuldade.objects.create(pergunta=p52, dificuldade=facil)
    Resposta.objects.create(pergunta=p52, texto="if (x >= y)", correta=True)
    Resposta.objects.create(pergunta=p52, texto="if x >= y then", correta=False)
    Resposta.objects.create(pergunta=p52, texto="if [x >= y]", correta=False)
    Resposta.objects.create(pergunta=p52, texto="if (x >|= y)", correta=False)

    p53 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é o operador lógico para "OU" em C?', explicacao="O operador lógico 'OU' em C é representado por duas barras verticais (`||`). O operador `|` é o 'OU' bit-a-bit (bitwise).")
    PerguntaDificuldade.objects.create(pergunta=p53, dificuldade=facil)
    Resposta.objects.create(pergunta=p53, texto="or", correta=False)
    Resposta.objects.create(pergunta=p53, texto="||", correta=True)
    Resposta.objects.create(pergunta=p53, texto="|", correta=False)
    Resposta.objects.create(pergunta=p53, texto="OR", correta=False)

    p54 = Pergunta.objects.create(assunto=assunto_c_c, texto="Além de if-else, qual outra estrutura de seleção permite testar uma variável contra uma lista de valores?", explicacao="A estrutura `switch` permite que uma variável seja testada contra uma lista de valores (os `case`), oferecendo uma alternativa mais limpa a múltiplos `else if`.")
    PerguntaDificuldade.objects.create(pergunta=p54, dificuldade=facil)
    Resposta.objects.create(pergunta=p54, texto="select", correta=False)
    Resposta.objects.create(pergunta=p54, texto="case", correta=False)
    Resposta.objects.create(pergunta=p54, texto="match", correta=False)
    Resposta.objects.create(pergunta=p54, texto="switch", correta=True)

    p55 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual operador é usado para comparação de igualdade em C?", explicacao="Em C, o sinal de igual único (`=`) é para atribuição de valor. Para comparar se dois valores são iguais, deve-se usar o sinal de igual duplo (`==`).")
    PerguntaDificuldade.objects.create(pergunta=p55, dificuldade=facil)
    Resposta.objects.create(pergunta=p55, texto="=", correta=False)
    Resposta.objects.create(pergunta=p55, texto=":=", correta=False)
    Resposta.objects.create(pergunta=p55, texto="eq", correta=False)
    Resposta.objects.create(pergunta=p55, texto="==", correta=True)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p56 = Pergunta.objects.create(assunto=assunto_c_c, texto="O que será impresso pelo código `int x=0; if(x=5){ printf(\"Verdadeiro\"); } else { printf(\"Falso\"); }`?", explicacao="O erro comum `x=5` é uma ATRIBUIÇÃO, não uma comparação. O valor da expressão de atribuição é 5. Em C, qualquer valor diferente de zero é `true`, então o bloco `if` é executado.")
    PerguntaDificuldade.objects.create(pergunta=p56, dificuldade=medio)
    Resposta.objects.create(pergunta=p56, texto="Falso", correta=False)
    Resposta.objects.create(pergunta=p56, texto="Verdadeiro", correta=True)
    Resposta.objects.create(pergunta=p56, texto="Nada será impresso.", correta=False)
    Resposta.objects.create(pergunta=p56, texto="O código não compilará devido a `x = 5`.", correta=False)

    p57 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual será a saída do switch: `int op=2; switch(op){ case 1:printf(\"A\"); case 2:printf(\"B\"); case 3:printf(\"C\");break; default:printf(\"D\"); }`?", explicacao="O `switch` executa o `case 2`, imprimindo 'B'. Como não há `break` no `case 2`, a execução 'cai' (fall-through) para o `case 3`, imprimindo 'C'. Então, encontra o `break` e sai.")
    PerguntaDificuldade.objects.create(pergunta=p57, dificuldade=medio)
    Resposta.objects.create(pergunta=p57, texto="B", correta=False)
    Resposta.objects.create(pergunta=p57, texto="C", correta=False)
    Resposta.objects.create(pergunta=p57, texto="BC", correta=True)
    Resposta.objects.create(pergunta=p57, texto="BCD", correta=False)

    p58 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor de `x` após: `int x = 10; if (x > 5 || ++x == 10) { /*...*/ }`?", explicacao="O operador OU (`||`) usa 'avaliação de curto-circuito'. Como a primeira parte (`x > 5`) é verdadeira, a segunda parte (`++x == 10`) nunca é avaliada. Portanto, `x` não é incrementado e permanece 10.")
    PerguntaDificuldade.objects.create(pergunta=p58, dificuldade=medio)
    Resposta.objects.create(pergunta=p58, texto="10", correta=True)
    Resposta.objects.create(pergunta=p58, texto="11", correta=False)
    Resposta.objects.create(pergunta=p58, texto="9", correta=False)
    Resposta.objects.create(pergunta=p58, texto="O comportamento é indefinido.", correta=False)

    p59 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor final de `maior` em: `int a=15, b=20; int maior = (a > b) ? a : b;`?", explicacao="Este é o operador ternário. A condição `(a > b)` é `(15 > 20)`, que é falsa. Portanto, a expressão retorna o valor após os dois pontos (`:`), que é `b` (ou seja, 20).")
    PerguntaDificuldade.objects.create(pergunta=p59, dificuldade=medio)
    Resposta.objects.create(pergunta=p59, texto="15", correta=False)
    Resposta.objects.create(pergunta=p59, texto="20", correta=True)
    Resposta.objects.create(pergunta=p59, texto="0", correta=False)
    Resposta.objects.create(pergunta=p59, texto="O código tem um erro de sintaxe.", correta=False)

    p60 = Pergunta.objects.create(assunto=assunto_c_c, texto="O que a condição `if (num & 1)` verifica?", explicacao="`&` é o operador E bit-a-bit. `num & 1` resulta em `1` apenas se o último bit de `num` for 1 (característica de todos os números ímpares). Se for par (último bit 0), o resultado é 0 (falso).")
    PerguntaDificuldade.objects.create(pergunta=p60, dificuldade=medio)
    Resposta.objects.create(pergunta=p60, texto="Se `num` é igual a 1.", correta=False)
    Resposta.objects.create(pergunta=p60, texto="Se `num` é um número par.", correta=False)
    Resposta.objects.create(pergunta=p60, texto="Se `num` é um número ímpar.", correta=True)
    Resposta.objects.create(pergunta=p60, texto="Se `num` é maior que 1.", correta=False)

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

