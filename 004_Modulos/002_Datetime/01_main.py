'''
    - Trabalhando com Data e hora em python 
    https://docs.python.org/3.0/library/datetime.html

    i.      Para se trabalhar com datas em python, importa-se o modulo datetime de date time 
    ii.     O modulo timedelta, é utilizado para verificar tempo (intervalor de tempo)
    iii.    É possivel inserir data nesta classe inserindo os atributos
            variavel = datetime(ano,mes,dia, hora_opcional, minuto_opcional, segundo_opcional)
            A data é impressa no formato americano AAAA-MM-DD HH:MM:SS
    
    iv.     É possivel alterar a estrutura da impressão da hora com o metodo strftime('configuracao') possivel achar na documentação da biblioteca

    v.      É possivel receber uma data em formato de string atraves do método strptime, que possui dois atributos, o primeiro é a string com a data propriamente dita, e a segunda string é o o formato em que a data se encontra na primeira string 

    vi.     É possivel pegar o timestamp -> contagem de segundos de 01/01/1970 até a data inserida

    vii.    É possivel converter timestamp para uma data normal 

    viii.   É possivel somar periodos de tempo a um objeto datetime existente com timedelta

    ix.     É possivel efetuar somas, subtrações e comparações de datas 

    x.      Possivel pegar apenas a hora de um objeto datetime


'''
#i e ii
from datetime import date, datetime, timedelta

#iii
data = datetime(2021, 9, 15, 16, 27, 0)
print(data)

#iv
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#v
data2 = datetime.strptime("20/04/2019","%d/%m/%Y")
print(data2)

#vi
print(data.timestamp())

#vii
data3 = datetime.fromtimestamp(1555729299.0)
print(data3)

#viii
data4 = datetime.strptime("14/01/1989 15:30:00", "%d/%m/%Y %H:%M:%S")
print(data4)
data5 = data4 + timedelta(days =5000, seconds=1000)
print(data5)

#ix
dif = data5 - data4
print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif.days)
print(data4 < data5)

#x
print(data4.time())