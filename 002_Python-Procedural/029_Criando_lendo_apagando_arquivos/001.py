'''
CRIANDO, LENDO, ESCREVENDO E APAGANDO ARQUIVOS

    - DOCUMENTAÇÃO: https://docs.python.org/3/library/functions.html#open

    I.      Para criar um arquivo, deve-se criar um objeto com auxilio do método open(). Este método recebe
            dois parametros, o primeiro refere-se ao nome do arquivo juntamente com o seu formato, devendo
            ser esse nome em formato string, o segundo parametro é o tipo de manipulação que sera feita. No
            link acima existe uma tabela com todos os métodos possiveis
                file = open('nome_arquivo.extensão', 'modo_de_operação_sigla')

    II.     Ao criar o objeto é possivel utilizar diversos métodos como por exemplo o método write(). Este
            método possui a finalidade de escrever sobre o arquivo criado

    III.    Sempre quando se abre um arquivo ao termino do seu uso é recomendavel fecha-lo com o método close
            caso o procedimento não seja feito pode acarretar em problemas

    IV.     Ao escrever em um arquivo o cursor no arquivo vai seguindo o texto sempre ficando ao fim. Caso seja
            necessário outra ação por exemplo de leitura é necessário retornar o cursor para o inicio do arquivo.
            Esse processo é feito fechando e abrindo o arquivo ou usando o método seek(a,b) que retornar o
            cursor para o inicio do arquivo. "A" e "B", refere-se a posição para onde o cursor deve ir,  "A" e
            em "B" a posição relativa. Para usos práticos utiliza-se (0,0)
            O esse método é uantes do arquivo ser fechado.

    V.      Para ler um arquivo existe duas funções (métodos), read, que le todas as linhas do arquivo e o
            readline() que le apenas uma unica linha do arquivo, em ambos os métodos o cursor avança com a
            leitura também

    VI.     O metodo readlines() le todas linhas e cada linha é colocada em uma lista
    VI.i.   Como o método acima gera uma lista é possivel utiliza-lo com laço for
    VI.ii.  COmo os metodos read ja finalizam uma escrita com \n em textos pode gerar um efeito se \n duplo
            para evitar isso corrigir em print quando for utilizado
    VI.iii. Ao utilizar o metodo for não é necessario utilizar nenhum comando read para ler o arquivo

    VII.    O método apresentado abaixo não é o método mais pythonico de se abrir um arquivo, alguma pessoas
            utilizam os blocos try e finally, entretanto mesmo funcionando não é a melhor opção.
    VII.I   A melhor forma para abrir um arquivo de forma mais pythonica é utiizar gerenciadores de contexto
            "with" e "as". A grande vantagem deste método é a não necessidade da utilização de close, tendo
            esse processi finalizado de forma automatica

    VIII.   No método open conforme indica o link no inicio desse documento existe o parametro apenas de leitura
            definido pela letra 'r'

    IX.     Quando se abre um arquivo ja criado e com conteudo é importante tomar cuidado na escrita de mais
            conteúdo sobre ele pois pode acarretar no apagamento do conteúdo já existente. Para evitar isso
            existe o método de abertura 'a' append que ao abrir move o cursor para o fim do arquivo evitando
            aparamento de conteudo

    X.      Para apagar um arquivo utiliza-se o pacote os com o método remove(). O metodo recebe como parametro
            o nome do arquivo

    XI.     Os métodos de abertura de arquivos podem ser utilizados em conjunto como ao longo deste arquivo como
            foi apresentado 'a+', 'w+' e etc

    XII.    É possivel criar json com o modulo json e o metodo dumps() que recebe dois parametros, o primeiro
            é um dicionário com as informações e um segundo parametro indicando se a identação do JSON esta
            ativa ou não (atributo nomeado)

    XIII.   Convertendo JSON para dicionário


'''
import os
import json

print('#1')
file = open('abc.txt', 'w+')

print('#2\n')
file.write('Linha_1\n')
file.write('Linha_2\n')
file.write('Linha_3\n')


print('#4\n')
file.seek(0,0)

print('#5 \n')
print(file.read())

print('#6\n')
print(file.readline())

print('#6.1\n')
file.seek(0,0)
print(file.readlines())

print('#6.2\n')
file.seek(0,0)
for x in file.readlines():
    print(x, end='')

print('#6.3\n')
file.seek(0,0)
for x in file.readlines():
    print(x, end='')

print('#3\n')
file.close()

print("\n7.1")
with open('cde.txt', 'w+') as file2:
    file2.write('Linha3\n')
    file2.write('Linha4\n')
    file2.write('Linha5\n')

    file2.seek(0)
    print(file2.read())

print('#\n8')
with open('cde.txt', 'r') as reader:
    print(reader.read())

print('\n#9')
with open('cde.txt', 'a+') as file:
    file.write('ouutra linhaa\n')
    file.seek(0)
    print(file.read())

print('\n10')
os.remove('abc.txt')


print('\n12')
d1 = {

        'Pessoa1': {
            'nome': 'Tarcisio',
            'idade': 32,
        },

        'Pessoa2': {
            'nome': 'Bryan',
            'idade': 32,
        },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print('\n13')
with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

print(d1_json)


