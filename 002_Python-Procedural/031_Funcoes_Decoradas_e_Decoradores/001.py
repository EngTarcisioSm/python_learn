'''
    - I.        Funções decoradoras envolvem uma outra função alterando ou não o comportamento daquela que
                esta envolvida

    - II.       É possivel que uma variavel armazene uma função fazendo com que o tipo da variavel mude e seja
                possivel executar a função a partir da variavel

    - III.      É possivel que uma função tenha uma outra função definida dentro de sí podendo ser executada
                ou mesmo uma função retornando uma outra função

    - IV.       Funções podem receber como parametro outras funções

    -V.         Decorar uma função utiliza @Nome_funcao_decoradora, podendo adicionar funcionalidades a função
                decorada

    - VI.       FUnção decorada adicionando funcionalidades

'''
from time import time
from time import sleep


print('#II')
def fala_oi():
    print('Oi')

variavel = fala_oi

print(variavel)
print(type(variavel))

print('#III')
def master():
    def slave():
        print('Oi...')
    slave()

master()

def master2():
    def slave2():
        print('Tchau')
    return slave2

variavel2 = master2()
print(type(variavel2))
variavel2()

print('#IV')
def master3(funcao):
    funcao()

def falei():
    print('IAAAAAAAAAAAAAIII...')

master3(falei)

print('#V')
def master3(funcao):
    print('Extra...')
    funcao()

@master3
def func():
    print('Diga X...')

#func()

print('VI')
def velocidade(funcao):
    def interna(*args, **kwargs): # permite a função que entrar possuir parametros
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A funcao {funcao.__name__} levou {tempo:.2f}ms para executar')
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()