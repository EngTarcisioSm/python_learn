from desafio_conta import Conta, ContaCorrente, ContaPoupanca
from desafio_pessoa import Pessoa, Cliente

class Banco():
    """Classe Banco
        Classe responsavel por criar um banco para armazenar clientes com funcionalidade de sacar
    """

    def __init__(self, agencia:int) -> None:
        self.__clientes = []
        self.__agencia = agencia

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def cliente(self, cliente):
        #self.__clientes = cliente
        pass

    @property
    def agencia(self):
        return self.__agencia


    def add_clientes(self, cliente:Cliente)-> None:
        self.clientes.append(cliente)

    def view_clientes(self):
        for cli in self.clientes:
            print(cli)

    def saqueCliente(self, nome_cliente:str, valor_saque:float)->str:
        """Método sacar

        Args:
            nome_cliente (str): [Nome do cliente do banco]
            valor_saque (float): [valor que se deseja sacar]

        Returns:
            str: [retorna string indicando sucesso ou falha no saque]
        """
 
        for cliente in self.clientes:
            if cliente.nome == nome_cliente:
                if cliente.conta_cliente.agencia == self.agencia:
                    cliente.conta_cliente.sacar(valor_saque)
                    return f'Saque realizado com sucesso'
                else:
                    return f'Cliente {cliente.nome} com numero de agencia divergente'
    


        return f'{nome_cliente} não é cliente do banco'
        


