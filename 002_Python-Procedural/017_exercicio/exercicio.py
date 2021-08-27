'''
    - Em um e-commerc o carrinho do cliente é armazenado em uma lista, cada item da lista é composto por
    uma tupla na qual existe o nome do produto e o valor
    - Deseja-se que a somatoria da lista seja feita por list comprehension
'''
carrinho = []
carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

totalCompra = sum([x[1] for x in carrinho])
print(totalCompra)