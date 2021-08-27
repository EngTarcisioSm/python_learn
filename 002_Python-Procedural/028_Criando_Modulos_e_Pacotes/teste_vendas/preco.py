from teste_ajuste.correcao import toReal

def preco_desconto(preco, percentual, formata=False):
    preco_output = 0
    if percentual > 1:
        preco_output = preco * ((100 - percentual)/100)
    else:
        preco_output = preco * (1 - percentual)

    if not formata:
        return preco_output
    else:
        return toReal(preco_output)

def preco_aumento(preco, percentual, formata=False):
    preco_output = 0

    if percentual > 1:
        preco_output = preco * ((100 + percentual)/100)
    else:
        preco_output = preco * (1 + percentual)

    if not formata:
        return preco_output
    else:
        return toReal(preco_output)




