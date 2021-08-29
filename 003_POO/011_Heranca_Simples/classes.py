
'''
     i.   Toda pessoa possui nome e idade 
     ii.  Todo cliente possui nome e idade ou seja são pessoas, ou seja, Cliente herda de Pessoa
     iii. Todo Aluno possui nome e idade ou seja, Aluno é uma pessoa, Herdando de Pessoa 

'''

class Pessoa:
     def __init__(self, nome, idade):
          self.nome = nome 
          self.idade = idade
          self.nome_classe = self.__class__.__name__

     def falar(self):
          print(f'{self.nome_classe} falando')

class Cliente(Pessoa):
     def comprar(self):
          print(f'{self.nome} comprando...')

class Aluno(Pessoa):
     def estudar(self):
          print(f'{self.nome} estudando...')