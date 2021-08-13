'''
count - Itertools
    I.      Para utilizar count é necessário importar da biblioteca itertools o modulo count. count()
            é um contador que esta pronto na linguagem python
    II.     A função count() gera um iterador que é um gerador, podendo se utilizar a função next,
    III.    O contador gerado por count não possui fim
    IV.     É possivel indicar um valor inicial para count com o atributo start
    V.      É possivel indicar na função count o incremento dos valores com o atributo step
        V.I.    É possivel utilizar numeros de ponto flutuante, o python acusará que esta função recebe
                apenas valores inteiros, entretanto funciona. Em virtude da precisão de armazenamento de
                numeros decimais do python é necessário utilizar a função round(x,y) para arredondar os
                valores onde x é o valor a ser arredondado e y é o numero de casas decimais
    VI.     É possivel efetuar contagem decrescente utilizando um step com valor negativo
    VII.    Contadores são muito utilizados em programação, uma de suas funcionalidades é na indexação de
            listas
    VIII.   Um unico cuidado deve se ter a utilizar este contador é entrar em um loop infinito com este
            contador pois ele não possui final
'''
# I
from itertools import count

print('\n# II',)
contador = count()
print('\n# III')
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

print('\n# IV')
contador = count(start=32)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

print('\n# V')
contador = count(start=1, step=2)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

print('\n# V.I')
contador = count(start=1, step=0.1)
for valor in contador:
    print(round(valor,2))
    if valor >= 100:
        break

print('\n# VI')
contador = count(start=100, step=-2)
for valor in contador:
    if valor < 0:
        break
    print(valor)

print('\n# VII')
lista_nomes = ['Alipio', 'Janete', 'Tarcísio', 'Bryan']
contador = count(start=1)
lista_indexada = list(zip(contador,lista_nomes))
print(lista_indexada)
