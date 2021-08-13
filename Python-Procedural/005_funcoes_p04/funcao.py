'''
- Funções parte 04 (Escopo de variáveis)
    - I.    Existe escopo global

    - II.   Variaveis de escopo global ficam disponiveis dentro de funções

    - III.  Quando uma variavel de escopo global tem seu valor alterado dentro de uma função, é criado
    uma nova variavel de mesmo nome dentro da função entretanto seu valor não é alterado fora da função

    - IV.   O escopo global sempre terá maior precedencia que o escopo local

    - V.    Alterar o valor de uma variavel global dentro de uma função, não é uma boa prática pois pode
    apresentar comportamentos estranhos dentro do código

    - VI.   Para alterar uma variável global dentro de uma função (não é uma boa prática e não se reco-
    menda) utiliza-se a palavra reservada global antes da variavel

    - VII.  Caso se deseja utilizar variveis utilize parametros e retornos para se trabalhar com variaveis
    não recomendando processo de alterar variaveis globais dentro de funções

    - VIII. Quando dentro de uma função se cria uma nova variavel de mesmo nome de uma variavel de escopo
    global, independente da posição em que esta foi criada dentro da função, a variavel global deixa de
    ser acessivel totalmente dentro da função, caso tente efetuar este processo acarretará em uma excessão
    - IX.   A variavel criada dentro do escopo local de uma função não fica disponivel para outras funções
    apenas dentro de sí

    - X.    Quanto menos se utilizar um escopo global melhor é
'''

# I, II, III e IV
variavel = 'valor'

def func1():
    print(variavel)
def func2():
    variavel = 'outro valor'
    print(variavel)
def func3():
    variavel = 'outro valor ainda'
    func1()
func1()
func2()
func1()
func3()

# V e VI
def func4():
    global variavel
    variavel = 'valor_alterado_não_recomendavel'

func1()
func4()
func1()

# VII
def func5(arg=None):
    arg = arg.replace('v', 'c')
    return arg

print(func5(variavel))

# VIII - acarreta erro
'''
def func():
    print(variavel)
    variavel = 1234
'''

# IX
def func6():
    mais_valor = 'hi'
'''
acarreta erro ao ser executado 
def func7():
    print(mais_valor)
'''