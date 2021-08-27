'''
exercicios
    1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome
    2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles
    3 - Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um percentual (0 - 100)
    Retorne o valor do primeiro número somado ao percentual do mesmo
    4 - fizz buzz - Se o parâmetro da função for divisivel por 2, retorne fizz se o parâmetro da função
    for divisível por 5 retorne buzz. Se o parametros  da função por divisivel por 5 e por 3, retorne FuzzBuzz,
    caso contrario retorne o numero enviado.
'''

def saudacao(saudacao:str, nome:str):
    print(f'{saudacao} {nome}')

def sum(num1:int, num2:int, num3:int):
    print(num1+num2+num3)

def sumPerct(num:int, percent:float):
    return num + num*(percent/100)

def FizzBuzz(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


# Teste Área teste
saudacao('Bom dia', 'Tarcísio')
sum(10,20,30)
print(sumPerct(10, 50))
print(FizzBuzz(21))