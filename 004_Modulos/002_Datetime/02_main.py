'''
    i.      Pegar a data atual do sistema -> .now()
    ii.     Para imprimir uma data com o formato local é necessário importar outra biblioteca chamado locale com os módulos setlocale e LL_AC. Recebe dois parametro o primeiro é LL_ALL e o segundo uma string de configuração, caso deixado o segundo parametro em branco será pego as configurações da máquina 

    iii.    Para saber o ultimo dia do mês atual existem várias formas, uma delas é importar a biblioteca calendar e dentro dela o modulo mdays que é uma lista 

    https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/18071297#overview

'''
from datetime import datetime
#ii
from locale import setlocale, LC_ALL
#iii
from calendar import mdays


#ii
setlocale(LC_ALL, 'pt_BR.utf-8')

#i
dt = datetime.now()
print(dt)

#ii
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

#iii
print(mdays)

mes_atual = int(dt.strftime('%m'))
print(mdays[mes_atual])