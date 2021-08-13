'''
- Dicionários
    - I.    Similares a listas
    - II.   Diferença entre listas e dicionários: listas possuem indices, enquanto dicionŕios possuem chaves
    no lugar do indice
    - III.  Estrutura
    dicionario = dict('chave1' = valor,...)
    - IV.   Os valores são acessados artraves da chave
    - V.    É possivel criar dicionarios com dic() ou com {}, caso se utilize a ultima opção ao a cada chave
    deve ser inserida da seguinte forma 'chave': valor
    - VI.   Se utilizar {} para criar um dicionário, caso exista chaves com valores repetidos, ao se criar
    ficara apenas uma das chaves com o valor da ultima inserção
    - VII.  Chaves dentro de dicionários necessitam de ser unicos
    -VIII.  Para acessar qualquer valor de um dicionário, basta inserir o nome da variavel e entre chaves
    o nome da chave
    - IX.   Chaves podem ser strings, numeros interios e tuplas
    - X.    Quando se tenta acessar uma chave de um dicionário e este não existe o programa quebra, para
    evitar isso é possivel com dicionario.get(vaor_chave), desta forma caso a chave não exista apenas
    retornará none
    - XI.   Para atualizar o valor de uma chave basta colocar o nome da chave entre chaves seguido do
    simbolo de atribuição e em seguida o valor
    - XII.  Para inserir uma nova chave com valor é possivel fazer também com o mesmo método anterior pois
    caso a chave não exista ela é criada ou utilizar.update({chave:valor}), a função update recebe o
    como parametro um dicionário
    -XIII.  Para remover uma chave com o seu respectivo valor da lista utiliza-se
    del nome_dicionario['nome_chave']
    - XIV.  É possivel verificar a existencia de uma chave dentro de um dicionário utilizando 'in'
    com retorno booleano (chave in dicionario) é possivel também utilizar (chave in dicionario.keys())
    - XV.   Da mesma forma que é possivel pesquisar chaves é possivel pesquisar valores dentro do dicionario
    com: in e  .values() -> (valor in d1.values())
    - XVI.  Para saber a quantidade de pares de valores que existem utiliza-se 'len()
    - XVII. É possivel iterar sobre um dicionário com for
            for in nome_dicionario: -> Retorna todos as chaves do dicionatário
            for in nome.values()
    - XVIII. quando se vai copiar o valor de um dicionário para um outro, não se  deve fazer unicamente com o simbolo
    de atribuição, pois no python isso não funciona como outras linguagens funcionando mais como um ponteiro, ou seja
    alterações na segunda variávil, altera a primeira para que isso não ocorra utilizar x = y.copy(), efetuará uma cópia
    fraca, ou seja caso o dicionário copiado tenha dicionários internos eles poderam ser alterados para evitar isso
    existe uma bilbioteca especifica que trata copia profunda 'import copy', utilizando o metodo copy.deepcopy

    - XIX.  É possivel efetuar o casting (conversão) para dicionários com dict(), entretanto a estrutura da lista ou
    tupla... deve ser similar ao de um dicionário com elementos internos em pares (listas de listas, tuplas de tuplas)
    que se assemelhe a uma chave valor

    - XX.   Existe a função pop e popitem dentro de dicionário, entretanto se comporta de forma diferente das listas

    - XXI.  dicionario.pop(chave): elimina chave passada como parametro

    - XXII. dicionario.popitem(): Remove o ultimo item do dicionario

    -XXIII. dicionario.update(dicionario2): inclui o dicionario2 dentro do dicionario1

'''
# I a IV
print('# I a IV')
d1 = dict(chave1='Valor 1 de chave', chave2= '324')
d1['nova_chave'] = 'Novo valor de chave'
print(d1['chave1'])
print(d1)

# V
print('# V')
d2 = {'nome1':'Tarcísio', 'nome2':'Bryan '}
print(d2)

#VI e VII
print('# VI e VII')
d3 = {'nome1':'Tarcísio', 'nome2':'Bryan', 'nome2':'William', 'nome2':'Vasconcelos'}
print(d3)

# IX
print('# IX')
d4 = {'str':'valor', 123: 'Outro_Valor', (1,2,3,4):'Mais um valor'}
print(d4)

# X
print('# X')
print(d4.get(123))
print(d4.get('342fvbsfd'))

# XI
print('# XI')
d4['str'] = 'valor novo denovo '
print(d4)

# XII
print('# XII')
d4.update({'novo_Nome':'Bryan William Vasconcelos de Melo'})
d4['nome_Novo'] = 'Tarcísio Souza de Melo'
print(d4)

# XIII
print('# XIII')
del d4['nome_Novo']
print(d4)

# XIV
print('# XIV')
print('novo_Nome' in d4)
print('novo_Nome' in d4.keys())

# XV
print('# XV')
print('Outro_Valor' in d4.values())

# XVI
print('# XVI')
print(len(d4))

# XVII
print('# XVII')
for k in d4:
    print(k)

for k in d4.values():
    print(k)

clientes = {
    'cliente1' : {
        'nome': 'Luiz',
        'sobrenome':'Otávio',
    },
   ' cliente2' : {
       'nome': 'João',
       'sobrenome' :'Moreira',
   },
}
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} {dados_v}')

# XVIII
print('# XVIII')
d5 = {1: 'a',2: 'b',3: 'c'}
d6 = d5
d6[1] = 'z'
print(d5)
print(d6)
d7 = d6.copy()
d7[1] = 'T'
print(d6)
print(d7)
d6[2] = 'Q'
print(d6)
print(d7)

# XIX
print('# XIX')
lista = [
    ['c1', 10],
    ['c2', 20],
    ['c3', 30],
]

tupla = (
    ('c1', 40),
    ('c2', 50),
    ('c3', 60),
)

d8 = dict(lista)
d9 = dict(tupla)
print(d8)
print(d9)

# XXI
print('# XXI')
d9.pop('c3')
print(d9)

# XXII
print('# XXII')
d8.popitem()
print(d8)

#XXIII
print('XXIII')
d10 = {
    1: 2,
    2: 3,
    3: 4,
}
d11 = {
    'a': 'b',
    'b': 'c',
    'c': 'd',
}

d10.update(d11)
print(d10)