'''
    Zip - Unindo iteráveis
    Zip_longest - Itertools

    1.  - Tem como função unir iteraveis
    2.  - Objetos zip são possiveis de converter em outros tipo como listas, dicionários
    3.  - Tendo listas de tamanhos diferentes ele só unirá até o tamanho da menor lista (ZIP)
    4.  - Para "corrigir o problema de unir apenas o menor tamanho utiliza-se o módulo itertools /
    zip_longest. este modulo uni pelo maior e os valores faltantes são preenchidos com none
        1.  -É possivel alterar o valor vazio para algum valor especifico, para isso um atributo nomeado
        deve ser inserido colocando o valor a ser desejado, o atributo possui o nome de fillvalue
    5.  - Dentro de itertools existe existe a biblioteca count que tem como função gerar um contado infinito
        o qual é um gerador, iterador
'''
import sys
from itertools import zip_longest, count

### linhas de código
cidade = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Caixa Prego']
### linhas de código
estado = ['SP', 'MG', 'BA', 'MG']
cidades_estados = zip(estado, cidade)

print(type(cidades_estados), sys.getsizeof(cidades_estados))
for valor in cidades_estados:
    print(valor)
cidades_estados2 = zip_longest(estado, cidade)
for valor in cidades_estados2:
    print(valor)

cidades_estados3 = zip_longest(estado,cidade,fillvalue='Estado')
for valor in cidades_estados3:
    print(valor)

indice = count()
cidades_estados4 = zip(
    indice,
    estado,
    cidade
)

for indice, estado, cidade in cidades_estados4:
    print(indice, estado, cidade)