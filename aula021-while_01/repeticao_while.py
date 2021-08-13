'''
Em python existe dois laços de repetição, o laço while e o laço for
'''

# while
# usado na repetição de processos, possui um bloco de código referente a suas intruções
# Estrutura
'''
while condicao:
    códigos
    ...
'''
# A palavra while em inglês, significa 'enquanto', logo enquanto a condição passada for verdadeira
# a estrutura de código identada será repetida
'''
loop infinito 
while True:
    código
    ...
O loop acima será um loop infinito pois a condição de while sempre será true
'''
# loops finitos: em loops finitos a condição de existencia do loop whiles em algum momento sua condição
# deve se provar falsa para qu o loop infinito não ocorra e o loop é finalizado

# contagem de 0 - 100
x = 0
while x <= 100:
    print(x)
    x += 1

# continue
# utilizando para pular algum determinado laço de repetição, em geral é feito alguma testagem e dependendo
# do resultado o continue é executado  e a iteração daquele momento é pulada

# printar os pares
x = 0
while x <= 100:
    x += 1
    if (x % 2) == 0:
        print(x)
    else:
        continue
    print(',')

# Calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite um número: ')
    operator = input('Digite um operador: ')
    exit = input('Sair: [s]im ou [n]ão: ')

    if not (num_1.isnumeric() and num_2.isnumeric()):
        print('Você precisa digitar apenas números...')
        continue

    if exit == 's':
        # utilizado para interromper laços de repetição
        break

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido...')
