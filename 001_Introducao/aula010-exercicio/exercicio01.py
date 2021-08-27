"""
* Criar variaveis para nome (str), idade(int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando f-strings (com chaves)
"""

nome = 'Tarcísio'
idade = 32
altura = 1.82
peso = 132

ano_atual = 2021
ano_nascimento = ano_atual - idade

imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura:.1f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}')