'''
Desempacotamento de listas
    - Formas de desempacotamento
'''
lista = ['Luiz', 'Tarcísio', 'Bryan']

# metodo 1: numero de elementos da lista igual ao numero de parametros que recebe a lista
#   - se o numero de variaveis recebendo a lista for menor que o número de itens da lista então
# ocorrerá erro de compilação
n1, n2, n3 = lista
print(n1, n2, n3)
# para pegar apenas alguns valores iniciais utilizar o numero de variaveis igual ao numero de itens e com os
# valores valores e aquelas que não se desejam armazenalos em outro

b = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

n1, n2, n3, *outra  = b
print(n1, n2, n3, outra)

# se o restante não for de interesse, utilizar *_
n1, n2, *_ = b
