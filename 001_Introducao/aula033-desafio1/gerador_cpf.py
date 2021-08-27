from random import randint

cpf = str(randint(100000000, 999999999))

acumulador = 0
for x, y in enumerate(range(10, 1, -1)):
    auxiliar = int(cpf[x])*y
    acumulador += auxiliar

digito0_calc = 11 - (acumulador % 11)
digito0 = digito0_calc if (digito0_calc <= 9) else 0
newCPF = cpf[:9]+str(digito0)

acumulador = 0
for x, y in enumerate(range(11, 1, -1)):
    auxiliar = int(newCPF[x])*y
    acumulador += auxiliar

digito1_calc = 11 - (acumulador % 11)
digito1 = digito1_calc if (digito1_calc <= 9) else 0
newCPF += str(digito1)

print(newCPF)