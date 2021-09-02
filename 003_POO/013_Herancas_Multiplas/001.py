'''

    i.      Na Herança multiplica uma classe herda de duas ou mais outras classes;
    ii.     Se uma classe tem herança multipla e as classes mães possuem métodos com nomes identicos, o que ocorrerá é que a classe física herdará da primeira classe mãe primeiro 
        class NovaClasse(X, Y):
        -Herdará primeiro de X e depois de Y
    iii.    Quando se vai utilizar herança multipla é comum se utilizar classes mixin, ou seja, classes que não foram criadas para ser instanciadas diretamente, usada para dar funcionalidade a classe que a ira herdar  
    iv.     Exemplo de herança multipla 
    v.      Quando um método não utiliza nenhum parametro da classe é possivel torna-la estatica removendo o self de seus atributos e colocando um decorador "@staticmethod"
'''
from smartphone import Smartphone

class A:
    def fala(self):
        print('Falando... Estou em A')

class B(A):
    def fala(self):
        print('Falando ... Estou em B')

class C(A):
    def fala(self):
        print('Falando ...Estou em C')

# ii
class D(B,C):
    pass

# ii
class E(B,C):
    def fala(self):
        print('Falando... Estou em E')

d = D()
d.fala()
e = E()
e.fala()

#iv
print('\n\n')
smartphone = Smartphone('Pocophone F2 Pro')
smartphone.ligar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
