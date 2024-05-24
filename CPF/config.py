from random import randint

def estado():
	"""
	Funçao apenas para mostra codigo dos estados.
	"""
	print("Escolha o Estado:\n[1] Distrito Federal, Goias, Mato Grosso, Mato Grosso do Sul, Tocantins\n"
			"[2] Amazonas, Para, Roraima, Amapa, Acre, Rondonia\n[3] Ceara, Maranhao, Piaui\n"
			"[4] Praiba, Pernanbuco, Alagoas, Rio Grande do Norte\n[5] Bahia, Sergipe\n"
			"[6] Minas Gerais\n[7] Rio de Janeiro, Espirito Santo\n"
			"[8] Sao Paulo\n[9] Parana, Santa Catarina\n[0] Rio Grande do Sul")

def novo_nome():
	"""
	Funçao para criaçao do novo nome, nome completamente aleatorio.
	new_name = Gera um valor para puxar o nome na lista "name".
	new_codiname_1 = Gera um valor aleatorio para puxar o sobrenome da lista "codiname".
	new_codiname_2 = Gera um valor aleatorio para puxar o sobrenome da lista "codiname".
	"""
	name = ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Mateus", "Isabela", "Marcos", "Larissa", "Rafael", 
		"Carolina", "Gabriel", "Amanda", "Thiago", "Beatriz", "Fernando", "Bianca", "Leonardo", "Natália", "Felipe", 
		"Mariana", "Diego", "Luana", "Gustavo", "Camila", "Rodrigo", "Luiza", "Luciano", "Vivian", "Marcelo", "Fátima", 
		"Renato", "Priscila", "Alexandre", "Sofia", "Ricardo", "Giovanna", "Bruno", "Lorena", "Eduardo", "Letícia", "Guilherme", 
		"Marina", "Vinicius", "Clara", "Maurício", "Isadora", "Emanuel", "Paloma"]
	codiname = ["Silva", "Santos", "Souza", "Oliveira", "Pereira", "Rodrigues", "Almeida", "Costa", "Ferreira", "Gomes", 
		"Martins", "Carvalho", "Araujo", "Ribeiro", "Cruz", "Marques", "Barbosa", "Fernandes", "Mendes", "Nunes", "Monteiro", 
		"Moura", "Cavalcanti", "Cardoso", "Freitas", "Moreira", "Lima", "Castro", "Sampaio", "Vieira"]
	new_name_1 = randint(0, len(name)-1)
	new_name_2 = randint(0, len(name)-1)
	for n in range(2):
		new_codiname_1 = randint(0, len(codiname)-1)
		new_codiname_2 = randint(0, len(codiname)-1)
		if new_codiname_2 == new_codiname_1:
			new_codiname_2 -= 1
	if new_name_1 % 3 == 1:
		guardar = f'{name[new_name_1]} {name[new_name_2]} {codiname[new_codiname_1]} {codiname[new_codiname_2]}'
	else:
		guardar = f'{name[new_name_1]} {codiname[new_codiname_1]} {codiname[new_codiname_2]}'
	return f'\033[1;31m{guardar}\033[m'

def criar_cpf():
	"""
	Funçao para gerar o CPF aleatorio, Apenas os 8 primeiros digitos.
	cpf = Lista principal, onde e guardado o cpf( 8 digitos ).
	"""
	cpf = []
	for n in range(8):
		cpf.append(randint(0, 9))
	return cpf

def validaçao_1(x=1):
	"""
	Funçao para validar apenas o 10º digito do CPF.
	O calculo feito e baseado no calculo da verificaçao da Receira Federal.
	"""
	lista = []
	calculo = 0
	cont_cal = 10
	for dv_1 in criar_cpf():
		calculo = ((dv_1) * (cont_cal))
		cont_cal -= 1
		lista.append(calculo)
	lista.append(calculo + (x * 2))
	cal_1 = sum(lista) % 11
	if cal_1 < 2:
		cal_1 = 0
	else:
		cal_1 = 11 - cal_1
	return cal_1

def validaçao_2():
	"""
	Funçao para validar apenas o 11º digito do CPF.
	O calculo feito e baseado no calculo da verificaçao da Receira Federal.
	"""
	numeros = criar_cpf()
	lista = []
	calculo = 0
	cont_col = 10
	for dv_2 in numeros[1:]:
		calculo = ((dv_2) * (cont_col))
		cont_col -= 1
		lista.append(calculo)
	cal_2 = sum(lista) % 11
	if cal_2 < 2:
		cal_2 = 0
	else:
		cal_2 = 11 - cal_2
	return cal_2

def mostrar_cpf(x):
	"""
	Funçao usada para formatar em escrita o CPF construido.
	Construido pelas funçoes (criar_cpf(), validaçao_1(), validaçao_2())
	guardar_cpf = Apenas uma lista para futuramente utilizar os CPF criados.
	"""
	cont = 0
	guardar_cpf = []
	for n in criar_cpf():
		guardar_cpf.append(n)
		cont += 1
		if cont == 3 or cont == 6:
			guardar_cpf.append('.')
		if cont == 8:
			guardar_cpf.append(x)
			guardar_cpf.append('-')
	guardar_cpf.append(validaçao_1(x))
	guardar_cpf.append(validaçao_2())
	return guardar_cpf
