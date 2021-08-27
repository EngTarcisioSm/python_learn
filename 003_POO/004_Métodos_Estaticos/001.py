'''
    - Métodos Estáticos

    I.      métodos estáticos também possui um decorador de método "@staticmethod", não necessitando
            nem da instancia e muito menos da classe.
    II.     Este método funciona como se fosse uma classe isolada da instancia e da classe funcionando
            como uma função, estando interno ao a classe quase por uma questão apenas de organização
    III.    Não recebe como atributo de instancia self e nem da classe cls
    IV.     É possivel criar variaveis dentro do método estático, estando disponivel apenas dentro do
            método estatico
    V.      É possivel chamar um método estático tanto pela classe como pela instancia (objeto)

'''

from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    #esse método de classe acaba atuando como um método que retorna um objeto que tem por objetivo
    #retornar um objeto da classe entretanto tendo outros parametros de entrada
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #método estatico
    @staticmethod
    def gera_id():
        rand = randint(1000, 9999)
        return rand

p1 = Pessoa(nome='Tarcísio',idade=32)
print(p1.gera_id())
print(Pessoa.gera_id())