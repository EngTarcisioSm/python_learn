'''
EM PYTHON TUDO É UM OBJETO: incluindo classes, Metaclasses são as "classes" que criam classes 

    i.      Para que uma classe seja uma meta classe ela deve seguit alguns passos

    i.i.    Herdar de type
    i.ii.   Usar o método new
    i.iii.  O Método __new__ recebe alguns paramentros como mcs (como se fosse o self), name (nome da classe a ser criada) bases (as classes que essa classe criada herdará) e namespace (contem todos atributos e métodos criados dentro da classe)
    i.iv    Toda classe que herdar da classe meta e suas filhas obedeceram os parametros da meta 

    ii.     É possivel forçar métodos a serem criados em quem herdar de meta, customizar a criação de uma classe através de uma metaclasse 

    iii.    Recurso utilizado na criação de framework 

    iv.     Utilizado em Design Patern (Padrões de projeto)

    v.      É possivel fazer com que o Python com o uso de metaclasses não permita que um atributo seja sobrescrito 

    vi.     É possivel criar classes com type, sendo o primeiro parametro o nome da classe, o segundo parametro se a classe irá herdar de aguem e o terceiro parametro o namespace da classe 
'''

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name) #toda classe criada a partir da meta tera seu nome pritado aqui 
        # se o nome da classe for A faz o que esta abaixo
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        #para as demais classes execute os passos abaixo
        

        #se o atributo attr_classe' for criado em uma classe diferente de A ele não poderá ser sobrescrito 
        if 'attr_class' in namespace:
            del namespace['attr_class']

        #verifica se existe 'b_fala' no namespace
        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}') 
        else:
            #verifica se b_fala é um método ou atributo 
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um método não um atributo')
            return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_class = 'Bryan'
    def fala(self):
        self.b_fala()


class B(A):
    attr_class = 'Tarcisio'
    teste = 'valor'
    b_fala = 'Wow'

    def b_fala(self):
        print('Oi')
    def sei_la(self):
        pass


a = A()
b = B()
print(a.attr_class)
print(b.attr_class)


#vi
ClasseA = type('ClasseA', (), {'attr': 'Olá Bryan'})
a = ClasseA()
print(a.attr)
print(type(a))