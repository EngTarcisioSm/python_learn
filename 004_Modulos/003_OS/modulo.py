'''
    Módulo OS

    - metodo walk -> permite entrar dentro de todas pastas e subpastas de um sitema verificando todos os arquivos 
        os.walk(caminho_de_busca)
    Entrega 3 valores a raiz (caminho onde se esta buscando), diretorios e arquivos 

    - metodo x = os.path.join(raiz, arquivo)
    Retorna todo o o caminho do arquivo

    - metodo x, y = os.path.splitext(arquivo)
    Retorna dois valores, o nome do arquivo e o formato do arquivo 


    projeto percorre pasta e encontra arquivo especifico
'''
import os

caminho_procura = input('Digite um caminho.: ')
termo_procura = input('Digite um termo.: ')

contador = 0



def formata_tamanho(tamanho):
    base = 1024
    kilo = base **1
    mega = base **2
    giga = base **3
    tera = base **4
    peta = base **5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho,2) #especifica o numero de casas decimais 

    return f'{tamanho} {texto}b'




for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                caminho_completo = os.path.join(raiz,arquivo)
                #print(caminho_completo)

                # divide o nome do arquivo e sua extensão
                nome_arquivo, extensao = os.path.splitext(arquivo)
                #print(f'{nome_arquivo} | {extensao}')

                # informa o tamanho do arquivo em bytes
                tamanho = os.path.getsize(caminho_completo)
                #print(tamanho)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print(extensao)
                print('Tamanho:', formata_tamanho(tamanho))

                contador+=1
            except PermissionError as e:
                print('Sem permissoes.')
            except FileNotFoundError as e:
                print("Arquivco não encontrado")
            except Exception as e:
                print("Error desconhecido", e)

print()
print(f'{contador} arquivo(s) encontrado(s)')