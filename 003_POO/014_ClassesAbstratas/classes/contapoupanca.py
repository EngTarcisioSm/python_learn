from classes.conta import Conta
     
class ContaPoupanca(Conta):     
     
     def sacar(self, valor):
          # verifica se o a variavel valor contem um objeto do tipo int ou float caso não o tenha executa o if 
          if not isinstance(valor, (int, float)):
               raise ValueError("SAldo precisa ser numérico")
          if self.saldo < valor:
               print('Saldo insuficiente')  
               return
          self.saldo -= valor
          self.detalhes()



