'''
VARIAVEIS (ATRIBUTOS) DE CLASSES 

     - i.      Variáveis de classe pertencem a classe não as instancias da classe, entretanto podem ser acessadas pelos objetos tento o mesmo valor em qualquer objeto criado 
     - ii.     É possivel chamar direto um atributo de classe pela propria classe
     - iii.    É importante destacar que os atributos de classe não estão presentes nas instancias, quando é feito o acesso pela instancia, o python após ver que o atributo não existe na instancia é buscado na classe 
     - iv.     É possivel alterar atributos de classes tanto na classe, alterando o valor lido nas instancias também, entretanto quando esse valor é alterado na instancia o que ocorre é que é criado um atributo no objeto e não se altera nos demais nem na classe 
     - v.      Se uma classe tem um atributo de classe com o mesmo nome que um atributo de instancia, o atributo de classe só ficara disponivel para a classe, na instancia fica valendo aquela da instancia 

'''

class A:
     att_de_classe = 123456

a1 = A()
a2 = A()

#i
print(a1.att_de_classe)
print(a2.att_de_classe)

#ii
print(A.att_de_classe)

# iii
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

#iv
A.att_de_classe = 'mudou'
print(a1.att_de_classe)
print(a2.att_de_classe)
print(A.att_de_classe)

a1.att_de_classe = 'mudou nada'
print(a1.att_de_classe)
print(a2.att_de_classe)
print(A.att_de_classe)
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

#v
class B:
     atributo = 'você'

     def __init__(self):
          self.atributo = 'Eu'

b1 = B()
b2 = B()
print(B.atributo)
print(b1.atributo)
print(b2.atributo)