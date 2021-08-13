'''
    -  Operadores lógicos
        and
        or
        not
        in
        not in
    - Operador and e or são utilizados para efetuar mais que uma comparação, a expressão composta de
    and ambas as condições devem ser true, enquanto a condição or apenas uma das condições devem ser
    true para gerar uma resposta true
    - O operador not também chamado de inversor, inverte valores booleanos
'''
a = 1
b = 2
c = 3
d = 4
resposta1 = a > b and c > d
print(resposta1)

resposta1 = a > b or c > d
print(resposta1)

e = False
f = not e
print(f)

# not sendo usado para verificar se uma variavel esta vazia
g = ''
h = 0
if not g:
    print('g esta vazio')
    print(not g)
if not h:
    print('h esta vazia')
    print(not h)

# operador in checa se existe algo dentro de alguma coisa
nome = 'Tarcisio'
if 'a' in 'Tarcisio':
    print(f'Existe letra "a" dentro de {nome}')