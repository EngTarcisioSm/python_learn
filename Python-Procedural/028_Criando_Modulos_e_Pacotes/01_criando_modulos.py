'''
CRIANDO MÓDULOS E PACOTES

    - I.        Quando se faz um programa ou script em python, um programa simples pode se tornar gigante,
                recomenda-se organizar o código, dividindo o código em vários módulos cada um com sua respectiva
                função. Modularizando o códgo

    - II.       OBSERVAÇÃO: no python não existe o conceito de variaveis constantes, quando se quer especificar
                que o valor de uma variavel é fixa utiliza-se o nome da mesma toda em maiusculo como norma
                para que os demais programadores entendam que essa variavel não deve ter seu valor alterado

    - III.      os modulos nada mais são que trechos de código. O processo é semelhante ao processo de importar
                módulos que ja vem no python utilizando import nome_modulo
                OBSERVAÇÂO nome_modulo sem ".py" no nome

    - IV.       Um cuidado deve se ter na criação de módulos pois é comum dentro de um módulo se criar testes
                para a lógica que se encontra dentro do mesmo. Ao chamar o código sem o devido tratamento o
                que pode ocorrer é que o import executa todo o código inclusive os trechos de teste para depois
                usar a função ou classe desejada.

    - IV.I      Todo o programa ou script python além do nome do seu arquivo leva um nome dado pelo proprio
                python chamado de __main__, isso pode ser visto testando
                    print(__name__)
                Desta forma como um módulo também possui esse "nome oculto" para evitar que o módulo seja
                executado como um todo, logo abaixo da área de lógica e antes de iniciar a area de testes
                do módulo deve-se colocar
                if __name__ == '__main__':
                Desta forma o trecho de teste do código não será executado, entretanto a lógica de teste
                não será mais executada no proprio módulo

    - V.        É possivel importar o módulo utilizando
                    from nome_modulo import itens, ...

    - VI.       Quando se importa um módulo e não se utiliza a IDE deixa o nome do módulo cinza

    - VII.      Um módulo python nada mais é do que um outro arquivo com códigos python            
'''
import operacoes

print(__name__)

lista = [1,3,5,7,9,11]

print(operacoes.PI)
print(operacoes.dobra_lista(lista))