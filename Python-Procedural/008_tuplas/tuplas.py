'''
- Tuplas
    - I.    Tuplas são similares a listas
    - II.   A diferença entre tuplas e listas que as tiplas não são possiveis depois de criado ter seu valor
    alterado ou aidionado, uma vez criado
    - III.  É possivel converter tuplas para listas e listas para tuplas
    - IV.   Ao inves de utilizar chaves utiliza-se ()
    - V.    Os valores não necessitam ser do mesmo tipo
    - VI.   Para acessar seus indices é igual a listas
    - VII.  É possivel iterar uma tupla com laço for
    - VIII. É possivel fatiar tiplas igual listas
    - IX.   É possivel criar tuplas sem auxilio dos ()
    - X.    É possivel criar uma tupla com 1 elemento, bastando depois do elemento colocar uma virgula
    - XI.   Remover itens da tupla igual lista]
    - XII.  É possivel repetir o valor de uma tupla durante sua criaçãoi utilizando o operador *
    - XIII. Se converte tupla para lista com list()
    - XIV.  Converter lista para tupla com tuple()
'''
# I a VII
t1 = (1, 2, 3, 'B', 'Tarcísio')
print(type(t1))
print(t1)

for v in t1:
    print(v)

# VIII
print(t1[2:])

# IX
t2 = 1, 2, 3, 4, 5, 'Bryan'
print(type(t2))
print(t2)

# X
t3 = 10,
print(type(t3))

# XI
n1, n2, *_ = t1
print(n1)
print(n2)

# XII
t4 = (1,2,3,4,5,5,6,7,8) * 10
print(t4)

# XIII
t5 = (1,2,3,4,5,6,6,7)
t5 = list(t5)
t5[2] = 8000
print(t5, type(t5))
t5 = tuple(t5)
print(t5, type(t5))