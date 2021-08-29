'''
COMPOSIÇÃO

     i.        Relação mais forte entre classes 
     ii.       Uma classe será dona de objetos de outras classes 
     iii.      Se uma classe princiál for apagada todos os demais objetos que ela possuia serão apagados juntos 
     iv.       O método __del__(self) em classes ocorre quando o garbage colector do python deleta um objeto 
'''
from classes import Cliente, Endereco

cliente1 = Cliente('Tarcísio', 32)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
del cliente1
print()

cliente2 = Cliente('Bryan', 5)
cliente2.insere_endereco('Ferraz de Vasconcelos', 'SP')
cliente2.insere_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Janete', 57)
cliente3.insere_endereco('São Paulo', 'SP')
cliente3.insere_endereco('Águas de Lindóia', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
print(f'########## Fim do programa ##########')