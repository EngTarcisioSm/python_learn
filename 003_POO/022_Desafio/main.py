"""
Exercicio com abstração, herança, encapsulamento e Polimorfismo 

Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente ) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas 


dicas:

Criar class Clinete que herda da classe Pessoa (herança)
    pessoa tem nome e idade (com getters)
    Cliente Tem conta (agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agencias, numero da conta e saldo 
    Contas devem ter método para deposito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo -as subclasses que implementam o metodo sacar)

Criar classe Banco para Agregar classes de clientes e de contas (Agregação)
Vanco será responsavel autenticar o cliente e as contas da seguinte maneira 
    Banco tem contas e clientes(Agregação)
    * checar se a agencia é daquele banco
    * checar se o cliente é daquele banco
    * Checar se a conta pe daquele banco 
Só será possivel sacar se passar na autenticação do banco (descrita acima )


"""