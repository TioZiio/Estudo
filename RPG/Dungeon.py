dados = {}
lista = []
mob = []
quant = []

while True:
      dados['name'] = str(input('Nickname: '))
      dados['andar'] = int(input('Quantos andares da dungeon: '))
      for n in range(dados['andar']):
            quant.append(int(input(f'Quantos mobs no {n+1}º andar: ')))
            dados["mobs"] = quant[:]
      mob.append(sum(quant))
      dados['total'] = mob[:]
      lista.append(dados.copy())
      mob.clear(), quant.clear()
      print('-=' * 15)
      perg = str(input('Mas alguem [S/N]: ')).strip().upper()
      print('-=' * 15)
      if perg == 'N':
            break

print()
print('-=' * 15)
print(f'X   Aproveitamento Dungeon   X')
print('-=' * 15)
print(f'{"No."}{"Name":>7}{"Andares":>13}{"Mobs":>8}')
for n in range(len(lista)):
      print(f'{n+1} -{lista[n]["name"]:>7}{lista[n]["andar"]:>10}{lista[n]["total"][0]:>10}')

print('-=' * 15)
while True:
    info = int(input('\nDigite o codigo na lista anterior para saber mais.\n'
                     'Caso queira sair DIGITE 0: '))
    if info == 0:
        break
    if info <= len(lista):
        print(f'\nDetalhes do {lista[info-1]["name"]}:\n'
              f'Subiu {lista[info-1]["andar"]} andares e matou {lista[info-1]["total"][0]} monstros.')
    elif info != 0 and info > len(lista):
        print('\033[31mO Codigo digitado nao existe\033[m')

print('\n-=-=-=-= Volte_Sempre =-=-=-=-=')


class Aventureiro:
    def __init__(self, name='', classe='', nivel='???', verificaçao=0):
        self.name = name
        self.classe = classe
        self.nivel = nivel
        self.verificaçao = verificaçao

    def dados(self):
        self.name = str(input('Qual seu NickName: '))
        self.classe = str(input('Qual sua Classe: '))
        self.nivel = int(input('Qual seu Nivel: '))

    def masmorra(self):
        if self.nivel < 10:
            print(f'Com o nivel atual de {self.nivel} voce so podera ir ate o 10º andar.')
            self.verificaçao = 10
        elif 10 < self.nivel < 30:
            print(f'Com o nivel atual de {self.nivel} voce so podera ir ate o 30º andar.')
            self.verificaçao = 30
        elif 30 < self.nivel < 60:
            print(f'Com o nivel atual de {self.nivel} voce so podera ir ate o 60º andar.')
            self.verificaçao = 60
        else:
            print(f'Com o nivel atual de {self.nivel} voce so podera ir em todos os andares.')
            self.verificaçao = 100

    def entrarmasmorra(self):
        perg = int(input('Qual andar: '))
        if self.verificaçao > perg:
            print(f'Bem vindo {self.name} ao andar {perg}, boa caçada.')
        else:
            print(f'infelizmente {self.name} voce ainda nao tem nivel suficiente para este andar.')



player = Aventureiro()
player.dados(), player.masmorra(), player.entrarmasmorra()