'''
Split, Join, Enumerate em python
    i   - Split -> Dividir uma string
          Split em inglês é dividir, é passado como parametro para split o caractere que ele utilizará
          para efetuar a divisão

    ii  - Join -> Juntar listas e também pertence a string
          Transforma uma lista em uma string.
          É necessário passar o caractere que fará a união entre os iteraveis da lista caractere.join(lista)
          o caractere pode ser literal ','.join(lista), podendo usar espaço ' '.join(lista)

    iii - Enumerate - Enumerar elementos da lista (também para objetos iteraveis)

    iv  - lista.count(x) conta a repetição do valor x em uma lista

    v   - uma lista pode conter outra lista
'''

# (i)
string = "O Brasil é o país do futebol, o Brasil é penta"
lista01 = string.split(" ")
print(lista01)
lista02 = string.split(',')
print(lista02)

# (iv)
for palavra in lista01:
    print(f'"{palavra}" apareceu {lista01.count(palavra)}x na string')

# (ii)
string2 = ','.join(lista01)
print(string2)

#(iv)
for indice, palavra in enumerate(lista01):
    print(indice, palavra)

# (v)
lista = [[1, 2],
         [3, 4],
         [5, 6]]
for num1, num2 in lista:
    print(num1,num2)

# também sendo possivel
for valores in lista:
    n1, n2 = valores
    print(n1, n2)