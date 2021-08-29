'''
     i.   Como um cliente pode ter vários endereços é bom especificar uma classe endereços
'''


class Cliente:

     def __init__(self, nome, idade):
          self.nome = nome 
          self.idade = idade
          self.endereco = []

     def insere_endereco(self, cidade, estado):
          # É instanciado um objeto da classe Endereco dentro da classe cliente para cada chamada da função insere_endereco
          self.endereco.append(Endereco(cidade, estado))

     def lista_enderecos(self):
          for endereco in self.endereco:
               print(endereco.cidade, endereco.estado)
     
     def __del__(self):
          print(f'{self.nome} foi apagado!')


class Endereco:
     
     def __init__(self, cidade, estado):
          self.cidade = cidade
          self.estado = estado

     def __del__(self):
          print(f'{self.cidade} / {self.estado} foi apagado!')