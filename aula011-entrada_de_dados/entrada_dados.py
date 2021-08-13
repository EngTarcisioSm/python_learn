'''
Entrada de Dados
'''

# função que solicita dados do usuario, tem como retorno o que o usuário digitou no shell
nome = input("Qual o seu nome? ")
# print(f'Este foi o nome digitado {nome} e o tipo da variavel é {type(nome)}')

# pegando o dado do usuário e efetuando um cast imediatamente de str -> int
ano_nascimento = int(input('Ano de Nascimento: '))
idade = 2021 - ano_nascimento

print(f'{nome} tem {idade} anos de idade, nascido em {ano_nascimento}')