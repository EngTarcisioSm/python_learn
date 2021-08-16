'''
- MÓDULOS PADRÕES DO PYTHON

    - I.        São arquivos .py (que contém código python) e servem para expandir as funcionalidades padrão
                da Linguagem
    - II.       Por padrão o Python já vem com  inumeras funcionalidades imbutidas
    - III.      A linguagem já vem com alguns modulos e é possivel instalar outros módulos externos também
    - IV.       Site com todas as referencias bibliográficas dos modulos que já vem com o pyhton:
                https://docs.python.org/3/py-modindex.html
    - V.        Para importar um módulo basta usar a palavra reservada import entretanto importará o módulo
                inteiro
    - VI.       Para importar apenas um trecho de um módulo utiliza-se:
                    from nome_modulo import nome_trecho_módulo
    - VII.      Quando se importa todo o módulo é necessário para chamar o trecho usar o nome_modulo.nome_trecho
                quando é importado apenas o trecho do módulo isso não se faz mais necessário, chamando apenas
                pelo nome do trecho do módulo
    - VIII.     É possivel dar um apelido para o módulo e chama-lo pelo apelido

    - IX.       O módulo random possui uma função randint(x,y) que retorna numeros aleatorios, sendo 0 o valor
                inicial e y o valor final

    - X.        quando se importa com from e no proprio código ja exista uma função com o mesmo nome a função
                do módulo será sobrescrita naquele stript, caso seja necessário usar o mesmo nome, altere o
                nome da função utilizando "as". utilizando o import normal não se faz necessário pois é neces-
                sario chamar nome_modulo.nome_funcao()
    - XI.       É possivel importar da seguinte forma
                    from nome_modulo import *
                O problema é que importará tudo sem a necessidade do prefixo nome_modulo. o que pode causar
                o sobrescrevimento de alguma função
    - XII.      É possivel importar mais de uma função de um modulo
                    from nome_modulo import func1, func2
    -XIII.      Para instalar um módulo que não foi instalado e não veio junto com o python utiliza-se
                    pip install nome_modulo
    - XIV       Para desinstalar um módulo do python:
                    pip unistall nome_modulo
                É solicitado uma confirmação

'''
# V
# import sys
# from sys import platform
from sys import platform as pl
import random as rd

# informa a plataforma em que o script esta sendo executado
# print(sys.platform)
# VII
# print(platform)
# VIII
print(pl)

#IX
print(rd.randint(0, 10))
for i in range(10):
    print(rd.randint(0,10))