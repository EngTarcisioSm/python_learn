'''
List Comprehension em Python
    - Em português "compreensão de listas"
    - São utilizadas para duas coisas em python:
        - Otimização em termos de performace em código;
        - Escrita de menos linhas de código
    - Pode-se utilizar qualquer tipo de dados dentro da lista, inclusive dados de tipos diferentes

    - I.    Pode-se iterar sobre uma lista em uma unica linha de código
    - II.   o resultado, variavel resultante da list comprehension
    - III.  É possivel ter mais de um laço for dentro de um list comprehension
            No exemplo para cada 1 iteração de um for o segundo for é executado totalmente
    - IV.   É possivel iterar como anteriormente mensionado sobre strings
    - V.    É possivel iterar sobre tuplas com list comprehension
    - VI.   É possivel filtrar listas
'''

print("#I")
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
print(l2)

print("\n#II")
l3 = [variavel * 2 for variavel in l1]
print(l3)

print("\n#III")
l4 = [(v1,v2) for v1 in l1 for v2 in range(3)]
print(l4)

print("\n#IV")
l5 = ['Luiz', 'Tarcisio', 'Bryan', 'Alipio', 'Janete']
l6 = [v.replace('a','@').upper() for v in l5]
print(l6)

print("\n#V")
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
l7 = [(y,x) for x, y in tupla]
print(l7)

print("\n#V")
l8 = list(range(100))
print(l8)
# pegando todos os elementos da lista l8 que são divisiveis por 2
l9 = [v for v in l8 if v % 2 == 0]
print(l9)
# pegando todos os elementos da lista l8 que são divisiveis por 3 e por 8
l10 = [v for v in l8 if v % 3 == 0 if v % 8 == 0]
print(l10)
# utilizando else
l11 = [v if v % 3 == 0 else -1 for v in l8]
print(l11)
# utilizando if com 2 condições
l12 = [v if v % 3 == 0 and v % 8 else -1 for v in l8]
print(l12)