'''
    - Métodos Getters e Setters em POO (Python)

    I.      POO da linguagem pyhton é um pouco diferente das outras linguagens de programação
    II.     Para dar mais estabilidade nos dados que uma classe recebe existem os metodos getters e
            setters
            Como o proprio nome ja informa, um getter fornece um valor enquanto um setter, configura
            um valor
    III.    Quando utilizado um método getter, ao invez de fazer o acesso direto a um atributo da
            classe, uma função fara a interface de acesso a este valor
            Por padronização ao retornar o atributo desejado é inserido um underline na frente do nome
            do atributo
    IV.     Por sua vez o metodo setter faz a interface quando vai ser configurado um atributo de uma
            interface.
    V.      O método getter utiliza como decorador "@property" enquanto o metodo setter utiliza como
            decorador "@nome_atributo.setter
    VI.     Tanto o getter como o setter são metodos e levam o nome do atributo





parei em 7:22
'''

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco *(percentual/100))

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, new_preco):
        self._preco = new_preco


p1 = Produto(nome='Camisa', preco=50)
p1.desconto(10)
print(p1.preco)

p2 = Produto(nome='caneca', preco=15)
p2.desconto(10)
print(p2.preco)