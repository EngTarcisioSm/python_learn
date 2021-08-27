'''
Variáveis
    - rotulo de endereços de memória
    - = simbolo de atribuição
    - Nomenclatura
        - Iniciar com letras
        - pode conter números, não sendo o primeiro caractere
        - não pode usar espaço, caso haja necessidade de espaçamento usar underscore '_'
        - letras minusculas
    - É possivel efetuar operações logicas e matemáticas com variáveis
'''

nome = 'Tarcísio'  # string
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  # boolean

print('Nome: ', nome, 'tipo: ', type(nome))
print('Idade: ', idade, 'tipo: ', type(idade))
print('Altura: ', altura, 'tipo: ', type(altura))
print('É maior: ', e_maior, 'tipo: ', type(e_maior))

# operações matemáticas com variáveis
print(idade * altura)