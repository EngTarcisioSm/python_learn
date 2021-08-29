'''
Sobreposição de métodos na Herança 

     i.        Uma classe filha por ser herdada por outra classe tornando essa classe mais especifica ainda 
     ii.       Quando uma classe herda atributos e métodos de outra classe, ocorre da seguinte forma. O python busca o atributo e método na classe, caso ele não ache ele busca na classe que a classe atual herda, caso não seja achado ele busca a proxima super classe caso haja 
     iii.      É possivel que uma classe filha sobrescreva algum atributo ou método que ela herda 
     iv.       Ao sobrepor um método de uma classe mãe em uma classe filha toda a logica do método da classe mãe não é utilizado, para fazer uso da lógica da do método da classe mãe e sendo incrementado na classe filha utiliza-se super().nome_metodo()
     v.        Caso o método que se queira utilizar a logica é de uma classe que a classe mãe herda utiliza-se Nome_Classe.nome_metodo(self)

     vi.       Em uma classe filha caso seja necessário sobrepor o construtor para incremento é possivel fazer o mesmo que o de métodos, utilizando super().__init__(self, atributos) ou Pessoa.__init__(self, atributos)
               Utiliza-se super() caso o construtor esteja na proxima classe mãe, caso não utilizar/especificar o nome da classe 
'''
from classes import Cliente, ClienteVIP

c1 = Cliente(nome='Tarcísio', idade=32)
c2 = ClienteVIP(nome='Bryan', idade=5, sobrenome='William Vasconcelos de Melo')

print(c1.nome)
c1.comprar()
c1.falar()
print()

print(c2.nome)
c2.comprar()
c2.falar()
print()