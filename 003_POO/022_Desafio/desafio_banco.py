from desafio_conta import Conta, ContaCorrente, ContaPoupanca
from desafio_pessoa import Pessoa, Cliente

class Banco():

    def __init__(self) -> None:
        self.__clientes = []

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def cliente(self, cliente):
        #self.__clientes = cliente
        pass

    def add_clientes(self, cliente:Cliente)-> None:
        self.clientes.append(cliente)

    def view_clientes(self):
        for cli in self.clientes:
            print(cli)

Bradesco = Banco()


cliente1 = Cliente(nome="Bryan", idade=5, conta_cliente=ContaCorrente(1993,1,5000))

Bradesco.add_clientes(cliente1)

Bradesco.view_clientes()