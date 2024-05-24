import requests
from bs4 import BeautifulSoup
import re


url = 'https://maisesports.com.br/data-lancamento-todos-campeoes-do-lol/'
dados = BeautifulSoup(requests.get(url).content, 'html.parser')

todos = dados.find_all('li')
personagens = []

for n in todos:
	t = str(n)
	if 'Lutadores' in t:
		break
	personagens.append(n.text)

personagens.pop(0)

campeoes = []
for campeao in personagens:
	remove = campeao.replace('-', '').replace('–', '')
	match = re.search(r'^([^\d]+)', remove)
	if match:
		nome = match.group(1).strip()
		campeoes.append(nome)

# Salvar os nomes em um arquivo de texto
with open('nomes.txt', 'w') as file:
	for nome in campeoes:
		file.write(nome + '\n')

"""
Observação: quando executado e escrito no arquivo, alguns nomes devem ser alterados por enquento manualmente.
	Nomes com espaço ou ' gerarao erro.
	Exemplos:
			K'Sante -> fica -> KSante
			Renata Glasc -> RenataGlasc
			Nunu & Willump -> Nunu
	Os nomes são: 
		K'sante, Bel'Veth, Renata Glasc,  Kai'sa, Aurelion Sol, Rek'Sai, Vel'Koz, Kha'Zix
		Lee Sin, Jarvan IV, Miss Fortune, Xin Zhao, Kog’Maw, Dr. Mundo, Cho’Gath, Master Yi
		Nunu & Willump
"""