'''
    MAP
    - Responsavel por efetuar mapeamentos

    I.      Map é uma função que tem como objeto modificar dados

    II.     O primeiro argumento de map é uma função (podendo ser uma função lambda), o segundo parametro
            desta função é um objeto

    III.    A função MAP não retorna uma lista pronta, retorna um iterador para se iterar sobre o elemento

    IV.     Para se ter um novo item é obrigatório fazer um casting caso o objeto de map não seja válido na
            utilização

    V.      Problemas resolvidos com MAP podem ser ser resolvidos de mesma forma com list comprehension

    VI.     O MAP fica pouco util com listas entretanto com dicionários começam a ficar mais interessante
            quando utilizado com dicionários

    VII.    Pode ser usado para extrair dados de um conjunto de dicionários

'''
# Import de dados específicos de dados
from dados import produtos, pessoas, lista

print('\n I, II e III')
nova_lista = map(lambda x: x*2, lista)
print(nova_lista)

print('\n IV')
print(list(nova_lista))

print('\n V')
nova_lista2 = [x * 2 for x in lista]
print(nova_lista2)

print('\n VI')
# Aumentar o preço dos produtos em 5%, atraves da função lambda não é possivel efetuar esse processo
#sendo necessário a criação de um novo produto
def altera_preco(p):
    p['preco'] = round(p['preco'] * 0.05,2) # mantem duas casas decimais
    return p
novos_produtos = map(altera_preco, produtos)
print(produtos)
print(list(novos_produtos))

print('\n VII')
# retirar apenas os nomes
nomes = map(lambda p:p['nome'], pessoas)
# retirar apenas as idades
idade = map(lambda p:p['idade'],pessoas)
print(list(nomes))
print(list(idade))