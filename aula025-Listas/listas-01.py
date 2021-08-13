'''
Listas - Introdução

    I. variaveis são uma forma de armazenar valores dentro da memoria

    II.  Listas são um tipo de dados que pode ser utilizado em python.
         II.I.   Diferente das variaveis, listas podem armazenar diversos valores.
         II.II.  Pode conter dados de tipos diversos dentro de sí, desde tipos de dados, funções até
                 objetos
         II.III. Para se criar uma lista dentro de python deve-se se ter um nome para ela seguido do sinal
                 de atribuição, finalizando com abrir e fechar de colchetes

    III. Cada valor de uma lista possui um indice
        III.I   Assim como as strings o acesso pode ser feito com indices positivos e negativos
        III.II  Diferente da string que cada indice comporta um unico caractere, na lista é possivel
                colocar valores muito maiores

    IV.  Para acessar qualquer valor de uma lista assim como strings basta informar seu nome e entre paren-
        tesis informar o indice

    V.  Para alterar o valor de um indice de uma lista basta informar nome, entre colchetes o indice a ser
        alterado o sinal de atribuição seguido do novo valor, o qual não necessita de ser do mesmo tipo
        o novo valor

    VI. O fatiamento de uma lista é feito da mesma forma que é efetuado nas strings, informando o valor
        de inicio, seguido de dois pontos, o de fim (que não será incluso no retorno) e tudo isso entre
        parentesis [x;y]. Pode ser omitido tanto o valor de inicio como o de fim
        VI.I.   É possivel inserir step de uma lista inserindo um terceiro valor no intervalo de fatia-
                mento. [x:y:z]
                Passando um step negativo o retorno é inverso, sendo uma forma simples de se inverter uma
                lista ou string

    VII.    Metodos de listas
            VII.I   Concatenar listas
                    - '+' : operador de soma pode concatenar 2 listas
                    - lista1.extend(lista2): concatena na lista1 os valores da lista2, é possivel adicionar
                    valores com extend, entretanto para esse processo é rotineiro utilizar outra fun-
                    ção append()
            VII.II  Incluir valores em uma lista
                    .append() -> insere um valor após o ultimo elemento da lista
            VII.III Inserir valor em qualquer posição da de uma lista
                    .insert(x,y) -> onde x é a posição(indice) a ser colocado o valor e y o valor a ser
                    colocado
            VII.IV  Remover o ultimo elemento de uma lista
                    .pop() -> remove o ultimo elemento de uma lista
            VII.V   Remover um trecho da lista
                    del(lista[x:y]) -> remove um trecho de uma lista, é necessário inserir como atributo
                    a lista e o trecho a ser removido
                    É possivel inserir apenas a lista com um indice e será removido apenas um unico item

    VIII.   Pegar valores maximos e monimos de uma lista
            VIII.I  max(lista) -> tem como parametro o nome da lista e retorna o maior valor da lista
            VIII.II min(lista) -> te, como parametro o nome da lista e retorna o menor valor da lista

    IX. GERANDO LISTAS COM RANGE() E LIST()
        - Ao utilizar o metodo range() ele retorna um objeto range.
        - O metodo list() transforma qualquer coisa iteravel em uma lista
        - Como range é um objeto iteravel é possivel utilizar list(range()) e criar uma lista desta forma
        - É possivel também list(string)

    X.  Listas são objetos iteráveis, podendo ser utilizados com laço for
'''
# II
lista = [1, 2, 3, 4, 'Tarcísio', False]

# III
#          0    1    2    3    4
lista2 = ['A', 'E', 'I', 'O', 'U',]
#         -5   -4   -3   -2   -1

# IV
print(lista2[1])

# V
lista[5] = 10.999
print(lista)

# VI
print(lista[2:5])
print(lista[:4])
print(lista[2:])
print(lista[1::2])
print(lista[::-1])

# VII.I
l3 = lista + lista2
print(l3)
lista.extend(lista2)
print(lista)

# VII.II
l3.append(True)
print(l3)

# VII.III
l3.insert(2,'bulbassauro')
print(l3)

#VII.IV
l3.pop()
print(l3)

#VII.V
del(l3[2:6])
print(l3)
del(l3[2])
print(l3)

# VIII:
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l4))
print(min(l4))

# IX
l5 = list(range(0, 11))
print(l5)
l6 = list(range(0, 101, 8))
print(l6)
l7 = list('Tarcisio')
print(l7)

# X
for letra in l7:
    print(letra)

acumulador = 0
for n in l6:
    acumulador += n
print(acumulador)

for elem in lista:
    print(f'O tipo de {elem} é {type(elem)}')