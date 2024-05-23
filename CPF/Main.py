from config import *

estado()

perg = int(input('Qual estado: '))

print(f'Seu novo nome é: {novo_nome()}\nSeu CPF é: ', end='')
for n in mostrar_cpf(perg):
	print(f'\033[1;31m{n}\033[m', end='')
print()