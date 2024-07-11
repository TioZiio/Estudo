import json

arquivo = 'classe.json'

personagens = {
    'Game_01': {
        'nome': ['Zarathrusta','Sinistra', 'Senhor d Engenho'],
        'classe': 'Sem-teto',
        'arma': 'Espada Curta e Escudo'}
}

def escrever_arquivo_json():
    with open(arquivo, 'w') as arq:
        json.dump(
            personagens,
            arq,
            indent=2
        )
    return print('Sucesso')

def ler_arquivo_json():
    with open(arquivo, 'r', encoding='utf8') as arq:
        info = json.load(arq)
        print(info)


escrever_arquivo_json()
ler_arquivo_json()