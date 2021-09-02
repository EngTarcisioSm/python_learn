from abc import ABC, abstractmethod

class Conta(ABC):

     def __init__(self, agencia, conta, saldo):
          self._agencia = agencia
          self._conta = conta
          self._saldo = saldo 

     @property
     def agencia(self):
          return self._agencia
     
     @property
     def conta(self):
          return self._conta

     @property
     def saldo(self):
          return self._saldo

     @saldo.setter
     def saldo(self, valor):
          # verifica se o a variavel valor contem um objeto do tipo int ou float caso não o tenha executa o if 
          if not isinstance(valor, (int, float)):
               raise ValueError("SAldo precisa ser numérico")
          self._saldo = valor

     def depositar(self, valor):
          # verifica se o a variavel valor contem um objeto do tipo int ou float caso não o tenha executa o if 
          if not isinstance(valor, (int, float)):
               raise ValueError("SAldo precisa ser numérico")
          self._saldo += valor
          self.detalhes()

     def detalhes(self):
          print(f'Ag: {self.agencia}', end=' ')
          print(f'C:{self.conta}', end=' ')
          print(f'$:{self.saldo}')

     @abstractmethod
     # o método sacar deve ser implementado na classe que herda pois há diferentes tipos de saque nas diversas contas possiveis 
     def sacar(self, valor):
          pass