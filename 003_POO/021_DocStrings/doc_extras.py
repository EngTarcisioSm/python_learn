"""Documentação de variaveis e atributos de Funções e classes 

"""

#é possivel especificar o tipo de uma variavel durante o código 

numero: int = 10
num2: float = 1.9

#é possivel especificar os tipos de parametros de funções com a ide reclamando caso for colocado um tipo diferente (funciona tanto para função como para metodos de classe)

def funcao (p1: float, p2: str, p3: dict):
    pass

#é possivel colocar o tipo de retorno de forma explicita  (funciona tanto para função como para metodos de classe)

def funcao2 (p1: float, p2: str, p3: dict) -> float:
    return 10.10

#é possivel indicar que uma função retorna mais de um tipo (tambem métodos) entretanto para isso é necessário utilizar uma biblioteca 
from typing import Union

def funcao2 (p1: float, p2: str, p3: dict) -> Union[float,str]:
    pass