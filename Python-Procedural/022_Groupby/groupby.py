'''
    - Agrupar elementos em um dicionário

    I.      groupby esta dentro da biblioteca itertools
    II.     Para que o groupby funcione a lista de dicionários deve estar ordenado pela chave de interesse
            para isso utiliza-se o metodo sort()
    III.    tendo os valores devidamente ordenados groupby agrupará os valores iguais conforme a chave do
            dicionario selecionada
    IV.     É possivel após o agrupamento efetuar a contagem de quantos componentes existem por cada grupo
            o objeto retornado por groupby tem de ser convertido para uma lista
    V.      Groupby retorna apenas iteradores e como tal após utilizado não é possivel ser reutilizado 
'''
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'}
]
print('\n# II')
ordena = lambda item: item['nota']
alunos.sort(key= ordena)

print('\n# III')
alunos_agrupados = groupby(alunos, ordena)
print(alunos_agrupados)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento:{agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()

print('\n#IV')
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')