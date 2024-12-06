from typing import List, Union, Tuple, Dict, Any, NewType, Callable

# Primitivos
string: str = 'Hello Word'
numero: int = 10
flutuante: float = 10.5
boleano: bool = True

# Padrão python
tuplas: tuple = (1, 2, 3)
lista: list = [1, 2, 3]

# Sequencias com Typing
t_lista: List[int] = [1, 2, 3]
t_tuplas: Tuple[int, int, int] = (1, 2, 3)
t_lista_mista: List[Union[int, str]] = [1, 'a', 2, 'b']

# Dicionarios e conjuntos com Typing
pessoa: Dict[str, Union[str, int]] = {'nome': 'Tio', 'idade': 20}
pessoa2: Dict[str, Any] = {'nome': 'Tio', 'idade': 20, 'homem': True}

# Criando Alias
DictPlayer = Dict[str, Union[str, int, List[Union[int, str]]]]
pessoa3: DictPlayer = {
        'player': 'TioZiio', # str:str
        'age': 500 , # str:int
        'numb_luck': [1,15,26], # str:list[int]
        'skils': ['bola de fogo', 'decadencia'] # str:list[str]
        }

# Novo tipo
UserID = NewType('UserID', int)
tioziio = UserID(2)

# Callable
def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    # Função que recebe outra função.
    # Callable é um tipo que e usado para chamar outra função e dar um resultado
    return funcao

def mostra_oi():
    print('OI')
retorna_funcao(mostra_oi())


def retorna_funcao2(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y
retorna_funcao2(soma)(1, 2)

# Classes
class Player:
    def __init__(self, 
            player: str,
            age: int,
            numb_luck: List[int],
            skils: List[str]
        ) -> None:
        
        self.player: str = player
        self.age: int = age
        self.numb_luck: List[int] = numb_luck
        self.skils: List[str] = skils
    

