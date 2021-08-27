'''
    Operador Or
'''

nome = input('DIgite um nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada')

# com o operador booleano or o código é simplificado
print(nome or 'VoCê não digitou nada')

#outro exemplo
a = 0
b = None
c = False
d = []
e = {}
f = 22  # irá parar aqui pois todos os acima são falsos
g = 'Tarcisio'

var = a or b or c or d or e or f or g
print(var)