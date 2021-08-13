'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número
é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um numero inteiro
'''

numero = input('Digite um numero: ')
if numero.isnumeric():
    par = int(numero) % 2
    if par == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
else:
    print(f'"{numero}" não é um numero inteiro')