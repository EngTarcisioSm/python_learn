'''
Trocando valores de variaveis
'''

# Em outras linguagens de programação para trocar o valor de duas variaveis é necessário criar uma
# terceira variavel, que armazene um dos valores para que seja efetuado a troca, isso funciona no python
# entretanto existe uma maneira mais fácil

# Exemplo como em outras linguagens
x = 10
y = 'Tarcísio'
print(f'x = {x} y = {y}')
z = x
x = y
y = z
print(f'x = {x} y = {y}')

# Modo mais fácil em Python
a = 11
b = 'Bryan'
print(f' a = {a} b = {b}')
a, b = b, a
print(f' a = {a} b = {b}')

# Este modo não se resume apenas a dois valores
a = 10
b = 'zeta'
c = True
print(f'a:{a} b:{b} c:{c}')
a, b, c = c, a, b
print(f'a:{a} b:{b} c:{c}')
