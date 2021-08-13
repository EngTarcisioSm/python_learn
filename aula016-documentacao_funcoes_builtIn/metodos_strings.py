'''
- A linguagem conta com alguns métodos embutidos que facilitam a vida do desenvolvedor
- Metodos associados a strings
'''
num1 = input('Digite o numero 1: ')
num2 = input('Digite o numero 2: ')
'''
- metodo que verifica se uma função pode ser convertida para um número 
    - isnumeric
    - isdigit
    - isdecimal
- retornam um booleano informando se a conversão pode ocorrer ou não 
'''
# verifica se a conversão para numero inteiro e positivo
print(num1.isnumeric())
print(num2.isnumeric())

if num1.isnumeric() and num2.isnumeric():
    print(f'{num1}+{num2}={int(num1)+int(num2)}')
else:
    print('Impossivel realizar a conversão')
