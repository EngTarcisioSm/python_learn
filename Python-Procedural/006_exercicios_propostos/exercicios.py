'''
1 - Crie uma funcao1 que receba uma funcao2 como parâmetro e retorno o valor da função2 executada

2 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função do executada. Faça
a função1 executar duas funções que recebam um numero diferente de argumentos.
'''
# 1
def func1(function):
    return function()

def func2():
    return 'Hello World'

print(func1(func2))


# 2
def func3(funcao1, funcao2, *args):
    funcao1(args[0])
    funcao2(args[1], args[2], args[3])

def func4(nome):
    print(f'Olá {nome}')
def func5(cidade, mes, dia):
    print(f'{cidade}, {dia} de {mes}')

func3(func4, func5, 'Tarcísio', 'São Paulo', 'Junho', 14)


# 2 resolvido
# uma função que consegue executar varias outras
def func6(function, **kwargs):
    function(**kwargs)

def func7(nome, saudacao):
    print(f'{nome}, {saudacao}')


func6(func7, nome='Tarcisio', saudacao='Bom dia')
func6(func5, cidade='São Paulo', mes='Junho', dia=14)
