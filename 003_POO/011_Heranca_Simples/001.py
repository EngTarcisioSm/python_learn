'''
RELAÇÕES DE CLASSES PYTHON 

     i.
               Associação: Uma classe -> usa outra classe
               Agregação : Uma classe -> tem outra classe
               Composição: Uma classe -> é dona de outras classes
               Herança   : Uma classe -> é uma outra classe 

     ii.       Um bom codigo é aquele onde não existe repetição de código 

     iii.      Para se utilizar Herança após o nome da classe utiliza parentesis e coloca-se o nome da classe a qual a classe atual herdará 

     iv.       Ao uma classe herdar de outra classe ela herdará todos os atributos e métodos da classe mãe 

     v.        Classes que herdam são chamadas de classes filhas ou subclasses, classe que outras classes herdam dela são chamadas de superclasse ou classe mãe 

     vi.       variavel = self.__class__.__name__  retorna o nome da classe do objeto 
     
     vii.      Classes filhas podem ter seus métodos e atributos proprios 

     viii.     Herança funciona de cima para baixo, ou seja, a classe mãe tem os métodos e atributos mais genérios que são herdados pelas classes filhas, as classes filhas são mais especializadas podendo possuir métodos e atributos proprios e aqueles herdados da classe mãe 
'''
from classes import Aluno, Cliente

c1 = Cliente(nome='Tarcísio', idade=32)
a1 = Aluno(nome='Bryan', idade=5)

print(c1.nome)
c1.falar()
c1.comprar()
print()

print(a1.nome)
a1.falar()
a1.estudar()

