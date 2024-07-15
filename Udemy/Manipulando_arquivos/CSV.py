

from pathlib import Path
import csv 

caminho = Path(__file__).parent / 'aulaCsv.csv'

# print(caminho)

def leitura_listas():
    with open(caminho, 'r') as arq:
        dados = csv.reader(arq)
            
        for l in dados:
            print(l)

def leitura_dicionario():
    with open(caminho, 'r') as arq:
        dados = csv.DictReader(arq)
            
        for l in dados:
            print(l)

dados = [
        {'Nome': 'TioZiio', 'Classe': 'Progenitor', 'Idade': '23', 'Epoca': 'Seculo-21'},
        {'Nome': 'Perciaval', 'Classe': 'Guerreiro', 'Idade': '16', 'Epoca': 'Seculo-17'},
        {'Nome': 'Arthur', 'Classe': 'Diplomata', 'Idade': '15', 'Epoca': 'Seculo-19'}
    ]

def escrever_json():
    with open('aulaJ.json', 'w') as arq:
        import json
        json.dump(dados, arq, indent=2)

def escrever_csv():
    with open(caminho, 'w') as arq:
        indices = dados[0].keys()
        caneta = csv.DictWriter(
            arq,
            fieldnames=indices
        )
        caneta.writeheader()
        for n in dados:
            caneta.writerow(n)

if __name__== '__main__':
    escrever_json()
    escrever_csv()