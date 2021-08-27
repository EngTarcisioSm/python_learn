'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva
"Seu nome é grande"
'''

nome = input("Insira seu primeiro nome: ")

size_nome = len(nome)

if size_nome <= 4:
    print("Seu Nome é curto")
elif size_nome <= 6:
    print("Seu nome pe normal")
else:
    print("Seu nome é muito grande")