"""
Exercicio com abstração, herança, encapsulamento e Polimorfismo 

Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente ) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas 


dicas:

OK - Criar class Clinete que herda da classe Pessoa (herança)
    OK - pessoa tem nome e idade (com getters)
    OK - Cliente Tem conta (agregação da classe ContaCorrente ou ContaPoupanca)

OK - Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    OK - ContaCorrente deve ter um limite extra
    OK - Contas tem agencias, numero da conta e saldo 
    OK - Contas devem ter método para deposito
    OK - Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo -as subclasses que implementam o metodo sacar)

OK - Criar classe Banco para Agregar classes de clientes e de contas (Agregação)
Vanco será responsavel autenticar o cliente e as contas da seguinte maneira 
    OK - Banco tem contas e clientes(Agregação)
        OK - * checar se a agencia é daquele banco
        OK - * checar se o cliente é daquele banco
        OK - * Checar se a conta pe daquele banco 
OK - Só será possivel sacar se passar na autenticação do banco (descrita acima )


"""
from desafio_banco import Banco
from desafio_pessoa import Cliente
from desafio_conta import ContaPoupanca, ContaCorrente


Bradesco = Banco(1993)


cliente1 = Cliente(nome="Bryan", idade=5, conta_cliente=ContaCorrente(1993,8,5000))
cliente2 = Cliente(nome="Tarcisio", idade=32, conta_cliente=ContaCorrente(1998,1,5000))
cliente3 = Cliente(nome="Alipio", idade=60, conta_cliente=ContaCorrente(1993,100,5000))
cliente4 = Cliente(nome="Janete", idade=56, conta_cliente=ContaCorrente(1993,4,5000))
cliente5 = Cliente(nome="Sofia", idade=0, conta_cliente=ContaPoupanca(1993,2))

Bradesco.add_clientes(cliente1)
Bradesco.add_clientes(cliente2)
Bradesco.add_clientes(cliente3)
Bradesco.add_clientes(cliente4)
Bradesco.add_clientes(cliente5)


x = Bradesco.saqueCliente("Bryan", 1000)
print(x)

x = Bradesco.saqueCliente("Tarcisio", 1000)
print(x)

Bradesco.view_clientes()