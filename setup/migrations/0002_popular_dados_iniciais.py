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
    p11 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual será o valor de `len(s)` após a execução de `s = {'a': 1, 'b': 2}; s.update(c=3); del s['a']`?", explicacao="O dicionário `s` inicia com 2 elementos. `s.update(c=3)` adiciona um novo elemento, resultando em 3. `del s['a']` remove um elemento, resultando em 2. A função `len()` retorna o número de pares chave-valor.")
    PerguntaDificuldade.objects.create(pergunta=p11, dificuldade=dificil)
    Resposta.objects.create(pergunta=p11, texto="1", correta=False)
    Resposta.objects.create(pergunta=p11, texto="2", correta=True)
    Resposta.objects.create(pergunta=p11, texto="3", correta=False)
    Resposta.objects.create(pergunta=p11, texto="4", correta=False)

    p12 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o resultado da avaliação da expressão booleana: `1 < 2 < 3 or 10 and not 0`?", explicacao="A expressão `1 < 2 < 3` é avaliada como `True`. A expressão `10 and not 0` é avaliada como `10 and True`, que retorna `10`. A expressão final é `True or 10`. Em um contexto booleano, `True` é retornado em operações `or` se for o primeiro operando verdadeiro.")
    PerguntaDificuldade.objects.create(pergunta=p12, dificuldade=dificil)
    Resposta.objects.create(pergunta=p12, texto="True", correta=True)
    Resposta.objects.create(pergunta=p12, texto="1", correta=False)
    Resposta.objects.create(pergunta=p12, texto="10", correta=False)
    Resposta.objects.create(pergunta=p12, texto="False", correta=False)

    p13 = Pergunta.objects.create(assunto=assunto_py_sb, texto="O que o seguinte código imprime: `a = 5; b = 5; print(a is b)` e `a = 500; b = 500; print(a is b)`?", explicacao="Python 'interna' (cacheia) inteiros pequenos (geralmente de -5 a 256) por razões de otimização de memória. Para `a = 5; b = 5`, ambas as variáveis apontam para o mesmo objeto, então `a is b` é `True`. Para `a = 500; b = 500`, eles são criados como objetos separados, então `a is b` é `False` (em CPython, o interpretador padrão).")
    PerguntaDificuldade.objects.create(pergunta=p13, dificuldade=dificil)
    Resposta.objects.create(pergunta=p13, texto="True e True", correta=False)
    Resposta.objects.create(pergunta=p13, texto="False e False", correta=False)
    Resposta.objects.create(pergunta=p13, texto="True e False", correta=True)
    Resposta.objects.create(pergunta=p13, texto="False e True", correta=False)

    p14 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Considere o código: `x = 10; def func(): global x; x += 1; print(x); func()`. Qual será a saída?", explicacao="A palavra-chave `global x` dentro da função `func` indica que a variável `x` a ser modificada é a variável global e não uma variável local. O valor global de `x` é 10, que é incrementado para 11 e depois impresso.")
    PerguntaDificuldade.objects.create(pergunta=p14, dificuldade=dificil)
    Resposta.objects.create(pergunta=p14, texto="10", correta=False)
    Resposta.objects.create(pergunta=p14, texto="11", correta=True)
    Resposta.objects.create(pergunta=p14, texto="NameError", correta=False)
    Resposta.objects.create(pergunta=p14, texto="UnboundLocalError", correta=False)

    p15 = Pergunta.objects.create(assunto=assunto_py_sb, texto="Qual é o valor final de `y` após a execução do código: `x = 1; y = x; x = 2; print(y)`?", explicacao="Como `x` é um inteiro (tipo imutável), a linha `y = x` faz com que `y` receba uma cópia do valor (1). A linha `x = 2` faz com que a variável `x` aponte para um novo objeto (o inteiro 2), mas não afeta o valor do objeto para o qual `y` aponta (o inteiro 1).")
    PerguntaDificuldade.objects.create(pergunta=p15, dificuldade=dificil)
    Resposta.objects.create(pergunta=p15, texto="1", correta=True)
    Resposta.objects.create(pergunta=p15, texto="2", correta=False)
    Resposta.objects.create(pergunta=p15, texto="None", correta=False)
    Resposta.objects.create(pergunta=p15, texto="TypeError", correta=False)

    # ====================================================================
    # === QUIZ PYTHON: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_py_er_nome = 'Estruturas de Repetição'
    assunto_py_er = Assunto.objects.create(linguagem=python, nome=assunto_py_er_nome, slug=slugify(f'{python.nome}-{assunto_py_er_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p16 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual estrutura de repetição é mais adequada para iterar sobre os itens de uma lista?", explicacao="O laço `for` em Python é projetado para iterar diretamente sobre os elementos de uma sequência (como uma lista, tupla ou string).")
    PerguntaDificuldade.objects.create(pergunta=p16, dificuldade=facil)
    Resposta.objects.create(pergunta=p16, texto="O laço while", correta=False)
    Resposta.objects.create(pergunta=p16, texto="O laço do-while", correta=False)
    Resposta.objects.create(pergunta=p16, texto="O laço for", correta=True)
    Resposta.objects.create(pergunta=p16, texto="A recursão", correta=False)

    p17 = Pergunta.objects.create(assunto=assunto_py_er, texto="Como você cria um laço que executa 5 vezes usando a função range()?", explicacao="A função `range(5)` gera uma sequência de números de 0 a 4 (cinco números no total), que é ideal para ser usada em um laço `for` para repetir uma ação 5 vezes.")
    PerguntaDificuldade.objects.create(pergunta=p17, dificuldade=facil)
    Resposta.objects.create(pergunta=p17, texto="for i in range(1, 5):", correta=False)
    Resposta.objects.create(pergunta=p17, texto="for i in range(5):", correta=True)
    Resposta.objects.create(pergunta=p17, texto="for i in range(0, 6):", correta=False)
    Resposta.objects.create(pergunta=p17, texto="for i in range(5-1):", correta=False)

    p18 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave é usada para parar completamente a execução de um laço?", explicacao="A instrução `break` interrompe a execução do laço mais interno (seja `for` ou `while`) e o programa continua na próxima linha após o laço.")
    PerguntaDificuldade.objects.create(pergunta=p18, dificuldade=facil)
    Resposta.objects.create(pergunta=p18, texto="stop", correta=False)
    Resposta.objects.create(pergunta=p18, texto="exit", correta=False)
    Resposta.objects.create(pergunta=p18, texto="break", correta=True)
    Resposta.objects.create(pergunta=p18, texto="return", correta=False)

    p19 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual palavra-chave pula para a próxima iteração de um laço sem terminar o laço por completo?", explicacao="A instrução `continue` interrompe a iteração atual e faz com que o laço pule imediatamente para o início da próxima iteração.")
    PerguntaDificuldade.objects.create(pergunta=p19, dificuldade=facil)
    Resposta.objects.create(pergunta=p19, texto="skip", correta=False)
    Resposta.objects.create(pergunta=p19, texto="next", correta=False)
    Resposta.objects.create(pergunta=p19, texto="pass", correta=False)
    Resposta.objects.create(pergunta=p19, texto="continue", correta=True)

    p20 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável contador for menor que 10?", explicacao="A sintaxe do `while` em Python começa com a palavra-chave `while`, seguida pela condição, e termina com dois pontos (`:`) para iniciar o bloco de código.")
    PerguntaDificuldade.objects.create(pergunta=p20, dificuldade=facil)
    Resposta.objects.create(pergunta=p20, texto="while (contador < 10)", correta=False)
    Resposta.objects.create(pergunta=p20, texto="while contador < 10:", correta=True)
    Resposta.objects.create(pergunta=p20, texto="while: contador < 10", correta=False)
    Resposta.objects.create(pergunta=p20, texto="loop while contador < 10:", correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p21 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que será impresso pelo código `for i in range(5): if i == 3: break; else: print('Fim do laço')`?", explicacao="A cláusula `else` de um laço `for` só é executada se o laço terminar naturalmente (sem ser interrompido por um `break`). Como o `break` é acionado quando `i` é 3, o laço é interrompido e a cláusula `else` é ignorada. Nada é impresso na tela.")
    PerguntaDificuldade.objects.create(pergunta=p21, dificuldade=medio)
    Resposta.objects.create(pergunta=p21, texto="Fim do laço", correta=False)
    Resposta.objects.create(pergunta=p21, texto="Nada será impresso.", correta=True)
    Resposta.objects.create(pergunta=p21, texto="0 1 2", correta=False)
    Resposta.objects.create(pergunta=p21, texto="O código resultará em um erro de sintaxe.", correta=False)

    p22 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual lista será gerada por: `[i*2 for i in range(5) if i % 2 != 0]`?", explicacao="Esta é uma list comprehension. Ela itera sobre os números de 0 a 4 (`range(5)`), a condição `if i % 2 != 0` filtra apenas os números ímpares (1 e 3), e a expressão `i*2` é aplicada a cada um desses números filtrados, resultando na lista `[2, 6]`.")
    PerguntaDificuldade.objects.create(pergunta=p22, dificuldade=medio)
    Resposta.objects.create(pergunta=p22, texto="[0, 2, 4, 6, 8]", correta=False)
    Resposta.objects.create(pergunta=p22, texto="[2, 6]", correta=True)
    Resposta.objects.create(pergunta=p22, texto="[1, 3]", correta=False)
    Resposta.objects.create(pergunta=p22, texto="[0, 1, 2, 3, 4]", correta=False)

    p23 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual a saída do código `count=0; for i in range(2): for j in range(3): if j==1: continue; count+=1; print(count)`?", explicacao="O laço externo roda 2 vezes (i=0, i=1). O laço interno roda 3 vezes para cada `i` (j=0, 1, 2). A instrução `continue` pula a iteração quando j==1. Portanto, `count` é incrementado quando (i=0, j=0), (i=0, j=2), (i=1, j=0) e (i=1, j=2). O total de incrementos é 4.")
    PerguntaDificuldade.objects.create(pergunta=p23, dificuldade=medio)
    Resposta.objects.create(pergunta=p23, texto="6", correta=False)
    Resposta.objects.create(pergunta=p23, texto="5", correta=False)
    Resposta.objects.create(pergunta=p23, texto="4", correta=True)
    Resposta.objects.create(pergunta=p23, texto="3", correta=False)

    p24 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que a função `enumerate` faz em um laço `for`?", explicacao="A função `enumerate` é usada para obter tanto o índice quanto o valor de um item em um iterável. Ela retorna um objeto `enumerate` que produz tuplas no formato (índice, valor), tornando o código mais limpo e legível do que manter um contador manual.")
    PerguntaDificuldade.objects.create(pergunta=p24, dificuldade=medio)
    Resposta.objects.create(pergunta=p24, texto="Enumera a quantidade de memória usada por cada item da lista.", correta=False)
    Resposta.objects.create(pergunta=p24, texto="Retorna uma tupla contendo um contador (índice) e o valor de cada item da sequência.", correta=True)
    Resposta.objects.create(pergunta=p24, texto="Verifica se os itens da lista são numéricos.", correta=False)
    Resposta.objects.create(pergunta=p24, texto="Executa o laço um número fixo de vezes, independentemente do tamanho da lista.", correta=False)

    p25 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que acontece no laço `letras=['a','b','c']; while letras: print(letras.pop(0))`?", explicacao="A condição `while letras:` verifica se a lista é 'verdadeira'. Uma lista é considerada verdadeira se não estiver vazia. A cada iteração, `letras.pop(0)` remove e retorna o primeiro elemento da lista, que é impresso. O laço continua até que a lista fique vazia, momento em que a condição se torna falsa e o laço termina.")
    PerguntaDificuldade.objects.create(pergunta=p25, dificuldade=medio)
    Resposta.objects.create(pergunta=p25, texto="Entra em um loop infinito.", correta=False)
    Resposta.objects.create(pergunta=p25, texto="Imprime 'a', 'b', e 'c', cada um em uma nova linha.", correta=True)
    Resposta.objects.create(pergunta=p25, texto="Imprime 'c', 'b', e 'a', cada um em uma nova linha.", correta=False)
    Resposta.objects.create(pergunta=p25, texto="Gera um IndexError.", correta=False)

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    p26 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual será o valor final da lista `resultado` após o código: `lista = [1, 2, 3]; resultado = [i for i in lista if i%2==0] or [0]`?", explicacao="A list comprehension `[i for i in lista if i%2==0]` resulta em `[2]`. A expressão utiliza o operador `or` de curto-circuito. Como a lista `[2]` não é vazia, ela é considerada 'verdadeira' em um contexto booleano e é retornada imediatamente. A segunda parte da expressão, `[0]`, nunca é avaliada.")
    PerguntaDificuldade.objects.create(pergunta=p26, dificuldade=dificil)
    Resposta.objects.create(pergunta=p26, texto="[0]", correta=False)
    Resposta.objects.create(pergunta=p26, texto="[2]", correta=True)
    Resposta.objects.create(pergunta=p26, texto="[1, 2, 3]", correta=False)
    Resposta.objects.create(pergunta=p26, texto="[2, 0]", correta=False)

    p27 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual é a saída do código: `x = 0; for i in range(3): x += i; else: x += 10; print(x)`?", explicacao="O laço `for` itera para i=0, i=1 e i=2. A variável `x` é incrementada, resultando em `x = 0 + 0 + 1 + 2`, que é 3. Como o laço termina sua execução normalmente (sem ser interrompido por um `break`), a cláusula `else` é executada, adicionando 10 a `x`. O valor final impresso é $3 + 10 = 13$.")
    PerguntaDificuldade.objects.create(pergunta=p27, dificuldade=dificil)
    Resposta.objects.create(pergunta=p27, texto="3", correta=False)
    Resposta.objects.create(pergunta=p27, texto="10", correta=False)
    Resposta.objects.create(pergunta=p27, texto="13", correta=True)
    Resposta.objects.create(pergunta=p27, texto="12", correta=False)

    p28 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual tipo de objeto o código `(x*2 for x in range(5))` cria?", explicacao="A sintaxe que usa parênteses em torno de uma expressão de compreensão, como `(expr for item in iteravel)`, cria um objeto gerador (generator). Geradores são iteradores que produzem os itens sob demanda (lazy evaluation), o que é eficiente em termos de memória.")
    PerguntaDificuldade.objects.create(pergunta=p28, dificuldade=dificil)
    Resposta.objects.create(pergunta=p28, texto="Uma tupla (tuple).", correta=False)
    Resposta.objects.create(pergunta=p28, texto="Um objeto gerador (generator object).", correta=True)
    Resposta.objects.create(pergunta=p28, texto="Uma lista (list).", correta=False)
    Resposta.objects.create(pergunta=p28, texto="Um conjunto (set).", correta=False)

    p29 = Pergunta.objects.create(assunto=assunto_py_er, texto="O que será impresso pelo código: `x = 0; while x < 2: x += 1; print(x); else: print('Fim')`?", explicacao="O laço `while` executa duas vezes. Na primeira, `x` se torna 1 e é impresso. Na segunda, `x` se torna 2 e é impresso. A condição `x < 2` então se torna falsa. Como o laço terminou sem um `break`, o bloco `else` associado a ele é executado, imprimindo 'Fim'.")
    PerguntaDificuldade.objects.create(pergunta=p29, dificuldade=dificil)
    Resposta.objects.create(pergunta=p29, texto="1\n2", correta=False)
    Resposta.objects.create(pergunta=p29, texto="1\n2\nFim", correta=True)
    Resposta.objects.create(pergunta=p29, texto="1\n2\n3\nFim", correta=False)
    Resposta.objects.create(pergunta=p29, texto="Loop infinito, pois x nunca é atualizado.", correta=False)

    p30 = Pergunta.objects.create(assunto=assunto_py_er, texto="Qual o resultado da utilização do `zip` e do desempacotamento no código: `a = [1, 2]; b = ['x', 'y']; for num, letra in zip(a, b): print(f'{num}{letra}', end=' ')`?", explicacao="A função `zip(a, b)` cria um iterador que agrega elementos das duas listas, produzindo as tuplas `(1, 'x')` e `(2, 'y')`. Em cada iteração do laço `for`, ocorre o desempacotamento da tupla (tuple unpacking) nas variáveis `num` e `letra`. A f-string formata e imprime o resultado, e `end=' '` garante que a saída seja na mesma linha, separada por um espaço.")
    PerguntaDificuldade.objects.create(pergunta=p30, dificuldade=dificil)
    Resposta.objects.create(pergunta=p30, texto="1, 2, x, y", correta=False)
    Resposta.objects.create(pergunta=p30, texto="1x 2y ", correta=True)
    Resposta.objects.create(pergunta=p30, texto="1x\n2y", correta=False)
    Resposta.objects.create(pergunta=p30, texto="Um TypeError, pois não se pode iterar sobre o resultado de zip.", correta=False)

    # ====================================================================
    # === QUIZ PYTHON: CONDICIONAIS ===
    # ====================================================================
    assunto_py_c_nome = 'Condicionais'
    assunto_py_c = Assunto.objects.create(linguagem=python, nome=assunto_py_c_nome, slug=slugify(f'{python.nome}-{assunto_py_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p31 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual palavra-chave é usada para a parte "senão se" em uma estrutura condicional em Python?', explicacao="Python utiliza a contração `elif` para 'else if', tornando o código mais conciso.")
    PerguntaDificuldade.objects.create(pergunta=p31, dificuldade=facil)
    Resposta.objects.create(pergunta=p31, texto="else if", correta=False)
    Resposta.objects.create(pergunta=p31, texto="elif", correta=True)
    Resposta.objects.create(pergunta=p31, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p31, texto="elsif", correta=False)

    p32 = Pergunta.objects.create(assunto=assunto_py_c, texto='Como se escreve a condição "se a não for igual a b" em Python?', explicacao="O operador de desigualdade em Python é `!=`. A expressão `a is not b` verifica se `a` e `b` são objetos diferentes na memória, o que é uma verificação mais estrita.")
    PerguntaDificuldade.objects.create(pergunta=p32, dificuldade=facil)
    Resposta.objects.create(pergunta=p32, texto="if a <> b:", correta=False)
    Resposta.objects.create(pergunta=p32, texto="if not(a == b):", correta=False)
    Resposta.objects.create(pergunta=p32, texto="if a != b:", correta=True)
    Resposta.objects.create(pergunta=p32, texto="if a is not b:", correta=False)

    p33 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é o operador lógico para "E" em Python?', explicacao="Python usa palavras em inglês (`and`, `or`, `not`) para operadores lógicos, em vez de símbolos como `&&` ou `||`.")
    PerguntaDificuldade.objects.create(pergunta=p33, dificuldade=facil)
    Resposta.objects.create(pergunta=p33, texto="&&", correta=False)
    Resposta.objects.create(pergunta=p33, texto="and", correta=True)
    Resposta.objects.create(pergunta=p33, texto="&", correta=False)
    Resposta.objects.create(pergunta=p33, texto="AND", correta=False)

    p34 = Pergunta.objects.create(assunto=assunto_py_c, texto="O que a seguinte expressão booleana retornaria: not (True and False)?", explicacao="A ordem de operação é: primeiro o que está dentro dos parênteses (`True and False` resulta em `False`), depois o `not` (`not False` resulta em `True`).")
    PerguntaDificuldade.objects.create(pergunta=p34, dificuldade=facil)
    Resposta.objects.create(pergunta=p34, texto="True", correta=True)
    Resposta.objects.create(pergunta=p34, texto="False", correta=False)
    Resposta.objects.create(pergunta=p34, texto="None", correta=False)
    Resposta.objects.create(pergunta=p34, texto="Error", correta=False)

    p35 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual é a sintaxe correta para um bloco if em Python que verifica se a variável nome é igual a "Ana"?', explicacao="A sintaxe de um `if` em Python exige o operador de comparação `==`, e o bloco de código é iniciado por dois pontos (`:`).")
    PerguntaDificuldade.objects.create(pergunta=p35, dificuldade=facil)
    Resposta.objects.create(pergunta=p35, texto='if (nome == "Ana")', correta=False)
    Resposta.objects.create(pergunta=p35, texto='if nome = "Ana":', correta=False)
    Resposta.objects.create(pergunta=p35, texto='if nome == "Ana":', correta=True)
    Resposta.objects.create(pergunta=p35, texto='if nome is "Ana" then', correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p36 = Pergunta.objects.create(assunto=assunto_py_c, texto='Qual será o valor de `resultado` após a execução do código: `x = 0; resultado = "A" if x else "B"`?', explicacao="Este é o operador ternário do Python. A condição avalia a 'veracidade' de `x`. Em Python, `0` é considerado `False`, portanto, o valor após o `else` é retornado.")
    PerguntaDificuldade.objects.create(pergunta=p36, dificuldade=medio)
    Resposta.objects.create(pergunta=p36, texto='"A"', correta=False)
    Resposta.objects.create(pergunta=p36, texto='"B"', correta=True)
    Resposta.objects.create(pergunta=p36, texto="True", correta=False)
    Resposta.objects.create(pergunta=p36, texto="O código resultará em um erro.", correta=False)

    p37 = Pergunta.objects.create(assunto=assunto_py_c, texto='O que a expressão `[] or 0 or "Olá"` retornará?', explicacao="O operador `or` retorna o primeiro valor 'truthy' (verdadeiro) que encontrar. Uma lista vazia (`[]`) e o número `0` são 'falsy'. A string não vazia `\"Olá\"` é 'truthy', então ela é retornada.")
    PerguntaDificuldade.objects.create(pergunta=p37, dificuldade=medio)
    Resposta.objects.create(pergunta=p37, texto="False", correta=False)
    Resposta.objects.create(pergunta=p37, texto="[]", correta=False)
    Resposta.objects.create(pergunta=p37, texto='"Olá"', correta=True)
    Resposta.objects.create(pergunta=p37, texto="True", correta=False)

    p38 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual o resultado da expressão `True or False and not True`?", explicacao="A precedência de operadores é `not`, depois `and`, depois `or`. A expressão é avaliada como `True or (False and (not True))` -> `True or (False and False)` -> `True or False`, que resulta em `True`.")
    PerguntaDificuldade.objects.create(pergunta=p38, dificuldade=medio)
    Resposta.objects.create(pergunta=p38, texto="True", correta=True)
    Resposta.objects.create(pergunta=p38, texto="False", correta=False)
    Resposta.objects.create(pergunta=p38, texto="None", correta=False)
    Resposta.objects.create(pergunta=p38, texto="SyntaxError", correta=False)

    p39 = Pergunta.objects.create(assunto=assunto_py_c, texto="Considere `a = [1]; b = [1]`. Qual o resultado de `a == b` e `a is b`, respectivamente?", explicacao="O operador `==` compara o VALOR dos objetos (ambas as listas contêm `[1]`, então é `True`). O operador `is` compara a IDENTIDADE (se são o mesmo objeto na memória, o que não são, então é `False`).")
    PerguntaDificuldade.objects.create(pergunta=p39, dificuldade=medio)
    Resposta.objects.create(pergunta=p39, texto="True, True", correta=False)
    Resposta.objects.create(pergunta=p39, texto="False, False", correta=False)
    Resposta.objects.create(pergunta=p39, texto="True, False", correta=True)
    Resposta.objects.create(pergunta=p39, texto="False, True", correta=False)

    p40 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual será o valor de `y` no código `x=5; if 3<x<4: y=1; elif 4<x<6: y=2; else: y=3`?", explicacao="Python permite comparações encadeadas. A expressão `4 < x < 6` é o mesmo que `4 < x and x < 6`. Como `x` é 5, essa condição é verdadeira, e `y` recebe o valor 2.")
    PerguntaDificuldade.objects.create(pergunta=p40, dificuldade=medio)
    Resposta.objects.create(pergunta=p40, texto="1", correta=False)
    Resposta.objects.create(pergunta=p40, texto="2", correta=True)
    Resposta.objects.create(pergunta=p40, texto="3", correta=False)
    Resposta.objects.create(pergunta=p40, texto="A variável `y` não será definida.", correta=False)

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---

    p41 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual será a saída do código a seguir? `a = 0; b = 5; result = (a and 'primeiro') or (b > 3 and 'segundo') or 'terceiro'; print(result)`", explicacao="O operador `or` retorna o primeiro valor verdadeiro que encontra. `(a and 'primeiro')` é avaliado como `0` (falso). A próxima condição, `(b > 3 and 'segundo')`, é `True and 'segundo'`, que resulta em `'segundo'`. Como `'segundo'` é um valor verdadeiro, o `or` para e o retorna, sem avaliar `'terceiro'`.")
    PerguntaDificuldade.objects.create(pergunta=p41, dificuldade=dificil)
    Resposta.objects.create(pergunta=p41, texto="'segundo'", correta=True)
    Resposta.objects.create(pergunta=p41, texto="'primeiro'", correta=False)
    Resposta.objects.create(pergunta=p41, texto="'terceiro'", correta=False)
    Resposta.objects.create(pergunta=p41, texto="True", correta=False)

    p42 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual valor será atribuído a `status` no código: `idade = 25; permissao = False; status = 'Aprovado' if idade > 18 and permissao else 'Reprovado por permissão' if idade > 18 else 'Reprovado por idade'`?", explicacao="A expressão é avaliada da esquerda para a direita. A primeira condição `idade > 18 and permissao` é `True and False`, resultando em `False`. O código então executa a parte após o `else`, que é outra expressão ternária: `'Reprovado por permissão' if idade > 18 else 'Reprovado por idade'`. Como `idade > 18` é verdadeiro, `status` recebe `'Reprovado por permissão'`.")
    PerguntaDificuldade.objects.create(pergunta=p42, dificuldade=dificil)
    Resposta.objects.create(pergunta=p42, texto="'Reprovado por permissão'", correta=True)
    Resposta.objects.create(pergunta=p42, texto="'Aprovado'", correta=False)
    Resposta.objects.create(pergunta=p42, texto="'Reprovado por idade'", correta=False)
    Resposta.objects.create(pergunta=p42, texto="Ocorrerá um erro de sintaxe.", correta=False)

    p43 = Pergunta.objects.create(assunto=assunto_py_c, texto="O que será impresso pelo código a seguir? `dados = []; if dados: print('Cheio'); elif not dados: print('Vazio'); else: print('Indefinido')`", explicacao="Em Python, estruturas de dados vazias (como listas, tuplas, dicionários) são consideradas 'falsas' em um contexto booleano. A condição `if dados:` avalia para `False`, pois a lista `dados` está vazia. A execução passa para o `elif not dados:`. Como `dados` é falso, `not dados` é verdadeiro, e o programa imprime 'Vazio'.")
    PerguntaDificuldade.objects.create(pergunta=p43, dificuldade=dificil)
    Resposta.objects.create(pergunta=p43, texto="'Vazio'", correta=True)
    Resposta.objects.create(pergunta=p43, texto="'Cheio'", correta=False)
    Resposta.objects.create(pergunta=p43, texto="'Indefinido'", correta=False)
    Resposta.objects.create(pergunta=p43, texto="Nada será impresso.", correta=False)

    p44 = Pergunta.objects.create(assunto=assunto_py_c, texto="Qual será a saída do código? `numeros = [1, 2, 3]; if (n := len(numeros)) > 2: print(f'Lista longa com {n} elementos'); else: print(f'Lista curta')` (Considerando Python 3.8+)", explicacao="O operador Walrus `:=` atribui o valor de `len(numeros)` (que é 3) à variável `n` e, em seguida, a expressão `n > 2` é avaliada. Como 3 é maior que 2, a condição é verdadeira. Portanto, a saída será a f-string formatada com o valor de `n`.")
    PerguntaDificuldade.objects.create(pergunta=p44, dificuldade=dificil)
    Resposta.objects.create(pergunta=p44, texto="'Lista longa com 3 elementos'", correta=True)
    Resposta.objects.create(pergunta=p44, texto="'Lista curta'", correta=False)
    Resposta.objects.create(pergunta=p44, texto="Ocorrerá um erro, pois `n` não foi definido antes.", correta=False)
    Resposta.objects.create(pergunta=p44, texto="True", correta=False)

    p45 = Pergunta.objects.create(assunto=assunto_py_c, texto="O que o código `a = 1000; b = 1000; if a is b: print(1); elif a == b: print(2); else: print(3)` imprimirá na tela?", explicacao="O operador `==` compara a igualdade dos valores, enquanto o `is` compara se duas variáveis apontam para o mesmo objeto na memória. Para otimização, Python pré-aloca inteiros pequenos (geralmente de -5 a 256). Números maiores como 1000 são criados como objetos separados. Portanto, `a is b` será falso, mas `a == b` será verdadeiro, imprimindo `2`.")
    PerguntaDificuldade.objects.create(pergunta=p45, dificuldade=dificil)
    Resposta.objects.create(pergunta=p45, texto="2", correta=True)
    Resposta.objects.create(pergunta=p45, texto="1", correta=False)
    Resposta.objects.create(pergunta=p45, texto="3", correta=False)
    Resposta.objects.create(pergunta=p45, texto="Ocorrerá um erro de comparação.", correta=False)

    # ====================================================================
    # === QUIZ C: SINTAXE BÁSICA ===
    # ====================================================================
    assunto_c_sb_nome = 'Sintaxe Básica'
    assunto_c_sb = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_sb_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_sb_nome}'))

# --- PERGUNTAS DE NÍVEL FÁCIL ---
    p46 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você declara uma variável inteira chamada quantidade com o valor 50 em C?", explicacao="Em C, uma linguagem de tipagem estática, você deve declarar o tipo da variável (`int`) antes de seu nome e, opcionalmente, inicializá-la.")
    PerguntaDificuldade.objects.create(pergunta=p46, dificuldade=facil)
    Resposta.objects.create(pergunta=p46, texto="quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p46, texto="int quantidade = 50;", correta=True)
    Resposta.objects.create(pergunta=p46, texto="integer quantidade = 50;", correta=False)
    Resposta.objects.create(pergunta=p46, texto="var quantidade = 50;", correta=False)

    p47 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual é o símbolo usado para indicar o fim de uma instrução em C?", explicacao="O ponto e vírgula (`;`) é um terminador de instrução fundamental em C, sinalizando ao compilador que um comando foi concluído.")
    PerguntaDificuldade.objects.create(pergunta=p47, dificuldade=facil)
    Resposta.objects.create(pergunta=p47, texto=". (ponto final)", correta=False)
    Resposta.objects.create(pergunta=p47, texto=": (dois pontos)", correta=False)
    Resposta.objects.create(pergunta=p47, texto="; (ponto e vírgula)", correta=True)
    Resposta.objects.create(pergunta=p47, texto="O final da linha", correta=False)

    p48 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual função da biblioteca stdio.h é usada para imprimir texto formatado no console?", explicacao="A função `printf()` (print formatted) faz parte da biblioteca de entrada/saída padrão (standard input/output) e é a principal forma de exibir texto no console.")
    PerguntaDificuldade.objects.create(pergunta=p48, dificuldade=facil)
    Resposta.objects.create(pergunta=p48, texto="print()", correta=False)
    Resposta.objects.create(pergunta=p48, texto="cout <<", correta=False)
    Resposta.objects.create(pergunta=p48, texto="printf()", correta=True)
    Resposta.objects.create(pergunta=p48, texto="log()", correta=False)

    p49 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Como você escreve um comentário de múltiplas linhas em C?", explicacao="Em C, um comentário de bloco começa com `/*` e termina com `*/`, e tudo que estiver entre esses delimitadores é ignorado pelo compilador.")
    PerguntaDificuldade.objects.create(pergunta=p49, dificuldade=facil)
    Resposta.objects.create(pergunta=p49, texto="// ... //", correta=False)
    Resposta.objects.create(pergunta=p49, texto="# ... #", correta=False)
    Resposta.objects.create(pergunta=p49, texto="/* ... */", correta=True)
    Resposta.objects.create(pergunta=p49, texto='""" ... """', correta=False)

    p50 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual diretiva de pré-processador é necessária para usar a função printf?", explicacao="A diretiva `#include <stdio.h>` instrui o pré-processador a incluir o conteúdo do arquivo de cabeçalho da biblioteca padrão de entrada/saída, onde `printf` é declarada.")
    PerguntaDificuldade.objects.create(pergunta=p50, dificuldade=facil)
    Resposta.objects.create(pergunta=p50, texto="#import <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p50, texto="#require <stdio.h>", correta=False)
    Resposta.objects.create(pergunta=p50, texto='#include "stdio.h"', correta=False)
    Resposta.objects.create(pergunta=p50, texto="#include <stdio.h>", correta=True)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p51 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o resultado da expressão `(float) 5 / 2` em C?", explicacao="O 'type cast' `(float)` converte o inteiro 5 para um float. Quando um dos operandos da divisão é float, a operação inteira é promovida para uma divisão de ponto flutuante, resultando em 2.5.")
    PerguntaDificuldade.objects.create(pergunta=p51, dificuldade=medio)
    Resposta.objects.create(pergunta=p51, texto="2", correta=False)
    Resposta.objects.create(pergunta=p51, texto="2.5", correta=True)
    Resposta.objects.create(pergunta=p51, texto="2.0", correta=False)
    Resposta.objects.create(pergunta=p51, texto="O código não compila.", correta=False)

    p52 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o valor final de `x` no código `int x = 5; int y = x++;`?", explicacao="O operador de pós-incremento (`x++`) primeiro retorna o valor original de `x` (5, que é atribuído a `y`) e DEPOIS incrementa `x`. Portanto, ao final, `y` vale 5 e `x` vale 6.")
    PerguntaDificuldade.objects.create(pergunta=p52, dificuldade=medio)
    Resposta.objects.create(pergunta=p52, texto="4", correta=False)
    Resposta.objects.create(pergunta=p52, texto="5", correta=False)
    Resposta.objects.create(pergunta=p52, texto="6", correta=True)
    Resposta.objects.create(pergunta=p52, texto="`y` não pode ser inicializado dessa forma.", correta=False)

    p53 = Pergunta.objects.create(assunto=assunto_c_sb, texto="O que a macro `#define QUADRADO(a) a * a` fará com a expressão `QUADRADO(2 + 3)`?", explicacao="O pré-processador faz uma substituição textual, expandindo a macro para `2 + 3 * 2 + 3`. Devido à precedência de operadores (multiplicação antes da adição), o cálculo é `2 + 6 + 3`, que resulta em 11.")
    PerguntaDificuldade.objects.create(pergunta=p53, dificuldade=medio)
    Resposta.objects.create(pergunta=p53, texto="A expressão resultará em 25.", correta=False)
    Resposta.objects.create(pergunta=p53, texto="A expressão resultará em 11.", correta=True)
    Resposta.objects.create(pergunta=p53, texto="A expressão resultará em 10.", correta=False)
    Resposta.objects.create(pergunta=p53, texto="O código não compilará devido à macro.", correta=False)

    p54 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Se `ptr` é um ponteiro para um inteiro, o que a expressão `*ptr` acessa?", explicacao="O operador `*` (asterisco), quando usado em um ponteiro, é o operador de dereferência. Ele acessa o VALOR que está armazenado no endereço de memória para o qual o ponteiro aponta.")
    PerguntaDificuldade.objects.create(pergunta=p54, dificuldade=medio)
    Resposta.objects.create(pergunta=p54, texto="O endereço de memória do ponteiro `ptr`.", correta=False)
    Resposta.objects.create(pergunta=p54, texto="O endereço de memória para o qual `ptr` aponta.", correta=False)
    Resposta.objects.create(pergunta=p54, texto="O valor armazenado no endereço de memória para o qual `ptr` aponta.", correta=True)
    Resposta.objects.create(pergunta=p54, texto="O tamanho do tipo de dado inteiro.", correta=False)

    p55 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual o valor da constante `TERCA` no `enum dia { DOMINGO, SEGUNDA, TERCA, QUARTA };`?", explicacao="Por padrão, os membros de uma enumeração (`enum`) em C recebem valores inteiros sequenciais começando em 0. Portanto, DOMINGO=0, SEGUNDA=1, e TERCA=2.")
    PerguntaDificuldade.objects.create(pergunta=p55, dificuldade=medio)
    Resposta.objects.create(pergunta=p55, texto="1", correta=False)
    Resposta.objects.create(pergunta=p55, texto="2", correta=True)
    Resposta.objects.create(pergunta=p55, texto="3", correta=False)
    Resposta.objects.create(pergunta=p55, texto="TERCA", correta=False)

    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    p56 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual será o resultado de `sizeof(char)` versus `sizeof(char*)` em um sistema de 64 bits?", explicacao="`sizeof(char)` é sempre 1 byte por definição. `sizeof(char*)` (o tamanho de um ponteiro) depende da arquitetura. Em sistemas de 64 bits, os endereços são representados por 8 bytes (64 bits).")
    PerguntaDificuldade.objects.create(pergunta=p56, dificuldade=dificil)
    Resposta.objects.create(pergunta=p56, texto="1 e 4 (bytes)", correta=False)
    Resposta.objects.create(pergunta=p56, texto="1 e 8 (bytes)", correta=True)
    Resposta.objects.create(pergunta=p56, texto="Ambos são 1 (byte)", correta=False)
    Resposta.objects.create(pergunta=p56, texto="1 e o valor é indefinido", correta=False)

    p57 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Considerando `int a = 1, b = 2;`, qual o resultado de `printf(\"%d\", a+++b);`?", explicacao="Devido à ambiguidade, o compilador C interpreta como `a++ + b`. O pós-incremento (a++) primeiro usa o valor de 'a' (1) na expressão e SÓ DEPOIS o incrementa. Então, $1 + 2 = 3$. Após a expressão, `a` se torna 2.")
    PerguntaDificuldade.objects.create(pergunta=p57, dificuldade=dificil)
    Resposta.objects.create(pergunta=p57, texto="3", correta=True)
    Resposta.objects.create(pergunta=p57, texto="4", correta=False)
    Resposta.objects.create(pergunta=p57, texto="Erro de sintaxe (Syntax Error)", correta=False)
    Resposta.objects.create(pergunta=p57, texto="Comportamento indefinido (Undefined Behavior)", correta=False)

    p58 = Pergunta.objects.create(assunto=assunto_c_sb, texto="O que a instrução `typedef int (*FuncPtr)(int, int);` faz?", explicacao="Esta instrução `typedef` cria um novo alias de tipo. `FuncPtr` torna-se um alias para um 'ponteiro para uma função que recebe dois inteiros como argumentos e retorna um inteiro'.")
    PerguntaDificuldade.objects.create(pergunta=p58, dificuldade=dificil)
    Resposta.objects.create(pergunta=p58, texto="Declara um ponteiro de função chamado `FuncPtr` que retorna um inteiro.", correta=False)
    Resposta.objects.create(pergunta=p58, texto="Cria um alias de tipo chamado `FuncPtr` para um ponteiro para função que retorna `int` e recebe dois `int`.", correta=True)
    Resposta.objects.create(pergunta=p58, texto="Declara uma função chamada `FuncPtr` que aceita dois ponteiros de inteiros.", correta=False)
    Resposta.objects.create(pergunta=p58, texto="Cria um novo tipo de struct para ponteiros.", correta=False)

    p59 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual é o modificador de tipo que indica ao compilador que uma variável não será alterada após a sua inicialização?", explicacao="O modificador `const` (de 'constant') é usado para declarar que o valor de uma variável (ou o valor apontado por um ponteiro) é fixo e não deve ser alterado pelo código, permitindo otimizações e checagem de erros pelo compilador.")
    PerguntaDificuldade.objects.create(pergunta=p59, dificuldade=dificil)
    Resposta.objects.create(pergunta=p59, texto="static", correta=False)
    Resposta.objects.create(pergunta=p59, texto="volatile", correta=False)
    Resposta.objects.create(pergunta=p59, texto="const", correta=True)
    Resposta.objects.create(pergunta=p59, texto="final", correta=False)

    p60 = Pergunta.objects.create(assunto=assunto_c_sb, texto="Qual será a saída do programa a seguir, que chama a mesma função três vezes? `void contador() { static int c = 0; c++; printf(\"%d \", c); } int main() { contador(); contador(); contador(); }`", explicacao="Uma variável local declarada com `static` é inicializada apenas uma vez, na primeira vez que a função é chamada. Ela retém seu valor entre as chamadas subsequentes. Portanto, `c` se torna 1, depois 2, e finalmente 3.")
    PerguntaDificuldade.objects.create(pergunta=p60, dificuldade=dificil)
    Resposta.objects.create(pergunta=p60, texto="1 1 1", correta=False)
    Resposta.objects.create(pergunta=p60, texto="0 1 2", correta=False)
    Resposta.objects.create(pergunta=p60, texto="1 2 3", correta=True)
    Resposta.objects.create(pergunta=p60, texto="Ocorrerá um erro de compilação.", correta=False)

    # ====================================================================
    # === QUIZ C: ESTRUTURAS DE REPETIÇÃO ===
    # ====================================================================
    assunto_c_er_nome = 'Estruturas de Repetição'
    assunto_c_er = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_er_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_er_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p61 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe completa de um laço for em C que vai de 0 a 9?", explicacao="O laço for em C tem três partes entre parênteses, separadas por ponto e vírgula: inicialização, condição e incremento/decremento.")
    PerguntaDificuldade.objects.create(pergunta=p61, dificuldade=facil)
    Resposta.objects.create(pergunta=p61, texto="for (int i=0; i < 10; i++)", correta=True)
    Resposta.objects.create(pergunta=p61, texto="for (i < 10; i++)", correta=False)
    Resposta.objects.create(pergunta=p61, texto="for (int i=0; i < 10)", correta=False)
    Resposta.objects.create(pergunta=p61, texto="for (int i=0 to 9)", correta=False)

    p62 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual laço em C garante que seu corpo seja executado pelo menos uma vez?", explicacao="O laço `do-while` é uma estrutura de pós-teste; o corpo do laço é executado primeiro e a condição é verificada depois, garantindo ao menos uma execução.")
    PerguntaDificuldade.objects.create(pergunta=p62, dificuldade=facil)
    Resposta.objects.create(pergunta=p62, texto="for", correta=False)
    Resposta.objects.create(pergunta=p62, texto="while", correta=False)
    Resposta.objects.create(pergunta=p62, texto="do-while", correta=True)
    Resposta.objects.create(pergunta=p62, texto="repeat-until", correta=False)

    p63 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a sintaxe para um laço while que continua enquanto a variável ativo for verdadeira (considerando 1 como verdadeiro)?", explicacao="A sintaxe do laço `while` em C requer que a condição esteja entre parênteses. `while (ativo)` é equivalente a `while (ativo != 0)`.")
    PerguntaDificuldade.objects.create(pergunta=p63, dificuldade=facil)
    Resposta.objects.create(pergunta=p63, texto="while [ativo == 1]", correta=False)
    Resposta.objects.create(pergunta=p63, texto="while (ativo)", correta=True)
    Resposta.objects.create(pergunta=p63, texto="while {ativo}", correta=False)
    Resposta.objects.create(pergunta=p63, texto="while ativo is 1", correta=False)

    p64 = Pergunta.objects.create(assunto=assunto_c_er, texto="Dentro de um laço for, o que a terceira expressão (i++) geralmente representa?", explicacao="A terceira parte da declaração de um laço `for` é a expressão de passo, executada ao final de cada iteração, tipicamente para incrementar ou decrementar a variável de controle.")
    PerguntaDificuldade.objects.create(pergunta=p64, dificuldade=facil)
    Resposta.objects.create(pergunta=p64, texto="A inicialização", correta=False)
    Resposta.objects.create(pergunta=p64, texto="A condição de parada", correta=False)
    Resposta.objects.create(pergunta=p64, texto="O incremento/decremento", correta=True)
    Resposta.objects.create(pergunta=p64, texto="A declaração da variável", correta=False)

    p65 = Pergunta.objects.create(assunto=assunto_c_er, texto="Como a palavra-chave break funciona dentro de um laço while em C?", explicacao="A instrução `break` em C causa a terminação imediata do laço mais interno em que se encontra, transferindo o controle do programa para a instrução seguinte ao laço.")
    PerguntaDificuldade.objects.create(pergunta=p65, dificuldade=facil)
    Resposta.objects.create(pergunta=p65, texto="Pula para a próxima iteração do laço.", correta=False)
    Resposta.objects.create(pergunta=p65, texto="Encerra a função atual.", correta=False)
    Resposta.objects.create(pergunta=p65, texto="Encerra o laço imediatamente.", correta=True)
    Resposta.objects.create(pergunta=p65, texto="Pausa a execução do laço temporariamente.", correta=False)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p66 = Pergunta.objects.create(assunto=assunto_c_er, texto="Quantas vezes a palavra \"Teste\" será impressa? `int i=5; do{ printf(\"Teste\\n\"); }while(i>10);`", explicacao="O laço `do-while` sempre executa seu corpo pelo menos uma vez, pois a condição só é verificada no final. 'Teste' é impresso, então `5 > 10` é avaliado como falso e o laço termina.")
    PerguntaDificuldade.objects.create(pergunta=p66, dificuldade=medio)
    Resposta.objects.create(pergunta=p66, texto="0 vezes", correta=False)
    Resposta.objects.create(pergunta=p66, texto="1 vez", correta=True)
    Resposta.objects.create(pergunta=p66, texto="5 vezes", correta=False)
    Resposta.objects.create(pergunta=p66, texto="Infinitas vezes", correta=False)

    p67 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual o valor final de `j`? `int i,j; for(i=0,j=10; i<5; i++,j--){ /*vazio*/ }`", explicacao="O laço executa 5 vezes (para i de 0 a 4). A cada iteração, `j` é decrementado. Inicia em 10, e após 5 decrementos (para i=0,1,2,3,4), seu valor final será 5.")
    PerguntaDificuldade.objects.create(pergunta=p67, dificuldade=medio)
    Resposta.objects.create(pergunta=p67, texto="10", correta=False)
    Resposta.objects.create(pergunta=p67, texto="0", correta=False)
    Resposta.objects.create(pergunta=p67, texto="5", correta=True)
    Resposta.objects.create(pergunta=p67, texto="4", correta=False)

    p68 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual é a forma idiomática em C para criar um laço infinito?", explicacao="Todas as opções são formas válidas e comuns de criar um laço infinito. `while(1)` usa uma condição que é sempre verdadeira. `for(;;)` omite todas as partes do `for`, resultando em um laço sem condição de parada.")
    PerguntaDificuldade.objects.create(pergunta=p68, dificuldade=medio)
    Resposta.objects.create(pergunta=p68, texto="while (1)", correta=False)
    Resposta.objects.create(pergunta=p68, texto="for (;;)", correta=False)
    Resposta.objects.create(pergunta=p68, texto="do {} while(true);", correta=False)
    Resposta.objects.create(pergunta=p68, texto="Todas as alternativas estão corretas.", correta=True)

    p69 = Pergunta.objects.create(assunto=assunto_c_er, texto="O que a instrução `break` faz dentro de laços aninhados?", explicacao="A instrução `break` sempre se aplica apenas ao escopo do laço mais próximo (o mais interno) em que está contida. Ela não afeta os laços externos.")
    PerguntaDificuldade.objects.create(pergunta=p69, dificuldade=medio)
    Resposta.objects.create(pergunta=p69, texto="Interrompe a execução de ambos os laços `for`.", correta=False)
    Resposta.objects.create(pergunta=p69, texto="Interrompe a execução apenas do laço `for` mais interno (o de `j`).", correta=True)
    Resposta.objects.create(pergunta=p69, texto="Interrompe a execução apenas do laço `for` mais externo (o de `i`).", correta=False)
    Resposta.objects.create(pergunta=p69, texto="Pula a iteração atual de ambos os laços.", correta=False)

    p70 = Pergunta.objects.create(assunto=assunto_c_er, texto="O que este código faz? `int arr[]={10,20,30}; int *ptr=arr; while(ptr<arr+3){ printf(\"%d \",*ptr); ptr++; }`", explicacao="Isso demonstra a iteração sobre um array usando aritmética de ponteiros. `ptr` começa no primeiro elemento, e a cada iteração, o valor (`*ptr`) é impresso e o ponteiro (`ptr++`) avança para o próximo elemento.")
    PerguntaDificuldade.objects.create(pergunta=p70, dificuldade=medio)
    Resposta.objects.create(pergunta=p70, texto="Imprime os endereços de memória dos elementos do array.", correta=False)
    Resposta.objects.create(pergunta=p70, texto="Entra em um loop infinito.", correta=False)
    Resposta.objects.create(pergunta=p70, texto="Imprime os valores `10 20 30 `.", correta=True)
    Resposta.objects.create(pergunta=p70, texto="Gera um erro de compilação.", correta=False)
    
    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    p71 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual será o valor final de `i` após a execução do laço: `int i = 0; for (; i++ < 5;) {}`?", explicacao="O pós-incremento `i++` é usado na condição. A expressão primeiro compara o valor *atual* de `i` com 5 e, *depois*, incrementa `i`. O laço para quando `i` é 5 (comparação `5 < 5` é Falsa), mas o incremento final ainda ocorre, tornando `i` igual a 6.")
    PerguntaDificuldade.objects.create(pergunta=p71, dificuldade=dificil)
    Resposta.objects.create(pergunta=p71, texto="4", correta=False)
    Resposta.objects.create(pergunta=p71, texto="5", correta=False)
    Resposta.objects.create(pergunta=p71, texto="6", correta=True)
    Resposta.objects.create(pergunta=p71, texto="O laço é infinito.", correta=False)

    p72 = Pergunta.objects.create(assunto=assunto_c_er, texto="O que o código a seguir imprimirá? `int i = 0; do { i++; if (i % 3 == 0) continue; printf(\"%d \", i); } while (i < 8);`", explicacao="O `i++` ocorre no início. Quando `i` é 3 ou 6, o `continue` pula o `printf`. O laço roda uma última vez quando `i` é 7, imprimindo '8' (pois `i++` o torna 8). A condição `8 < 8` falha, e o laço termina.")
    PerguntaDificuldade.objects.create(pergunta=p72, dificuldade=dificil)
    Resposta.objects.create(pergunta=p72, texto="1 2 4 5 7 8", correta=True)
    Resposta.objects.create(pergunta=p72, texto="1 2 4 5 7", correta=False)
    Resposta.objects.create(pergunta=p72, texto="1 2 3 4 5 6 7 8", correta=False)
    Resposta.objects.create(pergunta=p72, texto="1 2", correta=False)

    p73 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual será a saída do código? `for (int i = 0; i < 10; i++) { i++; printf(\"%d \", i); }`", explicacao="`i` é incrementado duas vezes por iteração: uma por `i++` no corpo e outra por `i++` na cláusula do `for`. (i=0 -> corpo i=1, print 1 -> cláusula i=2), (i=2 -> corpo i=3, print 3 -> cláusula i=4), ...")
    PerguntaDificuldade.objects.create(pergunta=p73, dificuldade=dificil)
    Resposta.objects.create(pergunta=p73, texto="0 1 2 3 4 5 6 7 8 9", correta=False)
    Resposta.objects.create(pergunta=p73, texto="1 2 3 4 5 6 7 8 9 10", correta=False)
    Resposta.objects.create(pergunta=p73, texto="1 3 5 7 9", correta=True)
    Resposta.objects.create(pergunta=p73, texto="0 2 4 6 8", correta=False)

    p74 = Pergunta.objects.create(assunto=assunto_c_er, texto="Qual será o valor de `a` e `b` após o laço `while`? `int a = 0, b = 5; while (a++, --b) {}`", explicacao="O operador vírgula (`,`) avalia `a++`, descarta o resultado, e então avalia e retorna `--b` para a condição. O laço roda enquanto `--b` for diferente de 0. O laço executa 5 vezes (b=4, 3, 2, 1, 0). Nesses 5 vezes, `a` é incrementado de 0 para 5.")
    PerguntaDificuldade.objects.create(pergunta=p74, dificuldade=dificil)
    Resposta.objects.create(pergunta=p74, texto="a=5, b=0", correta=True)
    Resposta.objects.create(pergunta=p74, texto="a=6, b=0", correta=False)
    Resposta.objects.create(pergunta=p74, texto="a=5, b=-1", correta=False)
    Resposta.objects.create(pergunta=p74, texto="a=4, b=0", correta=False)

    p75 = Pergunta.objects.create(assunto=assunto_c_er, texto="Para que serve a instrução `goto` em C, no contexto de laços?", explicacao="Embora `break` saia do laço mais interno, `goto` permite um salto incondicional para um 'label' (marcador) definido. Isso pode ser usado para sair de múltiplos laços aninhados de uma só vez, pulando diretamente para um ponto após o laço mais externo.")
    PerguntaDificuldade.objects.create(pergunta=p75, dificuldade=dificil)
    Resposta.objects.create(pergunta=p75, texto="É a única forma de implementar um laço `do-while`.", correta=False)
    Resposta.objects.create(pergunta=p75, texto="Para pular para uma iteração específica, como `goto 5;`.", correta=False)
    Resposta.objects.create(pergunta=p75, texto="Para sair de múltiplos laços aninhados de uma só vez, pulando para um *label* externo.", correta=True)
    Resposta.objects.create(pergunta=p75, texto="É um sinônimo da instrução `continue` para pular uma iteração.", correta=False)
    
    # ====================================================================
    # === QUIZ C: ESTRUTURAS CONDICIONAIS === 
    # ====================================================================
    assunto_c_c_nome = 'Estruturas Condicionais'
    assunto_c_c = Assunto.objects.create(linguagem=c_lang, nome=assunto_c_c_nome, slug=slugify(f'{c_lang.nome}-{assunto_c_c_nome}'))

    # --- PERGUNTAS DE NÍVEL FÁCIL ---
    p76 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é a sintaxe para a parte "senão se" em uma estrutura condicional em C?', explicacao="Em C, a estrutura para testar múltiplas condições sequencialmente é `if`, seguida por uma ou mais cláusulas `else if`, e opcionalmente um `else` no final.")
    PerguntaDificuldade.objects.create(pergunta=p76, dificuldade=facil)
    Resposta.objects.create(pergunta=p76, texto="elif", correta=False)
    Resposta.objects.create(pergunta=p76, texto="else if", correta=True)
    Resposta.objects.create(pergunta=p76, texto="elseif", correta=False)
    Resposta.objects.create(pergunta=p76, texto="elsif", correta=False)

    p77 = Pergunta.objects.create(assunto=assunto_c_c, texto='Como se escreve a condição "se x é maior ou igual a y" em C?', explicacao="O operador relacional para 'maior ou igual a' em C é `>=`. A condição deve estar entre parênteses na declaração `if`.")
    PerguntaDificuldade.objects.create(pergunta=p77, dificuldade=facil)
    Resposta.objects.create(pergunta=p77, texto="if (x >= y)", correta=True)
    Resposta.objects.create(pergunta=p77, texto="if x >= y then", correta=False)
    Resposta.objects.create(pergunta=p77, texto="if [x >= y]", correta=False)
    Resposta.objects.create(pergunta=p77, texto="if (x >|= y)", correta=False)

    p78 = Pergunta.objects.create(assunto=assunto_c_c, texto='Qual é o operador lógico para "OU" em C?', explicacao="O operador lógico 'OU' em C é representado por duas barras verticais (`||`). O operador `|` é o 'OU' bit-a-bit (bitwise).")
    PerguntaDificuldade.objects.create(pergunta=p78, dificuldade=facil)
    Resposta.objects.create(pergunta=p78, texto="or", correta=False)
    Resposta.objects.create(pergunta=p78, texto="||", correta=True)
    Resposta.objects.create(pergunta=p78, texto="|", correta=False)
    Resposta.objects.create(pergunta=p78, texto="OR", correta=False)

    p79 = Pergunta.objects.create(assunto=assunto_c_c, texto="Além de if-else, qual outra estrutura de seleção permite testar uma variável contra uma lista de valores?", explicacao="A estrutura `switch` permite que uma variável seja testada contra uma lista de valores (os `case`), oferecendo uma alternativa mais limpa a múltiplos `else if`.")
    PerguntaDificuldade.objects.create(pergunta=p79, dificuldade=facil)
    Resposta.objects.create(pergunta=p79, texto="select", correta=False)
    Resposta.objects.create(pergunta=p79, texto="case", correta=False)
    Resposta.objects.create(pergunta=p79, texto="match", correta=False)
    Resposta.objects.create(pergunta=p79, texto="switch", correta=True)

    p80 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual operador é usado para comparação de igualdade em C?", explicacao="Em C, o sinal de igual único (`=`) é para atribuição de valor. Para comparar se dois valores são iguais, deve-se usar o sinal de igual duplo (`==`).")
    PerguntaDificuldade.objects.create(pergunta=p80, dificuldade=facil)
    Resposta.objects.create(pergunta=p80, texto="=", correta=False)
    Resposta.objects.create(pergunta=p80, texto=":=", correta=False)
    Resposta.objects.create(pergunta=p80, texto="eq", correta=False)
    Resposta.objects.create(pergunta=p80, texto="==", correta=True)

    # --- PERGUNTAS DE NÍVEL MÉDIO ---
    p81 = Pergunta.objects.create(assunto=assunto_c_c, texto="O que será impresso pelo código `int x=0; if(x=5){ printf(\"Verdadeiro\"); } else { printf(\"Falso\"); }`?", explicacao="O erro comum `x=5` é uma ATRIBUIÇÃO, não uma comparação. O valor da expressão de atribuição é 5. Em C, qualquer valor diferente de zero é `true`, então o bloco `if` é executado.")
    PerguntaDificuldade.objects.create(pergunta=p81, dificuldade=medio)
    Resposta.objects.create(pergunta=p81, texto="Falso", correta=False)
    Resposta.objects.create(pergunta=p81, texto="Verdadeiro", correta=True)
    Resposta.objects.create(pergunta=p81, texto="Nada será impresso.", correta=False)
    Resposta.objects.create(pergunta=p81, texto="O código não compilará devido a `x = 5`.", correta=False)

    p82 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual será a saída do switch: `int op=2; switch(op){ case 1:printf(\"A\"); case 2:printf(\"B\"); case 3:printf(\"C\");break; default:printf(\"D\"); }`?", explicacao="O `switch` executa o `case 2`, imprimindo 'B'. Como não há `break` no `case 2`, a execução 'cai' (fall-through) para o `case 3`, imprimindo 'C'. Então, encontra o `break` e sai.")
    PerguntaDificuldade.objects.create(pergunta=p82, dificuldade=medio)
    Resposta.objects.create(pergunta=p82, texto="B", correta=False)
    Resposta.objects.create(pergunta=p82, texto="C", correta=False)
    Resposta.objects.create(pergunta=p82, texto="BC", correta=True)
    Resposta.objects.create(pergunta=p82, texto="BCD", correta=False)

    p83 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor de `x` após: `int x = 10; if (x > 5 || ++x == 10) { /*...*/ }`?", explicacao="O operador OU (`||`) usa 'avaliação de curto-circuito'. Como a primeira parte (`x > 5`) é verdadeira, a segunda parte (`++x == 10`) nunca é avaliada. Portanto, `x` não é incrementado e permanece 10.")
    PerguntaDificuldade.objects.create(pergunta=p83, dificuldade=medio)
    Resposta.objects.create(pergunta=p83, texto="10", correta=True)
    Resposta.objects.create(pergunta=p83, texto="11", correta=False)
    Resposta.objects.create(pergunta=p83, texto="9", correta=False)
    Resposta.objects.create(pergunta=p83, texto="O comportamento é indefinido.", correta=False)

    p84 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor final de `maior` em: `int a=15, b=20; int maior = (a > b) ? a : b;`?", explicacao="Este é o operador ternário. A condição `(a > b)` é `(15 > 20)`, que é falsa. Portanto, a expressão retorna o valor após os dois pontos (`:`), que é `b` (ou seja, 20).")
    PerguntaDificuldade.objects.create(pergunta=p84, dificuldade=medio)
    Resposta.objects.create(pergunta=p84, texto="15", correta=False)
    Resposta.objects.create(pergunta=p84, texto="20", correta=True)
    Resposta.objects.create(pergunta=p84, texto="0", correta=False)
    Resposta.objects.create(pergunta=p84, texto="O código tem um erro de sintaxe.", correta=False)

    p85 = Pergunta.objects.create(assunto=assunto_c_c, texto="O que a condição `if (num & 1)` verifica?", explicacao="`&` é o operador E bit-a-bit. `num & 1` resulta em `1` apenas se o último bit de `num` for 1 (característica de todos os números ímpares). Se for par (último bit 0), o resultado é 0 (falso).")
    PerguntaDificuldade.objects.create(pergunta=p85, dificuldade=medio)
    Resposta.objects.create(pergunta=p85, texto="Se `num` é igual a 1.", correta=False)
    Resposta.objects.create(pergunta=p85, texto="Se `num` é um número par.", correta=False)
    Resposta.objects.create(pergunta=p85, texto="Se `num` é um número ímpar.", correta=True)
    Resposta.objects.create(pergunta=p85, texto="Se `num` é maior que 1.", correta=False)
    
    # --- PERGUNTAS DE NÍVEL DIFÍCIL ---
    p86 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o resultado da expressão: (5 < 3 && 2 < 0) || (9 & 1)?", explicacao="A primeira parte (5 < 3 && 2 < 0) é Falsa. A segunda parte (9 & 1) é uma operação E bit-a-bit (bitwise AND). 9 (1001) & 1 (0001) resulta em 1 (Verdadeiro). A expressão final é 0 || 1, que resulta em 1 (Verdadeiro).")
    PerguntaDificuldade.objects.create(pergunta=p86, dificuldade=dificil)
    Resposta.objects.create(pergunta=p86, texto="0", correta=False)
    Resposta.objects.create(pergunta=p86, texto="1", correta=True)
    Resposta.objects.create(pergunta=p86, texto="9", correta=False)
    Resposta.objects.create(pergunta=p86, texto="8", correta=False)

    p87 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor de x e y após o if? int x = 5, y = 10; if (x == 4 && ++y > 10) {}", explicacao="O operador && (E Lógico) usa 'curto-circuito'. A primeira condição (x == 4) é Falsa. Como Falso && qualquer_coisa é sempre Falso, a segunda parte (++y > 10) nunca é executada. y não é incrementado.")
    PerguntaDificuldade.objects.create(pergunta=p87, dificuldade=dificil)
    Resposta.objects.create(pergunta=p87, texto="x=5, y=10", correta=True)
    Resposta.objects.create(pergunta=p87, texto="x=5, y=11", correta=False)
    Resposta.objects.create(pergunta=p87, texto="x=4, y=11", correta=False)
    Resposta.objects.create(pergunta=p87, texto="x=4, y=10", correta=False)

    p88 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual será a saída? int v=1; switch(v) { case 1: v+=2; case 2: v*=2; case 3: v-=1; } printf(\"%d\", v);", explicacao="O switch entra no case 1. v se torna 3. Sem break, ele 'cai' (fall-through) para o case 2. v se torna 6 (32). Sem break, 'cai' para o case 3. v se torna 5 (6-1). O switch termina e 5 é impresso.")
    PerguntaDificuldade.objects.create(pergunta=p88, dificuldade=dificil)
    Resposta.objects.create(pergunta=p88, texto="3", correta=False)
    Resposta.objects.create(pergunta=p88, texto="5", correta=True)
    Resposta.objects.create(pergunta=p88, texto="6", correta=False)
    Resposta.objects.create(pergunta=p88, texto="2", correta=False)

    p89 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual o valor de a e b após esta operação? int a=10, b=20; int res = (a > b) ? a++ : b++;", explicacao="O operador ternário avalia (10 > 20), que é Falso. Apenas a expressão após os dois-pontos (b++) é executada. res recebe o valor de bantes* do incremento (20). b é então incrementado para 21. a permanece 10.")
    PerguntaDificuldade.objects.create(pergunta=p89, dificuldade=dificil)
    Resposta.objects.create(pergunta=p89, texto="a=11, b=20", correta=False)
    Resposta.objects.create(pergunta=p89, texto="a=10, b=21", correta=True)
    Resposta.objects.create(pergunta=p89, texto="a=11, b=21", correta=False)
    Resposta.objects.create(pergunta=p89, texto="a=10, b=20", correta=False)

    p90 = Pergunta.objects.create(assunto=assunto_c_c, texto="Qual será a saída do código? int x=1; if(x>0){printf(\"A\");} if(x==1){printf(\"B\");} else if(x<2){printf(\"C\");}", explicacao="Existem dois blocos if independentes. O primeiro if (x > 0) é Verdadeiro, imprimindo 'A'. O segundo bloco if-else if é avaliado. if (x == 1) é Verdadeiro, imprimindo 'B'. A cláusula else if deste segundo bloco é ignorada, pois o if foi satisfeito.")
    PerguntaDificuldade.objects.create(pergunta=p90, dificuldade=dificil)
    Resposta.objects.create(pergunta=p90, texto="A", correta=False)
    Resposta.objects.create(pergunta=p90, texto="B", correta=False)
    Resposta.objects.create(pergunta=p90, texto="AC", correta=False)
    Resposta.objects.create(pergunta=p90, texto="AB", correta=True)
class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(popular_dados),
    ]

