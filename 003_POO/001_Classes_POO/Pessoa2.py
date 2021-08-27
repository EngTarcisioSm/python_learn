from datetime import datetime

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        # mesmo a principio possuindo o mesmo nome de atributo self.nome pertence ao objeto e é diferente
        # de nome
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        #válido apenas dentro do método __init__
        variavel = 'variavel'
        ...

    #método da classe pessoa, ou seja toda pessoa (todo objeto criado neste molde) "fala"
    def fala(self, objeto=None):
        if(self.falando):
            print(f'{self.nome} quer {objeto}')
            self.falando = not self.falando
        else:
            self.falando = not self.falando

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
