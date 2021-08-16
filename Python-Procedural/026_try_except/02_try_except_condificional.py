'''
USO DE TRY EXCEPT COMO CONDICIONAL

    - AULA DE TIRAR DÚVIDAS
    - USO DE TRY EXCEPT

    - I.    Em um processo hipotético de requisição de um número, tratar todas as possibilidades de conversão
                - Ver as excessões que aparecem e ir tratando
    - II.   Toda função python caso não possua um retorno retorna none
    -III.   Valor none não efetua calculos
'''

# I
def converte_numero(valor):
    try:
        # tenta conversão para um numero inteiro
        valor = int(valor)
        return valor
    except:
        try:
            # se conversão para inteiro falhar tenta para ponto flutuante
            valor = float(valor)
            return valor
        except ValueError:
            pass

while(1):
    numero = converte_numero(input('Digite um numero: '))
    if numero is not None:
        print(numero * 5)
        break

