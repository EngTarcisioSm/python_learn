'''
Formatação de Strings
    - utilizando f'texto {nome_variavel}'
    - O processo de formatação de uma string fica mais fácil utilizando fstrings e também mais fácil
    de um outro programador ler o código
'''

nome = 'Tarcísio'
idade = 32
altura = 1.82
e_maior = idade > 18
peso = 132
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

# utilizando fstrings
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')
# configurando a string para utilizar o numero de ponto flutuante com duas casas decimais
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

# utilizando .format()
print('{} tem {} anos e imc {}'.format(nome, idade, imc))
# .format() com numeração
print('{0} tem {1} anos e imc {2}'.format(nome, idade, imc))
# .format() com nomes de atributos
print('{a} tem {b} anos e imc {c}'.format(a=nome, b=idade, c=imc))
# o format() com numeração e nome de atributos tem a vantagem de poder se repetir atributos
# caso haja a necessidade

# .format() com formatação de numeros de ponto flutuante
print('{} tem {} anos e imc de {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e imc de {2:.2f}'.format(nome, idade, imc))
print('{a} tem {b} anos e imc de {c:.2f}'.format(a=nome, b=idade, c=imc))
