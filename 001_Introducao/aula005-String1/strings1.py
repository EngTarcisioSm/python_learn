'''
-Strings são um tipo primitivo de dados dentro da linguagem python
-Strings como qualquer coisa dentro da linguagem python são objetos e como tal carregam
consigo várias funções
-O nome de string dentro de python é str
'''

print('alguma coisa')  # conteúdo entre aspas é encarado como um texto pelo python(interpretador)

print(123456)  # não é uma string

print('123456')  # é uma string(str)

# Utilizando aspas simples ou duplas dentro de uma string
# primeira forma: inversão
print("Texto com aspas 'simples'")  # usando aspas duplas como delimitador de strings
#segunda forma: inversão
print('Texto com aspas "duplas"')  #usando aspas simples como delimitador de strings
#terceira forma: caractere de escape
print("Texto com aspas \"duplas\"")  # caractere de escape
print('Texto com aspas \'simples\'')  # caracete de escape

# Texto cru utilizando r
print(r'Texto     cru utilizando \n caractere especial e ele não sendo executado \' \"')