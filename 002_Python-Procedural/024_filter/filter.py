'''
    - FILTER
        I.      A função filter como o proprio nome já diz serve para filtrar coisas
        II.     Possui dois atributos, o primeiro que é uma função que deve obrigatóriamente retornar um
                valor booleano para o teste (podendo ser uma função lambda) e o segundo atributo é uma
                lista
        III.    O objeto retornado por filter retorna um iterator, é possivel efetuar casting para se
                trabalhar com uma lista
        IV.     No caso de listas, list comprehensions também poderia ser utilizado para o processo de
                filtragem de dados de uma lista
                A escolha de qual utilizar vai pelo gosto do desenvolvedor
        V.      É possivel efetuar filtragens de dicionários também
        VI.     Caso a lógica necessária seja muito complexa é possivel utilizar uma função
        VII.    É possivel incluir uma nova chave dentro de um dicionário com filter, recomenda-se utilizar
                map
'''
from dados import lista, produtos

print("\n I e II")
# retorna em uma nova lista apenas valores maiores que 5 da lista
nova_lista1 = filter(lambda x: x > 5, lista)
print(type(nova_lista1))
print(nova_lista1)

print("\n III")
print(list(nova_lista1))

print("\n IV")
nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)

print("\n V")
#filtrar produtos de um dicionário com o valor maior que 10
nova_lista3 = filter(lambda x: x['preco'] > 10, produtos)
for x in nova_lista3:
    print(x)

print("\n VI")
def filtra(produto):
    if produto['preco'] > 50:
        return True
nova_lista4 = filter(filtra , produtos)
for x in nova_lista4:
    print(x)

print("\n VII")
def filtra2(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = "Sim"
        return True
    else:
        return True
nova_lista5 = filter(filtra2, produtos)
for x in nova_lista5:
    print(x)