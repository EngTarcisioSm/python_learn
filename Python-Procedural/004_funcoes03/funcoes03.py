'''
- uma vez que se nomeia o parametro de uma função, depois de utilizala sempre terá de utiliza-lo
    def(1,3,4, nome='tarc')
    def(143,4, nome='bryan')

-1 Existe alguns momentos em que não se sabe o numero de argumentos que devem ser passados para função,
neste é possivel utilizar como parametro *args
O arg é o empacotamento de uma tupla, diferente de listas, tuplas não podem ser alteradas. O nome do
arg pode ser outro, entretanto a comunicade recomanda utilizar args

-2 Quando se tem uma lista e deseja pegar apenas os n primeiros valores e os demais não, sem perde-los
é possivel utilizar *variavel

3- Quando se tem uma lista e deseja passar ela para uma funcao com args recomenda-se desempacotar ela
diretamente no parametro com o auxilio de *

4 - **kwargs funciona igual aos args, porem recebe chave valor, o que o kwargs. kwargs pode ter outro
nome mais se recomenda a utilização deste para ficar em consonancia com a comunidade

5 - recomenda-se ao usar **kwargs utilizar .get('chave') pois caso a chave não exista é possivel
retornar none. Se não usar esse método e tentar buscar pela chave direto e ela não existir gerará
uma excessão
'''

# 1
def func(*args):
    print(args)
    print(args[0])
    print(len(args))

# 4
def fun2(**kwargs):
    print(kwargs)
    print(kwargs['nome'])

# 4
def fun3(**kwargs):
    print(kwargs)
    nome = kwargs.get('nome')
    if nome is not None:
        return nome

# 2
lista = [1, 2, 3, 4, 5, 6]
n1, n2, *v = lista
print(n1)
print(n2)
print(v)

# 3
func(1,2,3,4,5,6,7)
func(*lista)
func(*lista, 10, 20, 30)
lista2 = [100, 200, 300 ,400]
func(*lista, *lista2)

#4
fun2(nome='Tarcisio', sobrenome='Souza de Melo', idade=32)

print(fun3(nome='Tarcisio', sobrenome='Souza de Melo', idade=32))
