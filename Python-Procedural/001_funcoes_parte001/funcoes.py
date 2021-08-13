'''
FUnções - Parte 1
    i - Em python é possivel definir as proprias funções utilizando a palavra reservada
    def
        i.i - após utilizar def, deve-se dar um nome para função o qual não pode ser uma palavra
        reservada da linguagem
        i.ii - após o nome da função existem um abrir e fechar de parentesis e dentro deste pode ser
        inserido parametros que são variaveis disponiveis na função
        i.iii - após o abrir e fechar de parentesis vem o dois pontos. após isso com a devida identação,
        que é o que define o escopo em python pode ser inserido comandos em linguagem python
        i.iv - def nome_funcao():

    ii. Funções são criada para não se repetir código

    iii. entre os parentesis da função, ela pode receber parametro
        iii.i - def funcao(valor): -> valor é um parametro, funcao(1234) -> 1234 é um atributo
        iii.ii - não é necessario se definir tipo em um parametro

    iv - uma função que possui parametros, quando utilizada tem de ter valor para cada parametro
    definido em sua criação (a não ser que possua valor default) gerando erro caso não utilizado
        iv.i - Pode receber mais de um parametro

    v - é possivel setar valores pré configurados para o caso do usuario da função não colocar
    ou não querer colocar
        v.i - def funcao(par1 = 0, par2 = 1): desta forma caso não seja colocado algum valor
        os valores defaut serão assumidos, e se for colocado substituirá o valor default
        v.ii - caso queira colocar apenas um dos atributos entre parentesis o atributo tem de ser
        nomeado seguido do simbolo de atribuição e seu valor
'''
# (i)
def funcao():
    print('Hello World...')

funcao()
funcao()
funcao()
funcao()

#(iii)
def funcao2(msg):
    print(msg)

funcao2('Olá mundo')
funcao2('Adeus mundo cruel ')

def func3(nome, msg):
    print(f'{nome}, {msg}')

func3('Tarcísio', 'Bom dia!')

# (v):
def func4(nome='usuario', msg = 'sem mensagem'):
    print(f'{nome}, {msg}')

func4()
func4('tarcisio','qualé')
func4(msg='kkkkkkkkkkkkkkkkk')