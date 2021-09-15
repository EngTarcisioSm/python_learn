'''
    Motido do:
        if __name__ == "__main__"

    i.      Ocorre muitas vezes, não sendo o recomendavel, que o desenvolvedor executa testes do modulo no proprio arquivo do módulo

    ii.     Se um modulo esta sendo executado diretamente o python nomeia o mesmo como __main__ a partir do momento que o módulo e chamado por um primeiro, seu nome é alterado para o nome do proprio arquivo.py

    iii.    Desta forma ao colocar  if __name__ == "__main__"
            É verificado se o arquivo esta sendo executado direta ou indiretamente, caso o mesmo esteja sendo executado indiretamente a condição será falta, logo o que esta abaixo de if não será executado  
'''
from modulo import soma

print(soma(10, 30))