'''
while - parte 2
'''
# dentro de um laço while é comum utilizar um contador que será incrementado ou decrementado com o
# objetivo de finalizar o loop quando a condição não for satisfeita
contador = 0
while contador <= 100:  # quando a condição deixar de ser satisfeita o loop encerra
    print(contador)
    contador += 1

# diferentemente de outras linguagens de programação o loop while comporta um 'else' em que assim
# que a condição do loop se tornar falsa este loop while será executado
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Acabou a contagem')
print('Código que segue...')

# o else é importante no laço while pois caso o código do laço while seja interrompido por um
# 'break' esse 'else' não será executado, ou seja o else do laço while só é executado quando o loop
# while é finalizado totalmente
contador = 0
while contador <= 10:
    if contador >= 5:
        break
    print(contador)
    contador += 1
else:
    print('loop while finalizou completamente...')
print('continuando...')