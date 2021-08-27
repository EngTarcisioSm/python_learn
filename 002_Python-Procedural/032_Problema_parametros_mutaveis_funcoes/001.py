'''
    I.      Ao utilizar atributos mutaveis com valores defaut deve-se tomar cuidado, pois o python apresenta
            comportamento divergente do correto
    II.     Tem se como variaveis mutaveis: Listas, Dicionários...
    III.    Tem se como variaveis imutaveis: Tuplas, strings, numeros, True, False, None
    IV.     Para burlar esse problema uma opção é iniciar o atributo com um valor imutavel e durante o
            código caso o valor permaneça mutável mudar ele para o tipo que é desejado
'''

print("#I")
def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)

print("#IV")
def lista_de_clientes2(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes2(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes2(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes2(['José'])

print(clientes1)
print(clientes2)
print(clientes3)