'''
    - I.        POO:  Paradigma de programação que tenta retratar coisas do mundo real como objetos dentro
                do programa em desenvolvimento
    - II.       Uma classe dentro da linguagem nada mais é do que um molde
    - III.      Para se criar uma classe utiliza-se a palavra reservada class seguido do nome da classe
    - IV.       Classes iniciam com a primeira letra de seu nome em maiusculo terminando com dois pontos
                Caso o nome seja composto os dois nomes são maiusculos a primeira letra "PessoaPassaro"
    - V.        Para criar um objeto da classe é necessário instanciar o objeto vindo de um mesmo objeto
    - VI.       No exemplo anterior tanto p1 como p2 são pessoas entretanto os objetos são instanciados
                em posições de memoria diferentes. Mesmo molde para criar objetos, entretanto alocados em
                posições de memória diferentes
    - VII.      Classes podem possuir variaveis internas, neste contexto são chamadas de atributos da
                classe

    - VIII.     Depois de instanciado um objeto é possivel colocar em código atributos para este objeto
                "mais isso não é comum de ser feito

    - IX.       Método é uma função que pertence a uma classe. Quando uma função esta dentro de uma classe
                ela se torna um método de uma classe

    - X.        Métodos tem como atributo a palavra reservada self para indicar se tratar daquela classe
                def nome_metodo(self):
                    ...
    - XI.       Daqui para baixo tudo esta no arquivo Pessoa2

    - XII.      Existe um método especial chamado __init__ que tem por função inicializar a classe

    - XIII.     Métodos de classe inicluindo o método especial __init__ podem possui atributos entretanto
                a palavra reservada self, deve ser o primeiro atributo de todos métodos por convenção

    - XIV.      __init__ permite ao instanciar um objeto inicia-lo com valores

    - XV.       Para que um atributo colocado na instanciação do objeto pertença aquele objeto ele deve
                ser associado a self -> self.nome_atributo

    - XVI.      Instanciando um objeto e ja passando atributos

    - XVII.     Variáveis criadas dentro de métodos inclusive o __init__ sem o prefixo self. só são
                válidos dentro daquele método, enquanto self.nome_variavel possui escopo global dentro
                do objeto

    - XVIII.    Como informado acima atributos com self. com prefixo ficam disponiveis dentro de todos
                os métodos dentro do objeto

    - XIV.      métodos podem receber atributos durante o processo de execução
                - como ocorre com o método falar de pessoa

    - XV.       Os objetos são independentes entre si

    - XVI.      Classes podem ter atributos próprios não listados dentro de algum método. Para continuar
                usando o atributo dentro de uma classe é necessário continuar utilizando self antes do nome

    - XVII.     convenção de classe utilizada no python
                PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado
                para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a
                convenção utilizada para classes em Python;


'''
from Pessoa2 import Pessoa as ps

# II, III, IV
class Pessoa:
    pass

# V
p1 = Pessoa()
p2 = Pessoa()

# VI
print(p1)
print(p2)

# VIII
p1.nome = 'Tarcísio'
p2.nome = 'Bryan'
print(p1.nome)
print(p2.nome)

p3 = ps(nome='Tarcísio',idade=32)
p4 = ps(nome='Bryan', idade= 5, falando=True)
print(p3.nome, p3.idade, p3.fala())

# XIV
p3.fala('comida')
p3.fala('comida')
p4.fala('peidar')
p4.fala('peidar')

#XVi
print(p4.ano_atual)
print(p4.get_ano_nascimento())