'''
Faça um programa que pergunte ao usuário a hora, baseando-se no horário descrito, exiba a
saudação apropriada.
Bom dia 0 - 11
Boa tarde 12 - 17
Boa Noite 18 - 23
'''

hora = input('Informe a hora: ')

if hora.isnumeric():
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa Tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa Noite')
    else:
        print('Hora inválida')
else:
    print('Hora inválida')