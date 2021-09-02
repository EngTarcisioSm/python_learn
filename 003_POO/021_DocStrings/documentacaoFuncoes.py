def funcao():
    """A primeira linha ou primeiras linhas de uma função sempre é a documentação"""
    pass


def funcao2():
    """Pode ter varias linhas 

    a primeira linha é uma descrição breve
    """
    pass

#possivel de usar help(nome_funcao)


def funcao3(x,y):
    """
    Soma x e Y

    :param x: Primeiro número
    :type x: int ou float
    :param y: Segundo Numero
    :type y: int ou float

    :return: Soma entre x e y
    :rtype: int ou float 
    """


    return x+y