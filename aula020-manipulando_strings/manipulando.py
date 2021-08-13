'''

'''
# cada caractere de uma string possui um indice iniciado em zero
texto = 'Python s2'
# acessar um indice da string
print(texto[3])

# é possivel efetuar acesso com valores negativos sendo o ultimo caractere com indice de -1
print(texto[-4])

# é possivel efetuar fatiamento de strings informando um intervalo que se deseja, lembrando que
# o valor inicial esta incluso na resposta e o valor contido no indice final não. O intervalo
# a ser passado é dado da seguinte forma [x:y], onde x é o valor inicial e y o valor final
print(texto[2:6])

# caso o valor inicial seja omitido, será considerado como zero, ou seja pegando desde o inicio.
# Se o valor a ser omitido é um valor do intervalo final será considerado até o ultimo indice da string+1
print(texto[:6])
print(texto[7:])

# é possivel entre chaves conter 3 valores [x:y:z] sendo z o passo que a string terá, ou seja, faz com que
# caracteres sejam pulados
print(texto[0:6:2])

# ver a quantidade de caracteres de uma string utilizando a função len() que tem como atributo no caso de
# strings o numero de caracteres de uma string 
num_caracteres = len(texto)