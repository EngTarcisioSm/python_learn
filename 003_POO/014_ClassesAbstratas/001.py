'''
CLASSES ABSTRATAS

     i.        O conceito de classe abstrata ja foi utilizado anteriormente ao se utilizar uma classe mais generica ser herdada por uma classa mais especializada 
     ii.       Nem sempre deseja-se que a classe genérica possa ser instanciada 
     iii.      Uma classe abstrata pode ter métodos concretos e métodos abstratos 
     iv.       Métodos concretos são métodos normais que funcionam e podem ser herdados 
     v.        Método abstrato é um método que não tem corpo, se cria o método como abstrato sem nenhum código a ser executado, e com isso obriga as classes filhas que herdarem essa classe a implementar esse método bem como a logica dele 
     vi.       Para usar uma classe abstrata é necessário importar o módulo abc (abstract class) e importar dentro dela ABC e o decorado abstractmethod
               from abc import ABC, abstractmethod
     vii.      Toda classe abstrata deve herdar de ABC
     viii.     Para que a classe abstrata não poder ser instanciada ela deve ter ao menos um método abstrato, sendo que feito isso a classe não pode ser instanciada e suas classes filhas são obrigadas a implementar o método abstrato dentro de sí, o não cumprimento acarreta em erro 
'''
from abc import ABC, abstractmethod 
from classes.contapoupanca import ContaPoupanca
from classes.conta_corrente import ContaCorrente


class A(ABC):

     @abstractmethod
     def falar(self):
          pass

class B(A):

     def falar(self):
          print('Eiiiiiiita....')


a = B()
a.falar()
print()

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

print()

cc = ContaCorrente(1111, 3333, 0, 500)

cc.depositar(100)

cc.sacar(100)
cc.sacar(100)
cc.sacar(100)
cc.sacar(100)
cc.sacar(100)
cc.sacar(100)
cc.sacar(100)
