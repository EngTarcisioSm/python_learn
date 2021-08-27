'''
Sistema de perguntas e respostas com dicionários!
'''

# a variavel abaixo conterá todas as perguntas bem como todas as respostas emitidas
perguntas = {
    'Pergunta 1':{'pergunta':'Quanto é 2+2?','resposta': {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,},'resposta_certa': 'e',},
    'Pergunta 2':{'pergunta':'Quanto é 2*2?','resposta':{'a':1, 'b':2, 'c':4, 'd':6, 'e':8,},'resposta_certa': 'c',},
    'Pergunta 3':{'pergunta':'Quanto é 2**2?','resposta':{'a':1, 'b':2, 'c':4, 'd':8, 'e':16,},'resposta_certa': 'c',},

}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk} -> {pv["pergunta"]}')
    print('Respostas: ')
    for rk, rv in pv['resposta'].items():
        print(f'\t[{rk}]: {rv}')
    resposta_usuario = input('Digite sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:
        print('Acertou mizeravi')
        print("eeeeee acertou!!!!")
        respostas_certas +=1
    else:
        print('aaaaaaa errou')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = (respostas_certas / qtd_perguntas) *100

print(f'Acertou {respostas_certas} perguntas')
print(f'{porcentagem_acerto} %')