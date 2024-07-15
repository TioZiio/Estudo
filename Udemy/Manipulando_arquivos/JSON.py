
# Estrutura de dados serializada em textos simples;
# Transimissão de dados em rede e APIs web;

# Tipos de dados suportados:
#       Números (INT, FLOAT);
#       Strings (STR);
#       Booleanos (TRUE,FALSE);
#       Arrays (LIST)
#       Objetos (DICT);
#       Null (None, valor especial que representa ausência de valor);


# Dump[s] - Jogar pra fora; com strings
# Load[s] - Carregar pra dentro; com strings


# percival = """
# {
#     "name": "Percival",
#     "age": 16,
#     "class": "Guerreiro Balistico",
#     "titles": ["Salvador da Princesa", "Bumbum gostoso"],
#     "items": ["Coldre", "Espada de Família", "Rola 25cm"]
# }
# """

# personagens = json.loads(percival)
# print(personagens)
# print(json.dumps(personagens, indent=2))

import json
import os


arquivo = 'aulaJ.json'

caminho = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        arquivo
    )
)

# print(__file__)
# print(caminho)

dados = [
        {'Nome': 'TioZiio', 'Classe': 'Progenitor', 'Idade': '23', 'Epoca': 'Seculo-21'},
        {'Nome': 'Perciaval', 'Classe': 'Guerreiro', 'Idade': '16', 'Epoca': 'Seculo-17'},
        {'Nome': 'Arthur', 'Classe': 'Diplomata', 'Idade': '15', 'Epoca': 'Seculo-19'}
    ]

def abrir_arquivo():
    with open(caminho, 'w') as arq:
        json.dump(dados, arq, ensure_ascii=False, indent=2)

def ler_arquivo():
    with open(caminho, 'r') as arq:
        lendo_arquivo = json.load(arq)
        print(lendo_arquivo)

abrir_arquivo()
ler_arquivo()