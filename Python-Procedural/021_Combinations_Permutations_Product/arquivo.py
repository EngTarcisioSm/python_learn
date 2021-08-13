'''
    I.      Combinations, Permutations e Product estão dentro do módulo Itertools
            Combinação  - Ordem não importa
            Permutação  - Ordem importa
            Ambos não repetem valores únicos
            Produtos    - Ordem importa e repete valores

    II.     Combinations retorna as combinações possiveis de uma lista, recebe 2 parametros a lista
            e a quantidade de entes por grupo
            Para utilizar combinations devese importa-lo de itertools
                from itertools import combinations

    III.    Permutations efetua o mesmo processo que combinations entretanto a ordem importa x e y é
            diferente de y e x
            Para utilizar combinations devese importa-lo de itertools
                from itertools import permutations

    IV.     Product efetua o mesmo processo de combinations e permutations, aceitando repetição no
            processo
            Para utilizar combinations devese importa-lo de itertools
                from itertools import product
'''
from itertools import combinations, permutations, product

pessoas = ['Alípio', 'Janete', 'Tarcísio', 'Bryan']

print('\n# II')
for grupo in combinations(pessoas, 2):
    print(grupo)

print('\n# III')
for grupo in permutations(pessoas, 2):
    print(grupo)

print('\n# IV')
for grupo in product(pessoas, repeat=2):
    print(grupo)