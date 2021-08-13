'''
Função len()
    - serve para contar a quantidade de caracteres de uma string
    - também funciona para outros tipos de dados além de strings
    - não funciona com tipos numericos
'''

usuario = input("Digite seu nome: ")

# conta o numero de caracteres dentro de uma string retornando um numero inteiro. espaços também
# são considerados como caracteres
qtd_caracteres = len(usuario)

print(usuario, type(usuario), qtd_caracteres)