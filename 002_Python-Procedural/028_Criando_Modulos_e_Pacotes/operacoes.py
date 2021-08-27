import math

PI = math.pi        # constante

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica_Lista(lista, multiplicador):
    return [x*multiplicador for x in lista]

if __name__ == '__main':
    # testes de código do módulo
    print(PI)

    lista = [1,2,3,4,5,6,]
    print(dobra_lista(lista))
    print(multiplica_Lista(lista, 10))