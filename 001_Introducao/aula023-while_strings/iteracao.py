'''
O uso de loop while com strings não é tão comum
'''

frase = 'Tarcísio Souza de Melo'
tamanho_frase = len(frase)

contador = 0
while contador < tamanho_frase:
    print(frase[contador], contador)
    contador+=1

# torna-se possivel iterar sobre itens alterando seu valores e alocando em uma nova string
contador = 0
nova_string = ''
while contador < tamanho_frase:
    nova_string += frase[contador].upper()
    contador +=1
print(nova_string)  # todos caracteres convertidos para maiusculo