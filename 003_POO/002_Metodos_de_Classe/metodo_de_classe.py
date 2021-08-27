'''
    - I.        Todo e qualquer método e atributo que tenha em seu parametro ou prefixado no seu nome
                a palavra self esta se referindo a atributos e métodos que um objeto terá, entretanto
                é possivel criar também métodos que pertencem apenas a classe, utilizando a palavra
                reservada @classmethod, no lugar do self é necessário dar um outro nome para esse
                atributo que se referirá a classe e não a instanciação do objeto
'''

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

p1 = Pessoa.por_ano_nascimento('Tarcisio', 1989)
print(p1.nome, p1.idade)