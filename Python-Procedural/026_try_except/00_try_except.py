'''
    - Tratamento de Exceções

        - I.        Exceções são erros que ocorre dentro do programa, ocorrendo a parada do programa
        - II.       Para se trata exceções basta envolver o código em questão em um bloco try, segundo de um
                    bloco except (caso o código não funcione o que fazer)

                    try:
                        código
                    except:
                        # o que fazer caso o código acima de errado
        - III.      O except sem um parametro fica sujeito a receber todo tipo de possivel erro, não sendo uma
                    boa pratica efetuar desta forma. Para isso o except pode receber parametro filtrará o tipo
                    de erro a ser analisado, podendo ser tratado ou gerar um log
        - III.I     Mensagens de erro não são boas a serem exibidas para usuário, cabendo apenas e mais recomen
                    davem a disponibilidade para o desenvolvedor
        - IV        Ao usar o tratamento de excessão o código continua funcionando caso ocorra uma excessão
        - V         É possivel existir mais de um bloco de exception caso se verifique a existencia de um erro
                    cinhecido ou não
        - VI        quando não se tem ao certo o tipo de excessão que pode ser gerado pode ser utilizado 'Except'
                    como um nome generico
        - VII       É possivel utilizar um bloco else, que será executado sempre que o bloco try obtiver sucesso
        - VIII      é possivel incluir um ultimo bloco de código chamado finally: que é executado independente da
                    excessão ter ocorrido ou não
        - IX        O bloco finally pode ser utilizado como forma de tratar excessões, caso o bloco try não
                    um valor o bloco finally pode gerar um valor defaut para o código não quebrar
        - X         É possivel existir blocos try dentro de outros blocos try. Quando ocorre esse tipo
                    de ordenação o erro não se propaga para except externos. O tratamento de erros funciona
                    de forma semelhante a if else
        - XI        É possivel criar proprias excessões (visto mais para frente)
'''

print("#II")
try:
    # como a variavel 'a' não foi declarada acarretará em um erro
    print(a)
except:
    print('Erro')

print("# III")
try:
    print(b)
except NameError as erro:
    print('Erro: ', erro)

print("IV")
print('Programa continua mesmo apó a ocorrencia de duas excessçoes')

print(" #V")
try:
    print(c)
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele')
except Exception as erro:
    print('erro inesperado')

print(" #VII")
try:
    a = [1]
    print(a[0])
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
else:
    print("Deu Certo!")

try:
    a = [1]
    print(a[1])
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
else:
    print("Deu Certo!")


print(" #VIII")
try:
    a = [1]
    print(a[0])
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
else:
    print("Deu Certo!")
finally:
    print('Finalmente terminou!')

try:
    a = [1]
    print(a[1])
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave.')
else:
    print("Deu Certo!")
finally:
    print('Finalmente terminou!')

print("IX")
try:
    a = 1/0
except NameError as erro:
    print("...")
except (IndexError, KeyError) as erro:
    print("!!!")
except Exception as erro:
    print("???")
else:
    print("///")
finally:
    a = None

print(a)

print("X")
try:
    a = 0
    try:
        a = 1 /0
    except:
        print("Error")
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print("...")
else:
    print('ccc')
finally:
    print("iii")
    a = 10

print(a)
