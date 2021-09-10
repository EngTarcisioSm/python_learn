"""Código referente ao desafio de POO

    Conteúdo do desafio descrito no arquivo main.py

"""
from abc import ABC, abstractmethod
from desafio_conta import Conta, ContaCorrente, ContaPoupanca

class Pessoa(ABC):
    """Classe Pessoa

    :param nome: Nome da pessoa  
    :type texto : str

    :return: nenhum
    :rtype: None

    :raises ValueError: nenhum
    :raises TypeError: nenhum

    """
    def __init__(self, nome:str, idade:int) -> None:
        self.nome : str = nome
        self.idade: int = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, new_name:str)->None:
        self._nome: str = new_name
    
    @property
    def idade(self)->int:
        return self._idade
    
    @idade.setter
    def idade(self, new_idade:int)->None:
        self._idade:int = new_idade
    
    @abstractmethod
    def _(self):
        pass

    def __str__(self)->str:
        return f'Nome: {self._nome} Idade:{self._idade}'



class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int, conta_cliente: Conta) -> None:
        super().__init__(nome, idade)
        self.__conta_cliente = conta_cliente

    @property
    def conta_cliente(self):
        return self.__conta_cliente
    
    @conta_cliente.setter
    def conta_cliente(self, conta):
        pass
    
    def _(self):
        pass

    def __str__(self) -> str:
        return f'Nome: {self.nome} | Idade: {self._idade} | Ag: {self.conta_cliente.agencia} | Conta: {self.conta_cliente.conta} | Saldo: {self.conta_cliente.saldo}'


    

