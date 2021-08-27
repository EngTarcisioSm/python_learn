'''
    - REDUCE
        I.      O MÉTODO REDUCE NÃO VEM NATIVAMENTE JUNTO COM O PYHTON PARA UTILIZA-LA É NECESSÁRIO IMPORTA-LA
                from functools import reduce
        II.     A função reduce tem por objeto ser uma acumuladora compulsiva
        III.    A função recebe quatro parâmetros:
                    - uma função lambda com um acumulador
                    - uma expressão na qual recebe um item "i" e esse item é somado ao parametro da função
                    lambda
                    - a lista em questão
                    - o valor inicial do acumulador
        III. I  A função lambda acaba fazendo o código ficar mais limpo pois reduz a necessidade de laços de
                repetição para efetuar o mesmo processo
        IV.     Funciona também com dicionários

'''
# (#I)
from dados import produtos, pessoas, lista
from functools import reduce

print("# II e III")
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

print('# IV')
soma_dicionario = reduce(lambda ad, p: p['preco'] + ad, produtos, 0)
print(soma_dicionario)
# fazendo a média de preços
print(soma_dicionario / len(produtos))

print("# IV")
soma_dicionario2 = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
media_idade = (soma_dicionario2 / len(pessoas))
print(media_idade)