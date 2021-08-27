'''
Implementar jogo de força
    - Mostra asteriscos indicando o tamanho da mensagem
    - Quando acertar insere a letra no lugar do asterisco
    - inserir quantidade de chances
'''

palavra_secreta = 'Tarcisio'
tamanho_palabra = len(palavra_secreta)
lista_palavra = []

for x in range(0, tamanho_palabra):
    lista_palavra.append('_')

chance = 5
acertos = 0
while True:

    print(f'{chance} chances', end='\n\n')

    for letra in lista_palavra:
        print(letra, end=' ')
    print(end='\n\n')

    if chance == 0 or acertos == (tamanho_palabra -1):
        break

    while True:
        letra_digitada = input('Digite uma letra: ')
        if(len(letra_digitada) > 1):
            print('Apenas uma letra...')
        else:
            break

    if letra_digitada in palavra_secreta or letra_digitada.upper() in palavra_secreta:
        for indice, letra in enumerate(palavra_secreta):
            if letra_digitada == letra or letra_digitada.upper() == letra:
                lista_palavra[indice] = letra

        acertos += 1
        print('Acertou!!!')
    else:
        chance -= 1

if(chance > 0):
    print('Parabéns você acertou a palavra!')
else:
    print('Print você errou, tente novamente...')


