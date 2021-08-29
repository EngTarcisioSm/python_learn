'''
AGREGAÇÃO

     i.        Tanto na agregação como na composição, uma classe usa a outra parte como parte de sí e a primeira necessita obrigatóriamente da segunda classe 
               ex: carro e rodas, o carro existe sem as rodas, as rodas existe sem o carro, entretanto para o carro funcionar corretamente o carro deve ter as rodas
     ii.       Enquanto para o correto funcionamento da primeira classe é necessário utilizar a segunda, a segunda classe não necessita da primeira
'''
from classes import CarrinhoDeCompras, Produto

carrinho_compras = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000.00)
p3 = Produto('Caneca', 15)

carrinho_compras.inserir_produto(p1)
carrinho_compras.inserir_produto(p2)
carrinho_compras.inserir_produto(p3)

carrinho_compras.lista_produto()
print(carrinho_compras.soma_total())