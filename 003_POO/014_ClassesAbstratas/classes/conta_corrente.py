from classes.conta import Conta

class ContaCorrente(Conta):

     def __init__(self, agencia, conta, saldo, limite=100):
          super().__init__(agencia, conta, saldo)
          self._limite = limite

     def sacar(self, valor):
          # verifica se o a variavel valor contem um objeto do tipo int ou float caso não o tenha executa o if 
          if not isinstance(valor, (int, float)):
               raise ValueError("SAldo precisa ser numérico")
          if (self.saldo + self._limite) < valor:
               print('Saldo insuficiente')  
               return
          self.saldo -= valor
          self.detalhes()

     @property
     def limite(self):
          return self._limite