"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""


def request_CNPJ(input):
    cnpj = input
    if len(cnpj) == 18 or len(cnpj) == 14:
        cnpj = remove_char_especial(cnpj)
        if not is_seq(cnpj):
            cnpj = str_to_int(cnpj)
            if cnpj is None:
                print("\t CNPJ digitado invalido")
            else:
                return cnpj
        else:
            print("\t CNPJ digitado invalido")
    else:
        print("\t CNPJ digitado invalido")

def str_to_int(cnpj_string):
    list_numbers = []
    for x in cnpj_string:
        try:
            list_numbers.append(int(x))
        except ValueError:
            return None
    return list_numbers

def is_seq(cnpj):
    seq = cnpj[0] * len(cnpj)
    lista = []
    for x in seq:
        lista.append(x)
    if seq == cnpj:
        return True
    else:
        return False

def remove_char_especial(string_cnpj):
    lista = ['.','/','-']
    string_cnpj = string_cnpj.replace(lista[0], "")
    string_cnpj = string_cnpj.replace(lista[1], "")
    string_cnpj = string_cnpj.replace(lista[2], "")
    return string_cnpj

def removedig(cnpj):
    num1 = cnpj.pop()
    num2 = cnpj.pop()
    return cnpj, (num1 + num2*10)

def calc_check(cnpj):
    list_aux = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    aux = 0
    for x in range(len(list_aux)):
        aux = aux + cnpj[x] * list_aux[x]
    aux = 11 - (aux % 11)
    if aux > 9:
        aux = 0
    cnpj.append(aux)
    list_aux.insert(0, 6)
    aux2 = 0
    for x in range(len(list_aux)):
        aux2 = aux2 + cnpj[x] * list_aux[x]
    aux2 = 11 - (aux2 % 11)
    if aux2 > 9:
        aux2 = 0
    aux = aux*10 + aux2
    return aux


# TESTE AREA
def test_cnpj(input):
    cnpj = request_CNPJ(input)
    cnpj, digVerific = removedig(cnpj)
    digVerific2 = calc_check(cnpj)
    if digVerific == digVerific2:
        print("CNPJ VÁLIDO")
    else:
        print("CNPJ INVALIDO")

if __name__ == '__main__':
    ...