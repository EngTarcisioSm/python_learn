'''
Formatando valores com modificadores - Aula 05
    - Caracteres para formatação os tipos
        :s - Textos (strings)
        :d - Inteiros (int)
        :f - Números de ponto flutuante (float)
            :(numero)f - Quantidade de casas decimais (float)
        :(caractere)(> ou < ou ^)(Quantidade)(tipo - s, d ou f
        > - Esquerda
        < - Direita
        ^ - Centro
'''
num_1 = 1

# definindo o numero de casas decimais na impressão
print(f'{num_1:3f}')  # a formatação somente ocorre no ato da impressão o valor da variavel não altera

# inserir casas decimais a esquerda, neste caso complementará os valores inexistentes com zeros
print(f'{num_1:0>5}')  # o numero ao todo terá 5 algarismos com 4 zeros a esquerda

# adicionar numeros a esquerda e casas decimais ao mesmo tempo
print(f'{num_1:0>6.2f}')

# é possivel formatar strings também de forma analoga a floats
nome = 'tarcísio'
sobrenome = 'souza de melo'

# colocando caracteres em ums string
print(f'{nome:#^15}')

# alteração de strings
# - lower() : deixa tudo minusculo
# - upper() : deixa tudo maiusculos
# - title() : primeiras letras maiusculas

print(nome.lower())
print(nome.upper())
print(nome.title())