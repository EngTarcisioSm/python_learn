from abc import ABC, abstractmethod


class Conta(ABC):
    
    def __init__(self, agencia:int, num_conta:int) -> None:
        self.__agencia:int = agencia
        self.__num_conta:int = num_conta
        self.__saldo:int = 0
    
    @abstractmethod
    def sacar(self, valor:int)->str:
        pass
    
    def depositar(self,valor:int)->None:
        self.saldo += valor

    @property
    def agencia(self)->int:
        return self.__agencia
    
    @property
    def conta(self)->int:
        return self.__num_conta
    
    @property
    def saldo(self)->int:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor)->None:
        self.__saldo = valor
    
    def __str__(self)->str:
        return f'Ag.:{self.__agencia} | Cc.:{self.__agencia}'



class ContaPoupanca(Conta):

    def sacar(self, valor:int)->str:
        if self.saldo > valor:
            self.saldo += -valor
            return f'Saque de R$ {valor} efetuado com sucesso'
        return f'Não foi possivel efetuar o saque de R$ {valor}'
        
    

class ContaCorrente(Conta):

    def __init__(self, agencia: int, num_conta: int, limite:int) -> None:
        super().__init__(agencia, num_conta)
        self.__limite = limite
        self.__limite_fix = limite

    @property
    def limite(self)->str:
        return self.__limite

    @limite.setter
    def limite(self, valor)->None:
        self.__limite = valor

    def depositar(self, valor: int) -> None:
        self.saldo += valor
        if self.limite <= self.__limite_fix:
            if(self.limite + valor) > self.__limite_fix:
                self.limite == self.__limite_fix
            else:
                self.limite += valor


    def sacar(self, valor)->str:
        if self.saldo >= valor:
            self.saldo +=  -valor
        else:
            if (self.saldo + self.limite) >= 0 and (self.saldo + self.limite) >= valor:
                self.saldo -= valor
                self.limite += self.saldo
            else:
                if self.limite > 0 and self.limite > valor:
                    self.limite -= valor
                    self.saldo += -valor
                else:
                    return f'Saldo e/ou limite insuficiente'
        return f'$ {valor} sacado com sucesso'
            
    def __str__(self)->str:
        return f'Ag.:{self.agencia} | Cc.:{self.conta} | Saldo.:$ {self.saldo} | Limite.:$ {self.limite}'








