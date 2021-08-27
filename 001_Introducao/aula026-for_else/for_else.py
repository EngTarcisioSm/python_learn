'''
For /Else em Python

(I)
- Pelo fato de listas serem iteraveis é possivel utilizar for sobre elas
- O for assim como o while possui break(quebrando o laço) e continue(pulando para a proxima iteração)

(II)
- string.startswith(x) checa se determinada string começa um um valor x, podendo este ser passado de
forma literal
-string.lower().startswith(x) checa se determinada string começa com um valor x, podendo este ser passado
de forma literal, o lower() deixará toda a palavra em minusculo, logo o valor ou literal de x deve ser
minusculo tb

(III)
Assim como while o laço for suporta um else

()
- python é case sensitive
'''

lista = ['Tarcísio', 'Bryan', 'Barbara']
for item in lista:
    print(item)

# (II)
tem_B = False
for item in lista:
    if item.lower().startswith('b'):
        tem_B = True
if tem_B:
    print(f'Existe nome com "B"')
else:
    print(f'Não existe nome com "B"')

# (III)
for item in lista:
    if item.lower().startswith('b'):
        print('Tem nome com "B"')
        break
else:
    print('Não tem nome com "B"')