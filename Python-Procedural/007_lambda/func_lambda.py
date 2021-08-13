'''
Funções Lambda (funções anonimas)
    - I.    São definidas assim pois não possui nomes
    - II.   Estrutura
            variavel = lambda paramentro1, parametroN: operacao
    - III.  É uma função mais reduzida
    - IV.   Geralmente utilizada quando se deseja passar como parametro uma função para outras funções
    - V.    Não possui retorno
'''

# I, II e III
a = lambda x,y: x * y

print(a(2,3))

# IV
lista = [['P1', 13],
         ['P2', 6],
         ['P3', 7],
         ['P4', 4],
         ['P5', 8]]
# Deseja-se ordenar a lista, para isso utiliza-se a função sort() que recebe como parametro uma função, a
# primeira resposta seria criar uma função e passa-la como parametro ou usar função lambda
lista.sort(key = lambda x: x[1], reverse=True)
print(lista)

#ordenar sem afetar a lista
y = sorted(lista,key=lambda x:x[1])
print(y)
