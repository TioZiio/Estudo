
import json
import string
import sqlite3
from pathlib import Path


# Primeiro uso do String ---------------------------------
arquivo = Path(__file__).parent / 'aulaJ.json'

def abri_dados():
    with open(arquivo, 'r') as arq:
        dados = json.load(arq)
        # print(dados)
    return dados

def texto() -> str:
    frase = """
        Senhor ${nome} esta convidado a participar do RPG de ${rpg}, onde atuará como ${classe} durante o ${epoca} 
        com a idade inicial de ${idade} no dia 30/07/2024.

        Fico no aguardo da sua resposta, senhor ${nome}.

        Atenciosamente, 
        
        God.
    """
    return frase
# ------------------------------------------------------------


# Segundo uso do String -------------------------------
db = '/home/anonimo/Área de Trabalho/GitHub/Estudo/Projeto_Tkinter/clientes.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

    
def Desconecta_db():
    conn.commit()
    conn.close()
    print('Desconectado do banco de dados')

def puxa_dados():
    cursor.execute(f"""SELECT nome,telefone,endereco,cidade FROM clients""")
    clientes = cursor.fetchall()
    return clientes

def organiza_dicionario():
    temporario = []
    dados = puxa_dados()
    colunas = [col[0] for col in cursor.description]
    for linha in dados:
        valores = {colunas[i]: linha[i] for i in range(len(colunas))}
        temporario.append(valores)
    return temporario

def texto_db() -> str:
    frase_db = """
        Senhor(a) ${nome} com telefone ${telefone}, apartir do dia 30/07/2024 até 10/08/2024 
        recebera um desconto de R$$ 5,00 na taxa de entrga na area do(a) ${cidade} .

        Confirme seu endereço: ${endereco} e garanta seu cupon.

        Atenciosamente,
        Pipocaria Imperial.
    """
    return frase_db


if __name__ == '__main__':
    personagens = abri_dados()
    template = string.Template(texto())
    for n in personagens:
        print(template.substitute(n))
        print(40 * '_')

    pessoas = organiza_dicionario()
    db_template = string.Template(texto_db())
    
    for n in pessoas:
        print(db_template.substitute(n))
        print(40 * '_')

    Desconecta_db()