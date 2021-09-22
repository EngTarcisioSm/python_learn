'''
Trabalhando com o módulo JSON do python 

JSON(JavaScript Object Notation) - é um formato de troca de dados entre sistemas e programas muito leve e de fácil utilização. Muito utilizado por APIs

Tabela de Conversão (o que transforma em que)

PYTHON          JSON
dic             object
list, tuple     array (quando transformado para python vira list)
str             string
int, float      number (pa conversão inversa depende do valor)
True            true
FALSE           False
None            null

- converter de python para json utiliza-se DUMPS ou DUMP, para converter de JSON para python utiliza-se LOADS ou LOAD

- para usar mexer com JSON é necessário fazer a conversão usar a bilbioteca
json

- quando se converte de python para json passa-se a se ter uma string que contem dados na estrutura JSON 
'''
from dados import dados
import json

#convertendo lista
lista = [1,2,3,4,5,6]
dados_json = json.dumps(lista)

print(dados_json)
print(type(dados_json))

#convertendo um dicionario para json 
dados_json = json.dumps(dados.clientes_dicionario)
print(dados_json)
print(type(dados_json))

#estruturando a conversão para ser impressa de um jeito mais visual 
dados_json = json.dumps(dados.clientes_dicionario, indent=4)
print(dados_json)
print(type(dados_json))

#convertendo de json para dicionario
dicionario = json.loads(dados.clientes_json)
print(dicionario)
print(type(dicionario))
for chave, valor in dicionario.items():
    print(f'{chave}:{valor}')

#é possivel salvar um dicionario python em uma estrutura JSON 
#passo1 - criar um arquivo no modo de escrita 
#passo2 - usar o metodo dump() indicando o dicionario e o arquivo ao qual será salvo
with open('clientes.json','w') as arquivo:
    json.dump(dicionario, arquivo, indent=4)


#ler um json 
with open('clientes.json','r') as reader:
    data = json.load(reader)

print()
print(type(data))
for chave, valor in data.items():
    print(f'{chave}:{valor}')