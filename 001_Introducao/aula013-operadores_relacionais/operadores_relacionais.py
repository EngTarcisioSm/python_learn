'''
Operadores relacionais
    - Realizam comparações entre coisas
    ==
    >
    <
    >=
    <=
    !=
    - sempre retornam valor boolean
'''
num_1 = 2
num_2 = 2
num_3 = '2'
num_4 = 4

expressao = num_1 == num_2  # é igual?
print(expressao)  #  imprime um boolean

expressao = num_1 != num_2  # é diferente
print(expressao)

expressao = num_1 > num_2  # é maior
print(expressao)

expressao = num_1 < num_2  # é menor
print(expressao)

expressao = num_1 >= num_2  # é maior ou igual
print(expressao)

expressao = num_1 <= num_2  # é menor ou igual
print(expressao)

# usando operadores relacionais com if
nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
idade_minima = 18

if idade >= idade_minima:
    print(f'{nome} pode pegar empréstimo')

# utilizando operador relacional com if e else
if idade < 18:
    print('menor de idade')
else:
    print('maior de idade')

# realizando mais de uma operação relacional juntamente com elif
if idade < 18:
    print('menor de idade')
elif idade >= 18 and idade < 59:
    print('adulto')
else:
    print('idoso')
