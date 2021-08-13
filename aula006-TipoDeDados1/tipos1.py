'''
Tipos de dados
string  : str   : textos
inteiro : int   : valores inteiros positivos, negativos ou zero
float   : float : ponto flutuante
booleano: bool  : True ou False
'''
# função type retorna o valor de atributo passado
print('adsdad',type('adsdad'))
print(12345, type(12345))
print(1.2345, type(1.2345))
print(False, type(False))
print('12345', type('12345'))

# conteúdo vazio convertido retorna false
print(bool(''), type(''))

# conversões
print('Tarcísio', type('Tarcisio'), bool('Tarcisio'))

print('10', type('10'), type(int('10')))

# int('10.0') não é possivel
# float('10.0') é possivel