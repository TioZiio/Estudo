from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

nome_arquivo = 'leagueoflegends.txt'
lista_nomes = 'nomes.txt'

def puxar_nomes():
	names = []
	with open(lista_nomes, 'r') as arq:
		for n in arq:
			names.append(n.strip().lower())
	return names

def puxar_informacoes_champion(nome, personagens):
	chrome_options = Options()
	chrome_options.add_argument('--headless')

	url = f'https://universe.leagueoflegends.com/pt_BR/champion/{nome}/'

	driver = webdriver.Chrome(options=chrome_options)
	driver.get(url)
	driver.implicitly_wait(12)

	text = BeautifulSoup(driver.page_source, 'html.parser')
	frase = text.find('div', class_='championQuotesContainer_37am')

	comentario = frase.find('li', class_='quote_2507')
	pre_biografia = frase.find('div', class_='biographyText_3-to')
	
	if f'{nome}' in personagens:
		personagens[f'{nome}'].extend([comentario.text, pre_biografia.text])
	else:
		personagens[f'{nome}'] = [comentario.text, pre_biografia.text]

	driver.quit()

def puxar_biografia_champion(nome, personagens):
	chrome_options = Options()
	chrome_options.add_argument('--headless')

	url = f'https://universe.leagueoflegends.com/pt_BR/story/champion/{nome}/'

	driver = webdriver.Chrome(options=chrome_options)
	driver.get(url)
	driver.implicitly_wait(12)

	text = BeautifulSoup(driver.page_source, 'html.parser')
	biografia = text.find_all('p', class_='p_1_sJ') 
	temp = [x.text for x in biografia]
	
	if f'{nome}' in personagens:
		personagens[f'{nome}'].append(temp)
	else:
		personagens[f'{nome}'] = [temp]

	driver.quit()

def escrever_arquivo(dados):
	print('--> Escrevendo no txt...')
	with open(nome_arquivo, 'w', encoding='utf-8') as arq:
		for chave, valor in dados.items():
			arq.write(f'{chave}: {valor}\n')

def puxar_dados_arquivos():
	# Puxar todos os dados, sem especificações.
	dados = {}
	try:
		with open(nome_arquivo, 'r', encoding='utf-8') as arq:
			for linha in arq:
				chave, valor = linha.strip().split(': ', 1)
				dados[chave] = valor
	except FileNotFoundError:
		print(f"Arquivo '{nome_arquivo}' não encontrado.")
	return dados

def buscar_no_arquivo(nome_desejado, arquivo):
	with open(arquivo, 'r', encoding='utf-8') as arq:
		dados = arq.read()
		if nome_desejado.lower() in dados.lower():
			inicio = dados.find(f"{nome_desejado}:")
			fim = dados.find(']', inicio)
			trecho = dados[inicio:fim].strip()
			print('\n' + trecho)
		else:
			print(f"Nome '{nome_desejado}' não encontrado no arquivo.")

def main():
	names = puxar_nomes()
	personagens = {}

	for n in names:
		puxar_informacoes_champion(n, personagens)
		puxar_biografia_champion(n, personagens)

	escrever_arquivo(personagens)

if __name__ == '__main__':
	main()
	perg = str(input('Qual o nome do champion para uma pesquisa única:\n'))
	buscar_no_arquivo(perg, nome_arquivo)