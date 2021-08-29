

class Pessoa:

     def __init__(self, nome, idade):
          self.nome = nome
          self.idade = idade
          self.nome_classe = self.__class__.__name__

     def falar(self):
          print(f'{self.nome_classe} esta falando...')


class Cliente(Pessoa):

     def falar(self):
          print(f'{self.nome_classe} {self.nome} esta falando')

     def comprar(self):
          print(f'{self.nome_classe} {self.nome} esta comprando')


class ClienteVIP(Cliente):

     def __init__(self, nome, idade, sobrenome=None):
          Pessoa.__init__(self, nome, idade)
          self.sobrenome = sobrenome 

     def falar(self):
          Pessoa.falar(self)
          print(f'{self.nome} {self.sobrenome} Oba Oba...')

     def comprar(self):
          
          super().comprar()
          print(f'{self.nome} segura bebida que pisca')