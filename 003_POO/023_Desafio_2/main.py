"""[Projeto desafio 2]

        - Calculo de Rede Ip v4

            - O ip v4 é formado por um conjunto de 4 numeros cada um podendo ir de 0 a 255

            - Conversão de decimal para binário, utilizando-se de tabela 
                128     64      32      16      8       4       2       1
            Quando vai-se converter um numero (até 255) se escolhe dos numeros acima o que mais se aproxima daquele em que se deseja converter, não podendo ultrapassar o valor 
            exemplo: 10
                128     64      32      16      8       4       2       1
                                                1
            Após isso deve se escolher sempre a direita mais algum ou alguns numeros que somado a esse primeiro totalizando o valor a ser convertido, e os que não forem utilizados preencher com 0
                128     64      32      16      8       4       2       1
                                                1               1

                128     64      32      16      8       4       2       1
                 0      0       0        0      1       0       1       0

            - convertendo um ipv4 em binario
            10.20.12.45
            0000 1010   0001 0100   0000 1100   0010 1101    

            -> tendo uma mascara de rede ex: 26 terce-a 26 bits para rede conforme abaixo utilizando-se do ip acima exemplificado
            0000 1010   0001 0100   0000 1100   0010 1101 
            1111 1111   1111 1111   1111 1111   1100 0000 -> 26 bits para rede
            
            os bits em zero determinam os hosts da rede, ou seja, o numero maximo de computa
            dores possiveis na rede 
            Para se determinar esse numero de computadores utiliza-se a seguinte formula 
                2^b -2  -> onde b é o numero de zeros 

                2^6 - 2 = 62  computadores possiveis na rede

            - para saber o numero de mascara de rede basta fazer a conversão de binário para decimal utilizando a mesma tabela de de dec-> bin preenchendo os quadros da tabela e somando os valores onde resultar 1, octeto por octeto 

            1111 1111   1111 1111   1111 1111   1100 0000
                255         255         255         192

            O primeiro ip da rede acima seria (ip da rede)
            10.20.12.0
            O email de broadcast (ultimo ip) quantidade maxima -1
            10.20.12.63

            Tanto o IP da rede como o de broadcast não se utiliza  sendo o primeiro e ultimo ips respectivamente 
            10.20.12.1
            10.20.12.62



"""             
from calc_mask_ip import CalcMask

a = CalcMask(2, '10.200.40.200')
print(a)