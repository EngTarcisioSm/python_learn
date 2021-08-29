'''
RELAÇÃO ENTRE CLASSES - ASSOCIAÇÃO

     i.        Ocorre quando uma classe esta associada com outra classe ou seja uma classe utiliza outra classe, entretanto as duas classes podem existir separadamente   
     ii.       Um objeto recendo como atributo um outro objeto de outra classe, sendo um caso de associação fraca
'''
from Classe.classes import Escritor 
from Classe.classes import Caneta
from Classe.classes import MaquinaDeEscrever

escritor1 = Escritor('Bryan')
escritor2 = Escritor('Tarcísio')

caneta = Caneta('Bic')
maquina_de_escrever = MaquinaDeEscrever()

escritor1.ferramenta = caneta
escritor2.ferramenta = maquina_de_escrever

escritor1.ferramenta.escrever()
escritor2.ferramenta.escrever()

