""" 
Criar a estrutura de listas

    - Recriar iterator com uso de listas

    - __repr()__ : representação para desenvolvedores 
    - __str()__: utilizado com comando print
"""

class MinhaLista:

    def __init__(self) -> None:
        self.__items = []
        self.__index = 0
    
    def add(self, valor):
        self.__items.append(valor)

    #caso deseje acessar a lista por indices 
    def __getitem__(self, index):
        return self.__items[index]

    #alterar valores da lista com base em indices 
    def __setitem__(self, index, valor):
        #verifica se o index fornecido existe na lista 
        if index >= len(self.__items):
            self.add(valor)
        else:
            self.__items[index] = valor 

    #deletar item da lista 
    def __delitem__(self,index):
        if index >= len(self.__items):
            raise IndexError(f'Indice:{index} nao existente na lista')
        else:
            del self.__items[index]
     

    #implementação do iterator, a partir do momento que for utilizado um for na classe, ele funcione perfeitamente 
    
    #fala qual o iterador da classe 
    def __iter__(self):
        return self     # o iterador da classe é a propria classe, "padrão de projeto iterator"

    
    #segundo método que um iterador precisa retornará o proximo elemento da lista  
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        #retorna o nome da classe
        # __ chamado de dunder na linguagem python 
        return f'{self.__class__.__name__} ->{self.__items}'



if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Maria') 

    print(lista)

    for valores in lista:
        print(valores)

    lista[0] = 'Bryan'

    print(lista[0])
    print(lista[1])

    lista[3] = 'Tarcisio'

    for x in lista:
        print(x)

    del lista[2]
        

