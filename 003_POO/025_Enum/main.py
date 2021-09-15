"""
ENUM - tipo de dado

    - Implementado a partir da função de 3.4 para cima 
    - Para se utilizar enum deve-se importar o módulo
        from enum import Enum
    - Cria enumerações assim como em outras linguagens 
    - para gerar a numeração de forma automatica importa-se auto da biblioteca enum
    - Para se criar um enum deve-se criar uma classe e esta herdar de enum  
    - É possivel utilizar for com enum 

    - Sempre que existir algum set de escolhas, conjunto de coisas, que se deseje escolher, uma boa opção é utilizar enum 

    - Muito utilizado em testes 
"""
from enum import Enum, auto

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()

#exemplo para utilizar o enum com um if, ao invez de se ter um if imenso, utiliza enum simplificando o if facilitando inclusive novas implementações no enum sem a necessidade de se mexer tanto no código da função abaixo 
def move(direction:Directions)->str:
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()
    for direction in Directions:
        print(direction, direction.name, direction.value)