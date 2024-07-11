# instance - Descobrir qual é o tipo do objeto

lista = [
    'a', 1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome': 'David'},
]

for item in lista:
    # recebe os dados(item) e pprecisa de um typ(set, int, float, list...)
    if isinstance(item, set):
        print(item)