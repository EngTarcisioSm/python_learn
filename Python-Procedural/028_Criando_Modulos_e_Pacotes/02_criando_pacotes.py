'''
CRIANDO PACOTES PYTHON

    - i.        Pacotes em python são pastas
    - ii.       Pacotes são pastas com varios arquivos python (modulos)
    - iii.      Dentro de todo pacote python (ou subpacote) não é necessário mais é recomendavel ter um arquivo
                com o nome de
                    __init__py

    - iv.       Existe varias formas de se chamar um código de um módulo
    - iv.i      Modo 1:
                    import nome_pasta.nome_modulo
                A não ser que se utilize a abreviação com "as", toda vez que for utilizar alguma parte do
                módulo sera necessário utilizar o nome inteiro nome_pasta.nome_modulo.funcao_ou_outros
    - iv.ii     Modo 2:
                    from nome_pasta import nome_modulo
                Reduz o tamanho do código
    - iv.iii    Modo 3:
                    from nome_pasta.nome_modulo import itens_de_modulo
                Reduz mais ainda o tamanho do código

    - v         É possivel criar pacotes dentro de pacotes

'''
# iv

from teste_vendas.preco import preco_aumento

valor = 49.90
preco_com_aumento = preco_aumento(preco=valor, percentual=10, formata=True)
print(preco_com_aumento)
preco_com_aumento = preco_aumento(preco=valor, percentual=10, formata=False)
print(preco_com_aumento)
