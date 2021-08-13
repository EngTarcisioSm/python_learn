'''
Operador Ternário em Python
'''

# O operador ternário esta presente em outras linguagens de programação, tem como objetivo a reduçao
# e simplificação de código

# Estrutura do Ternário:
# variavel = 'valor se verdadeiro' if (condição para verdadeiro) else 'valor se falso'

# Sem Ternário exemplo
usuario_logado = True
msg = ''
if usuario_logado:
    msg = 'Usuario logado'
else:
    msg = 'por favor logar'
print(msg)

# com ternário
msg = 'Usuario logado' if usuario_logado else 'Usuario se logue'
print(msg)
