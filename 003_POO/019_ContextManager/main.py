'''
CRIANDO GERENCIADORES DE CONTEXTO 

    i.      Sempre que algo é aberto e fechado é necessário um gerenciador de contexto. Ao abrir determinado processo é necessário fecha-lo, e nesse ponto é que o gerenciador de contexto atua, podendo gerenciar o fechado apos a finalização 
    ii.     Python permite criar os proprios gerenciadores de contexto 
    iii.    with() as -> é um gerenciador de contexto 

    iv.     O gerenciador de contexto assim como o utilizado para abrir arquivos serve para outros processos, como acesso a redes e etc 
    v.      Exemplo
    vi.     Existe outro modo de criar gerenciador de contexto utilizando funções tendo o mesmo resultado 
    vii.    necessário utilizar a biblioteca contextmanager
            from contextlib import contextmanager
    viii.   para a função funcionar como um gerenciador de contexto é necessário que seja utilizado um decorador @contextmanager
    ix.     o retorno deve ser feito com yied

    x.      Tanto a classe como a função devem ser utilizadas com o with
'''
# v
class Arquivo:
    def __init__(self, nome_arquivo, modo_operacao):
        print('Inicio...')
        self.arquivo = open(nome_arquivo, modo_operacao)

    #usado para retornar algo com o uso de "as"
    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    #usado para gerenciar a saida após o fim do uso efetuando algum processo 
    #os parametros do método são utilizados para se gerenciar exceções que ocorrem durante esta execução 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu...')
        #necessário tratar aqui as exceções que podem ocorrer durante o processo de toda execução do gerenciador de contexto 
        self.arquivo.close()


#funcionando igual ao open
with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')


# viii
from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with abrir('abc.txt','w') as arquivo:
    arquivo.write('uma linha mais\n')
    arquivo.write('uma linha mais\n')
    arquivo.write('uma linha mais\n')
    arquivo.write('uma linha mais\n')
