"""
O que são Dataclasses

    O módulo Dataclasses dornece um decorador e funções para criar automaticamente métodos como, __ini__(), __repr__(), __eq__() etc em classes definidas pelo usuário.
    Basicamente, dataclasses são syntax sugar para criar classes normais
    Foi escrito originalmente na PEP 557
    DOcumentação oficial:
        https://docs.python.org/pt-br/3/library/dataclasses.html 
"""
""" 
    I.      Faz com que os métodos acima citados não necessitem de ser criados, a propria classe dataclasses ja faz isso
    
    II.     __repr() já criado
    
    III.    É possivel criar metodos (inclusive com @property)
    
    IV.     Caso seja necessário é possivel desabilitar o __init__() que dataclasses usa ou utilizar uma função que é executada logo em seguida de de init chamada de __post_init__()
    
    V.      O método __eq__() de comparação ja esta criado 
    
    VI.     Para desabilitar algo basta que ao lado de @dataclass, se abra e feche parentesis, se coloque o metodo a ser desabilitado simbolo de atriuição seguido de False
        @dataclass(eq=False, repr=False, order=False, init=False)
        frozen = torna a classe imutavel (vem como false por padrão)
        order = permite que a classe se torne ordenavel atravel de sorted
    
    VII.    É possivel em __post_init()__ criar logicas, como por exemplo verificar se um valor inserido é de um determinado tipo especifico. Mesmo sinalizando ao python que um valor de entrada é de determinado tipo, ele não gera nenhum erro caso o usuário opte por não inseri-lo

    VIII.   É possivel omitir atributos de __repr()__ com field
            Após inserido esse módulo basta após o tipo do atributo inserir field(repr=False)

    IX.     É possivel converter um objeto em um dicionário ou tupla com asdict ou astuple 

    X.      Não funciona muito bem Herança quando esta tiver que trabalhar com __init__

    parei em 12:30
"""

#I e VIII e IX
from dataclasses import dataclass, field, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    #VIII
    sobrenome: str = field(repr=False)
    #IV
    def __post_init__(self):
        #VII
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo invalido {type(self.nome)} != str em {self}'
            )
        self.nome_completo = f'{self.nome} {self.sobrenome}'
    #III
    #@property
    #def nome_completo(self):
    #    return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Tarcisio', 'Souza de Melo')

#II
print(p1)
print(p1.nome_completo)

#V
p2 = Pessoa("Bryan", 'William Vasconcelos de Melo')
print(p1 == p2)

#IX. 
print(asdict(p2))
print(astuple(p2))