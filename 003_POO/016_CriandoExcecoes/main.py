'''
CRIANDO EXCEÇÕES PERSONALIZADAS EM PYTHON 

    i.      Serve para depois de ter pesquisados todas as exceções disponiveis em python e nenhuma lhe atender, neste ponto é possivel criar a propria exceção (erro personalizado ).
    ii.     Toda Exceção por convenção tem seu nome terminado em ERROR
    iii.    A classe que cuidará de exceções deve herdar da classe Exception 
    iv.     Basta apenas criar a classe com o nome do erro, herdar de Exception e nada mais 
    v.      Quando for levantar a exceção tratar da mesma 
'''

# iv
class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Errado!')


# tratar com sucesso a exceção criada 
try: 
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')