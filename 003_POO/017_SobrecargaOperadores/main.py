'''
SOBRECARGA DE OPERADORES 

    i.      Comportamento de um operdor em python 
            +
            -
            *
            /
            %
            entre outros mais 

    ii.     Quando criamos nossas proprias classes o python não sabe o que fazer com cada operador quando associado a nossas classes, é possivel dar comportamento 
    
    iii.    Existem métodos mágicos que fazem a sobrecarga desses operadores em nossas classes 
            Exemplo:
                __add__
                __sub__
                __mul__
                __div__
                outros mais 
            Metodos mágicos vem acompanhado de dois underlines no inicio e no fim de seu nome
    iv.     Quando a classe criada possui algum desses métodos mágicos a classe ensina ao python como proceder a respeito daquele operador

    v.

    v.i.    Acaba que o método __add__ do exemplo se torna um factory method pois esta criando um objeto da propria classe 

    vi.     Método mágico __repr__
            Quando se printa um objeto ele retorna seu tipo e o seu endereço na memória, com a utilização do método mágico acima é possivel configurar o que sairá ao printar um objeto 
'''

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y

    def __add__(self,other):
        new_x = self.x + other.x
        new_y = self.x + other.y
        return Retangulo(new_x, new_y)

    def __repr__(self):
        return f'<class Retangulo> x: {self.x} y: {self.y}'

    # define simbolo "<"
    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

    # define ">"
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False 
    
    # define "=="
    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

r1 = Retangulo(10, 20)
r2 = Retangulo(20, 30)

r3 = r1 + r2
print(r3.x, r3.y)
print(r3)

print(r1 < r2)
print(r1 > r2)
print( r1 + r2 == r3)