'''
ENCAPSULAMENTO EM PYTHON 

     i.        Encapsulamento dentro da orientação a Objeto tem por objetivo esconder certas partes do código para proteção do código 
     
     ii.       No encapsulamento o python diverge das demais linguagens de programação com POO ou totalmente voltadas a POO

     iii.      Na POO classe vão existir modificadores de acesso (public - atributos e métodos possiveis de serem acessados dentro e fora da classe , protected - atributos e metodos que podem ser acessados apenas dentro da classe e filhas da classe e private - atributo e metodo apenas acessiveis dentro da propria classe não sendo acessivel a filhas ("herança"))

     iv.       def __init__(self) técnicamente dentro da linguagem python é o que se comporta mais proximo ao comportamento de um construtor de outras linguagens de programação com POO

     v.        Na linguagem python, não existe bloqueios para o desenvolvedor, na classe abaixo, caso self.dados recebesse um valor incorreto poderia quebrar toda a estrutura da classe 

     v.        Como em python não possui modificadores de acesso, foi criado convenções:
               - Atributos e métodos com 1 underline recomenda-se que esse atributo não seja acessa 
                    ex: _nome_atributo
                 Seria o mesmo que um protected (uma proteção mais fraca), em algumas ide's quando utilizado, ao utilizar o intellicense o atributo nem aparece na listagem da instancia, entretanto ainda é possivel acessar e modificá-lo
               - Atributos e métodos com dois underline seguidos é uma recomendação que fortemente o atributo não seja acessado e diverge do modo acima, sendo que esse atributo deixa de ser acessavel facilmente durante o código
                    ex: __nome_atributo
               É o mesmo que um protected mais forte, funciona também para métodos tudo que foi falado para atributos
               Quando tentado acessar mesmo assim o atributo, ocorre um erro 
               Quando é tentado modificar o atributo com o nome, na verdade é criado um novo atributo com esse nome não quebrando o código 
               É possivel mesmo assim acessar o atributo ou método de uma forma mais complexa 
                    nome_objeto._NomeClasse__nome_atributo
     vi.       É possivel deixar a visualização ativa utilizando getters (@property tem a finalidade de transformar um metodo como se fosse um atributo de classe). Caso o usuario tente atribuir um valor será levantado uma excessão pois não foi criado um setter 
'''

class BancoDeDados:

     def __init__(self):
          self.dados = {} 

     def inserir_clientes(self, id, nome):
          # verifica se a chave clientes existe ou não dentro de self.dados
          if 'clientes' not in self.dados:
               # se não existir é criado a chave e inserido 
               self.dados['clientes'] = {id: nome}
          else:
               # caso ja existe é atualizado 
               self.dados['clientes'].update({id:nome})
     
     def lista_clientes(self):
          for id, nome in self.dados['clientes'].items():
               print(id, nome)

     def apaga_cliente(self, id):
          del self.dados['clientes'][id]
          

bd = BancoDeDados()
bd.inserir_clientes(1, 'Bryan')
bd.inserir_clientes(2, 'Tarcísio')
bd.inserir_clientes(3, 'Janete')
bd.inserir_clientes(4, 'Alípio')
print(bd.dados)
bd.apaga_cliente(2)
bd.lista_clientes()


class BancoDeDados2:

     def __init__(self):
          self.__dados = {} 

     def inserir_clientes(self, id, nome):
          # verifica se a chave clientes existe ou não dentro de self.dados
          if 'clientes' not in self.dados:
               # se não existir é criado a chave e inserido 
               self.dados['clientes'] = {id: nome}
          else:
               # caso ja existe é atualizado 
               self.dados['clientes'].update({id:nome})
     
     def lista_clientes(self):
          for id, nome in self.dados['clientes'].items():
               print(id, nome)

     def apaga_cliente(self, id):
          del self.dados['clientes'][id]

     @property
     def dados(self):
          return self.__dados


bd1 = BancoDeDados()
bd1.inserir_clientes(1, 'Bryan')
bd1.inserir_clientes(2, 'Tarcísio')
bd1.inserir_clientes(3, 'Janete')
bd1.inserir_clientes(4, 'Alípio')
#print(bd1.__dados)
bd1.__dados = 'kkkkkkkkkkkk'
print(bd1.__dados)
bd1.apaga_cliente(2)
bd1.lista_clientes()

# print(bd1._BancoDeDados2__dados)
print(bd1.dados)