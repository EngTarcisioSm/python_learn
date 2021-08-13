'''
-> Existe uma lista de listas de numeros inteiros
-> As listas internas possuem o tamanho de no máximo 10 elementos
-> As listas internas possuem elementos de 1 a 10 e podem ser duplicados

-> Exercício
    - Crie uma função que encontra o primeiro duplicado considerando o segundo valor repetido como a
    duplicação
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda ocorrencia (o numero duplicado
            em sí
            Exemplo: [1,2,3,->3<-,2,1] (3 é a posição do duplicado)
            Se não encontrar duplicados na lista retorne 1
            Retornar a primeira duplicação 
'''

lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def find_first_duplicate(checklist:list):
    answer = list()
    for x in checklist:
        last = tuple()
        aux = 0
        for y in enumerate(x):
            if y[0] != 0:
                if last[1] == y[1]:
                    answer.append(y[1])
                    break
                elif aux == 9:
                    answer.append(-1)
            last = y
            aux += 1
    return answer

def find_first_duplicate_prof(checklist:list):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in checklist:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    return primeiro_duplicado

print(find_first_duplicate(lista_de_lista_de_inteiros))
print(find_first_duplicate_prof([1,2,3,4,5,6,1]))