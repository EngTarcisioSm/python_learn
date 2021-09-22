'''
CSV - Comma Separated Values

    - valores separados por virgula
    - É um formato de dados muito usado em tabelas (Excel, Google Sheets), base de dados, clientes de email, etc...

    - CRIAR, ESCREVER E LER

'''
import csv
import dados


#Leitura de arquivo csv
dados = 0
pathcsv = r'F:\projetos\Python_learn_vsCode\004_Modulos\007_csv\clientes.csv'
with open(pathcsv, 'r') as arquivo:
    dados = csv.reader(arquivo)
    for dado in dados:
        print(dado)

#parei em 4:25 aula 137