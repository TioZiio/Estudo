from random import randint
from config import *
name = ["Ana", "Carlos", "Daniel", "Eduardo", "Fernanda", "Gabriela",  "Henrique", "Isabel", "João", "Karina",
        "Lucas", "Maria", "Nicolau", "Olga", "Pedro", "Queren", "Rafael", "Sofia", "Tatiana", "Umberto"]
codiname = ["Almeida", "Barbosa", "Carvalho", "Dias", "Esteves", "Faria", "Gomes", "Hernandez", "Jacobs",
            "Klein", "Lima", "Machado", "Nogueira", "Oliveira", "Pereira", "Mendes"]
cpf = []
lista = []
cont = calculo = 0
cont_cal = 10

print('Escolha o Estado:\n'
      '[1] Distrito Federal, Goias, Mato Grosso, Mato Grosso do Sul, Tocantins\n'
      '[2] Amazonas, Para, Roraima, Amapa, Acre, Rondonia\n'
      '[3] Ceara, Maranhao, Piaui\n'
      '[4] Praiba, Pernanbuco, Alagoas, Rio Grande do Norte\n'
      '[5] Bahia, Sergipe\n'
      '[6] Minas Gerais\n'
      '[7] Rio de Janeiro, Espirito Santo\n'
      '[8] Sao Paulo\n'
      '[9] Parana, Santa Catarina\n'
      '[0] Rio Grande do Sul')
cod_estado = int(input('Qual estado: '))

new_name = randint(0, len(name)-1)
for n in range(2):
    new_codiname_1 = randint(0, len(codiname)-1)
    new_codiname_2 = randint(0, len(codiname)-1)
    if new_codiname_2 == new_codiname_1:
        new_codiname_2 -= 1
print(f'\n\033[31m{name[new_name]} {codiname[new_codiname_1]} {codiname[new_codiname_2]}\033[m')

for n in range(8):
    cpf.append(randint(0, 9))
for n in cpf:
    print(f'{n}', end='')
    cont += 1
    if cont == 3 or cont == 6:
        print(f'', end='.')
    if cont == 8:
        print(f'{cod_estado}-', end='')

for dv_1 in cpf:
    calculo = dv_1 * cont_cal
    cont_cal -= 1
    lista.append(calculo)
lista.append(calculo + (cod_estado * 2))

cal_1 = sum(lista) % 11
if cal_1 == 0 or cal_1 == 1:
    cal_1 = 0
else:
    cal_1 = 11 - cal_1
print(cal_1, end=''), cpf.append(cod_estado), cpf.append(cal_1), lista.clear()

calculo = 0
cont_col = 10
for dv_2 in cpf[1:]:
    calculo = dv_2 * cont_col
    cont_col -= 1
    lista.append(calculo)
cal_2 = sum(lista) % 11
if cal_2 == 0 or cal_2 == 1:
    cal_2 = 0
else:
    cal_2 = 11 - cal_2
print(cal_2)

