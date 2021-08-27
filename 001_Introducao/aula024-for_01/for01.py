'''
- Geralmente o loop while é utilizado para coisas que não sabemos a dimensão final, uma ação quando
não sabemos quando terminará
- Loop while em alguns casos torna o processo mais complexo
- Loop for é utilizado para coisas que sabemos quando terminará
'''

# com loop for a iteração em alguns casos torna-se mais simples de ser efetuada
nome = 'Python'
for letra in nome:
    print(letra)

'''
A função range, é uma função built-in do python que tem por objetivo fornecer um range de numeros, 
tendo os seguintes atributos range(start=0, stop, step=1)
    - start sinaliza de onde os valores irão iniciar, caso este seja omitido será iniciado em zero
    - stop sinaliza onde será o numero final dos valores (lembrando que o numero passado como parametro
    neste atributo não entra no range)
    - step finaliza a passada da contagem, que tem como valor default o valor 1, podendo assim como 
    start ser omitido, pode ocorrer o step positivo e o negativo 

range não esta vinculado ao for, ou seja ele não depende de for e o for não depende dele entretanto 
é uma cobinação boa 
'''
# range apenas com o valor de stop
for n in range(10):
    print(n)

# range com o valor de start stop e step
for z in range(10, 20, 2):  # contará de 2 em 2
    print(z)
# rage decrescente
for j in range(1000, 980, -1):
    print(j)

# iterando sobre uma string com for
nome = 'Bryan William Vasconcelos de Melo'
nome_upper = ''
for letra in nome:
    nome_upper += letra.upper()
print(nome_upper)

# tanto continue como break podem ser utilizados dentro do loop for
# uso com continue
nome_sem_vogal = ''
for letra in nome:
    letra_upp = letra.upper()
    if letra_upp == 'A' or letra_upp == 'E' or letra_upp == 'I' or letra_upp == 'O' or letra_upp == 'U':
        continue
    nome_sem_vogal += letra
print(nome_sem_vogal)

# uso de break
nome_break = ''
for letra in nome:
    if letra == 'V':
        break
    nome_break += letra
print(nome_break)
