'''
    Módulo OS

    - metodo walk -> permite entrar dentro de todas pastas e subpastas de um sitema verificando todos os arquivos 
        os.walk(caminho_de_busca)
    Entrega 3 valores a raiz (caminho onde se esta buscando), diretorios e arquivos 

    - metodo x = os.path.join(raiz, arquivo)
    Retorna todo o o caminho do arquivo

    - metodo x, y = os.path.splitext(arquivo)
    Retorna dois valores, o nome do arquivo e o formato do arquivo 


    parei em 10:07 video 133
'''
import os

caminho_procura = 'C:\_dev\Gráfico'
termo_procura = 'main'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        #caminho_completo = os.path.join(raiz,arquivo)
        #print(caminho_completo)

        nome_arquivo, extensao = os.path.splitext(arquivo)
        print(f'{nome_arquivo} | {extensao}')

