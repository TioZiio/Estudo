produtos = [
	{'nome': 'p1', 'preço': 20,},
	{'nome': 'p2', 'preço': 30,},
	{'nome': 'p3', 'preço': 40,},
	{'nome': 'p4', 'preço': 50,}
]

# Forma normal:
v_produtos = []
for n in produtos:
	if n['nome'] == 'p2':
		n['preço'] *= 5
	v_produtos.append(n)

print()
print()


# Forma reduzida de mapeamento:
n_produtos = [
	{**value, 'preço': value['preço']*5}
	if value['nome'] == 'p2' else {**value}
	for value in produtos
]

for x in n_produtos:
	print(x)