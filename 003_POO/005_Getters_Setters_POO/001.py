'''
    - Métodos Getters e Setters em POO (Python)

     I.      POO da linguagem pyhton é um pouco diferente das outras linguagens de programação
     II.     Para dar mais estabilidade nos dados que uma classe recebe existem os metodos getters e setters
             Como o proprio nome ja informa, um getter fornece um valor enquanto um setter, configura um valor
     III.    Quando utilizado um método getter, ao invez de fazer o acesso direto a um atributo da classe, uma função fara a interface de acesso a este valor
             Por padronização ao retornar o atributo desejado é inserido um underline na frente do nome do atributo
     IV.     Por sua vez o metodo setter faz a interface quando vai ser configurado um atributo de uma interface.
     V.      O método getter utiliza como decorador "@property" enquanto o metodo setter utiliza como decorador "@nome_atributo.setter
     VI.     Tanto o getter como o setter são metodos e levam o nome do atributo

     VII.    Os métodos getters e setters são de certa forma uma proteção para os atributos da classe 




parei em 7:22
'''

class Produto:

     def __init__(self, nome, preco):
          self.nome = nome
          self.preco = preco

     def desconto(self, percentual):
          self.preco = self.preco - (self.preco *(percentual/100))

     #Getter nome
     @property
     def nome(self):
          return self._nome

     #Setter preco
     @nome.setter
     def nome(self, new_nome):
          self._nome = new_nome.title()

     #Getter preco
     @property
     def preco(self):
          return self._preco

     #Setter preço
     @preco.setter
     def preco(self, new_preco):
          # Como tudo no python são objetos, verifica se new_preço é uma instancia da classe str
          if isinstance(new_preco, str):
               # Retira R$ da string deixando apenas numeropara depois ser convertido para float
               # replace não é a melhor forma de tratar iss, existem expressões regulares 
               self._preco = float(new_preco.replace("R$",""))
          else:
               self._preco = new_preco


p1 = Produto(nome='CAMISETA', preco=50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto(nome='caneca', preco=15)
p2.desconto(10)
print(p2.nome, p2.preco)