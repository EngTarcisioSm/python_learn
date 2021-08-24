'''
    I.      Geralmente o código main não importa todos pacotes, existem módulos que consome outros modulos
    II.     Quando python vai buscar modulo inicialmente ele busca no seu path. Isso pode ser visto usando a
            biblioteca sys com o modulo sys.path
    III.    Quando existir um main vários outros módulos dentro de diretórios e haja a necessidade de um módulo
            importar outro módulo basta ao realizar o import ter a visão do arquivo main. Esse processo
            funcionará para a execução do main entretanto os modulo sozinho não funcionará

            main
            modulo1
                - arquivo1.py
            modulo2
                - arquivo2.py

            no arquivo2
                from modulo1 import arquivo1

    IV.     Um segundo jeito utilizado em sua grande parte para textes é o trecho de código abaixo

            try:
                import sys
                import os

            sys.path.append(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        '../
                    )
                )
            )

            Esse trecho de código é colocado no início do arquivo desta forma tornando possivel importar
            módulos de outras pastas de forma normal, quanto mais profundo o modulo que chama estiver
            mais ../../ tem de ser usado 
'''
import sys

print("#2")
for x in sys.path:
    print(x)
