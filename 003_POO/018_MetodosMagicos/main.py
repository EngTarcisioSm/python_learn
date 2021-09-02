'''
MÉTODOS MÁGICOS 

    i.      São métodos que começam e teminam com dois underline (dunder)
    
    ii.     Modificam o comportamento da classe 
    
    iii.    Existem vários métodos mágicos  
    
    iv.     Referencia bibliografia
            https://rszalski.github.io/magicmethods/

    v.      Serão citados abaixo apenas alguns 

    vi.     __init__(self) é um método mágico
            Primeiro processo executado após a instanciação da classe 
            Costuma-se chamar o __init__ de construtor de classe entretanto ele não é pois tem outros processos que são inicializados antes dele

    vii.    o método que de fato constroi o objeto é o método magico  __new__(cls, *args **kwargs) 
            __new__ e __init__ juntos podem ser chamados de um construtor de objeto (não se tem um conceito definido de construtor em python, esses dois métodos juntos efetuam esse processo)

    viii.   em python toda a classe deriva de object, ou seja toda classe herda de objetc

    ix.     Torna possivel não permitir que uma classe seja instanciada mais que uma vez 

    x.      __call__(self, *args, **kwargs)
            Faz a classe se comportar como uma função, podendo ser desenvolvido qualquer lógica dentro desse método 
            A classe continua funcionando normalmente, apenas tendo esse comportamento quando for utilizada como uma função 

    xi.     __setattr__(self, name: str, value: Any)
            Será chamado toda vez que um atributo novo for configurado na classe 
            Sendo possivel interceptar no ato da atribuição e tomar alguma atitude antes do metodo retornar ao seu comportamento normal 

    xii.    __del__(self)
            Executa a lógica que esta nesse método sempre que o garbage collector do python deletar o objeto em questão, o python em sua documentação informa que ele não é preciso podendo não ser incentivado o uso pois o python não garante sua execução 
   
    xiii.   __str__(self)
            quando um objeto é instanciado e se tenta printar, é retornado o nome de sua nome do módulo nome da classe e a posição na memoria, esse método altera esse comportamento sendo permitido desenvolver uma logica dentro do mesmo   

    xiv.    __len__(self)
            quando a função len é executada essa função é chamada dentro da classe  
'''

class A:
    #def __new__(cls,  *args, **kwargs):
    #
    #    # ix
    #    if not hasattr(cls,'_jaexiste'):
    #        cls._jaexiste = object.__new__(cls)
    #
    #    return cls._jaexiste


    def __init__(self):
        print('Eu sou o INIT')

    #x
    def __call__(self, *args, **kwds):
        print(args)
        print(kwds)

    def __setattr__(self, name, value):
        print(f'{name}: {value}')
        self.__dict__[name] = value # comportamento normal da classe
        pass

    def __del__(self):
        print('Objeto coletado') 

    def __str__(self):
        return 'Estou com vontade de ir embora'

    def __len__(self):
        return 666

# mostrando o init sendo executado logo após a instanciação do objeto 
a = A()

# iX
#b = A()
#c = A()
#print( a == b)

#x
a(1,2,3,4,5, nombre='Luiz')

a.nombre = 'Bryan'

print(len(a))

print(a)
