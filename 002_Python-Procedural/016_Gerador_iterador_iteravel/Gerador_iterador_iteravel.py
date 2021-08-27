'''
=> Iteraveis, Iteradores e Geradores

    1.  - O metodo hasattr(obj, '__iter__') returna se o objeto possui o método iter que informa se um objeto
        é iteravel, retornando booleano (true ou false)
    2.  - O metodo hasattr(obj, '__next__')  retorna de o objeto possui o método next que informa se um objeto
        é iterador, retornando booleando
    3.  - O laço for transforma listas em iteradores, o que o for faz para a lista se tornar um iterador é
        utilizar o  metodo __iter__
    4.  - É possivel utilizar o metodo __iter__ diretamente e transformar uma lista em um iterador
    5.  - Iteraveis são valores que são possiveis iterar sobre eles mais não necessariamente são iteradores
    6.  - Iterador ao utilizar a função next(obj) sempre retornará o proximo item, retornando apenas um unico
        item
    7.  - Geradores são utilizados vai se gerar muitos dados com um tamanho muito grande que utilizam uma
        grande quantidade de memória.
        1.  - Nestes casos todos os valores podem e na maioria das vezes não são necessários todos ao mesmo
            tempo. Neste caso se utiliza geradores que somente é gerado o proximo valor quando o mesmo for
            necessário
    8.  - A palavra yield é utilizada para se criar geradores
    9.  - Uma segunda forma de se utilizar geradores é utilizar list comprehension entre parentesis
    10. - O tamanho que um gerador e uma lista ocupam em memoria é completamente diferente

'''
import sys
import time

print("#1")
lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))
numero = 123
print(hasattr(numero, '__iter__'))
nome = 'Tarcísio'
print(hasattr(nome, '__iter__'))

print("\n#2")
print(hasattr(lista, '__next__'))

print("\n#3")
lista2 = [1, 2, 3, 4, 5]
lista2 = iter(lista2)
print(hasattr(lista2, '__next__'))

print('\n#4')
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))

print("\n#8")
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

lista3 = gera()
print(lista3)
for x in lista3:
    print(x)

def gera2():
    variavel = 'Valor1'
    yield variavel
    variavel = 'Valor2'
    yield variavel
    variavel = 'Valor3'
    yield variavel
    variavel = 'Valor4'
    yield variavel
    variavel = 'Valor5'
    yield variavel

list4 = gera2()
print(next(list4))
print(next(list4))
print(next(list4))
print(next(list4))
print(next(list4))
# utilizar mais um gerador acarretará em erro uma vez que não há um sexto valor

print("\n#9")
lista5 = (x for x in range(100))
print(lista5)
for a in lista5:
    print(a)
print(type(lista5))

print("\n#10")
lista6 = [x for x in range(100)]
lista7 = (x for x in range(100))
print("tamanho lista normal: ", sys.getsizeof(lista6))
print("tamanho lista gerador: ", sys.getsizeof(lista7))
