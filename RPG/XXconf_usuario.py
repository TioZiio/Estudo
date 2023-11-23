arq = 'usuarios.txt'

def LerArquivo(txt):
	all_dados = []
	try:
		x = open(txt, 'rt')
	except Exception as erro:
		print(f'ERRO: {erro.__class__}')
	else:
		for n in x:
			dados = n.split(';')
			all_dados.append(dados[:])
	finally:
		x.close()
	return all_dados

def Cadastro(txt, nome='<desconhecido>', classe='<desconhacida>', lv=0):
	try:
		x = open(txt, 'at')
	except Exception as erro:
		print(f'ERRO: {erro.__class__}')
	else:
		try:
			x.write(f'{nome};{classe};{lv}\n')
		except Exception as erro:
			print(f'Houve ERRO: {erro}')
		else:
			print(f'Novo Cadastro com sucesso !!!\nBem-Vindo {nome}.')
		finally:
			x.close()

def analise(txt, nome='<desconhecido>', classe='<desconhacida>'):
	try:
		x = open(txt, 'wt')
		
	except Exception as erro:
		print(f'Houve ERRO: {erro}')
