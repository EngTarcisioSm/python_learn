'''
- SETS: CONJUNTOS
    - 1.    SIMILARES A LISTAS;
    - 2.    Forma um conjunto de elementos que se pode adicionar dentro de uma mesma estrutura de dados;
    - 3.    A principal diferença é que os sets não admitem elementos repetidos;
    _ 4.    Existem duas formas de se criar sets, a primeira é com {} similar a dicionários;
        - 1.Com {} o set não apresenta chaves
    - 5.    Suporta apenas elementos imutaveis
    - 6.    Não possuem indices, desta forma não é possivel acessar elementos de forma unitária
    - 7.    É possivel iterar com for sobre um set
    - 8.    Não é possivel criar sets em branco com {} ao fazer isso será criado um dicionario
    - 9.    A segunda forma de se criar um set é com set(), permitindo inclusive criar sets em branco
    - 10.   Para adicionar um novo elemento utilizar .add(elemento(s)) é possivel inserir apenas elementos
            imutaveis
        - 1.É possivel inserir, valores, unitário, tuplas, strings,
    - 11.   Para remover elementos utiliza-se .discard()
    - 12.   A função .update é similiar a função .add() com a diferença que ele itera sobre o valor inserido
            ou seja, quando colocado uma string ele não colocará a string como um todo mais sim cada caracte-
            re. Evidencia que o set não obedece ordem. A função update geralmente é utilizada para inserir
            uma lista, set, etc dentro de um "set"
    - 13.   Em geral, sets são utilizados para a remoção de valores duplicados de uma lista. \o unico
            são os elementos ficarem fora de ordem
    - 14.   função union ou | (pipe) -> une dois sets não repetindo os elementos existente entre eles
    - 15.   função intersection ou & -> retorna uma intersecção entre os elementos, ou seja, retorna apenas
            aqueles que estão em ambos
    - 16.   função diferente ou - -> retorna apenas o elemento do primeiro set que não se encontra no
            segundo set, neste caso a ordem importa
    - 17.   função symmetric_difference ou ^ -> retorna os elementos que existe em um e não no outro, re-
            tornando os elementos exclusivos de ambos
    - 18.   Uma das vantagens de se utilizar sets é verificar se duas listas são igual mesmo que uma tenha
            valores repetidos
'''
print("#4")
s1 = {1,2,3,4,5,6,7}
print(type(s1))
print(s1)
print()
print("#7")
for x in s1:
    print(x)
print()

print("#9")
s2 = set()
print(type(s2))
print()

print("\n#10")
s2.add(1)
print(s2)
s2.add((1, 2, 3, 4, 5, 6, 'Tarcísio'))
print(s2)
s2.add("Bryan")
print(s2)

print("\n#11")
s2.discard(1)
print(s2)

print("\n#12")
s3 = set()
s3.update('Externocleidomastódio')
print(s3)

print("\n#13")
l1 = [1,2,3,4,5,5,5,55,3,2,2,2,2,1,1,"Bryan", "Tarcisio"]
print(l1)
l1 = list(set(l1))
print(l1)

print("\n#14")
s4 = {1,2,3,4,5}
s5 = {1,2,3,4,5,6}
s6 = s4 | s5
print(s6)

print("\n#15")
s7 = s4 & s5
print(s7)

print("\n#16")
s8 = {1,2,3,4,5,6}
s9 = {1,2,3,4,5,7}
s10 = s8 - s9
print(s10)
s10 = s9 - s8
print(s10)

print("\n#17")
s11 = s8 ^ s9
print(s11)

print("\n#18")
s12 = ["Bryan", "Tarcísio", "Janete", "Alípio"]
s13 = ["Bryan", "Tarcísio", "Janete", "Alípio", "Janete", "Alípio", "Janete", "Alípio", "Bryan", "Tarcísio"]

s12 = set(s12)
s13 = set(s13)
print(s12 == s13)