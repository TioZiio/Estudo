"""
1 - Receber um número inteiro
2 - Saber se o número e multiplo de 3 e 5:
    Bacon com Ovos
3 - Saber se o número NÃO é multiplo de 3 e 5:
    Fica com fome
4 - Saber se o número e multiplo somente de 3:
    Bacon
5 - Saber se o número e multiplo somente de 5:
    Ovos
6 - Saber se o número e NÃO é multiplo de nenhum destes:
    Fica com fome
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n: int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    if n % 3 == 0:
        return 'Bacon'
    elif n % 5 == 0:
        return 'ovos'

    return 'Fica com fome'
