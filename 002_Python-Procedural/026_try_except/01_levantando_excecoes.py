'''
    - Lançamento de proprias exceções
    - Página de consulta: https://docs.python.org/3/library/exceptions.html

    - I.        Quando criamos funções ou mesmo classes, é uma pratica comum e errada tentar tratar todo e
                qualquer problema internamente na função, acabando com que modifique o comportamento da
                linguagem. No caso de excessões é possivel fazer com que a excessão possa ter algum trata-
                mento interno (gerando algum log por exemplo) e sendo externado para fora para que quando
                essa função consumida por terceiros possa ter o comportamento correto de gerar erros e
                poder ser tratado por quem consome aquele código
    - II.       Para isso faz-se uso da palavra reservada "raise". desta forma é possivel efetuar algum tra-
                tamento internamente na função e ela continuar a externar excessão

    - III.      Sabendo de que excessão se trata ainda sim é possivel gerar a excessão bruta, sabendo qual
                excessão ira retornar
    - IV        É possivel criar as proprias mensagens de erro, alterando as mensagens de erro ja existentes
                para isso é necessário ser bem especifico no erro a ser diagnosticado, posteriormente achar
                no link acima qual excessão das ja existentes no python se aplicaria a situação e com o
                uso de raise, colocando como seu parametro a mensagem de erro desejada
    - V         Para usuários não é comum passar informações muito técnicas
'''

def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log', error)
        raise   # permite externar um erro entretanto tratado inicialmente pela função


try:
    print(divide(2,0))
except:
    print('erro')


try:
    print(divide(3,0))
except ZeroDivisionError as error:
    print(error)


def divide2(n1,n2):
    if n2 == 0:
        raise ValueError("Denominador não pode ser igual a zero ")
    else:
        return n1/n2

try:
    print(divide2(2,0))
except ValueError as error:
    print(error)