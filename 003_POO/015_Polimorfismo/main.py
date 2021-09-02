'''
POLIMORFISMO

    i.      É o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes. Entende-se por mesma assinatura mesma quantidade e tipo de parâmetros 

    ii.     Polimorfismo ja foi utilizado em 014_ClassesAbstratas quando a classe abstrata Conta obriga as classes derivadas a implementar o método sacar, cada um a sua forma mesmo recebendo os mesmos parametros 

    iii.    Exemplo de polimorfismo

    iv.     Python só admite o polimorfismo de sobreposição, existe também o polimorfismo de sobrecarga que o pyhton não suporta 
'''
#iii
from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B esta falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C esta falando {msg.upper()}')


b = B()
c = C()

b.fala('blastóise')
c.fala('blastóise')
