'''
Enumerate e listas
'''
#listas pode ter mais de uma dimensão, ou seja, lista que em seus indices possuem outras listas.
#para acessar basta utilizar outro colchetes com o indice da ser acessado na proxima lista
# ex: lista[x][y]
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]
print(lista[2][1])

# todo enumerate gera um objeto ao qual pode ser iterado sobre ele
enumeracao = enumerate(lista)  # indica o nome do objeto e a posição da memória
print(enumeracao)

# é possivel efetuar conversão "typecast"
# typecast de enumerate para lista
mudando = list(enumeracao)
print(mudando)
#type cast de enumerate para lista gera uma lista com várias tuplas. Tuplas é um tipo de lista que
# não pode ser modificado

# no caso da enumeração que se tornou uma lista existe tuplas dentro dela e cada tupla possui um
# indice seguido do correspondente da lista que se tornou enumeração

# tuplas podem ser acessadas como listas com colchetes
print(mudando[2][1][0])

#enumerate não gera indices, ele enumera uma lista

# é possivel informar o valor ao qual o enumerate ira iniciar
for x1, x2 in enumerate(lista, 18):
    print(x1, x2)

# utilizando enumerate em for com apenas um valor de recebimento 'x' ele ira retornar tuplas
for x in enumerate(lista):
    print(x)

# podendo ser feito também - desempacotamento
for x in enumerate(lista):
    a, b = x
    print(a, b)

#podendo fazer o mesmo processo para a lista gerada - desempacotamento
for x in enumerate(lista):
    num, listaa = x
    nome1, nome2, nome3 = listaa
    print(f'{num}: nome1: {nome1}, nome2: {nome2}, nome3: {nome3}')

