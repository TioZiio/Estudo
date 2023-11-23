from Estoque_Loja import *
from Funçoes_Jogo import *
from time import sleep


def Interrupçao(x=False, y=False):
    """
    Funçao de Except Interrupt personalizada.
    x = Except Interrupt
    y = Except Type ou Value Error 
    """
    if x == True:
        return print('\n\033[31mO USUARIO PREFIRIU NAO DIGITAR.\033[m\n') 
    elif y == True:
        return print('Houve um Erro de Type ou Value.')

def decisao_produto():
    """
    Funçao para decidir qual categoria de produto.
    asking = Decisao de escolha da Classe dos produtos.
    """
    sleep(1)
    print(catalogo())
    sleep(0.7)
    while True:
        try:
            asking = int(input('\nO que vai ser pra hoje: '))
            if 0 <= asking <= 6:
                break
            elif asking == 7:
                sleep(1)
                carrinho()
                sleep(1.5)
                print(catalogo())
            else:
                print(f'O codigo {asking} digitado nao e Valido.')
                sleep(0.7)
        except (ValueError):
            Interrupçao(x='', y=True)
            sleep(0.7)
        except (KeyboardInterrupt):
            asking = 0
            Interrupçao(x=True, y='')
            break
    return asking

    

def adicionar_item():
    """
    Funçao para adicionar produtos ao carrinho.
    x = Valor para escolha da Classe do item (Armas, Comidas, Vestimentas, ...).
    quest = De acordo com a escolha do (x), pode escolher qual item de compra.
    quant = Valor da quantidade de itens pra compra.
    """
    sair = 0
    while True:
        x = decisao_produto()
        if x == 0:
            sair = 0
            break
        else:
            x -= 1 
        try:
            sleep(1.5)
            print(catalogo_itens(x))
            sleep(1)
            while True:
                quest = int(input('\nQual item hoje: '))
                if 0 < quest > controle(x):
                    break
                if quest == 0:
                    break
                else:
                    quant = int(input('Quantas unidades: '))
                    break
        except (KeyboardInterrupt):
            Interrupçao(x=True, y='')
            sleep(0.7)
            sair = 0
            break
        else:
            compras[0].append(itens(x, 0, 'item', quest-1))
            compras[2].append(itens(x, 1, 'valor', quest-1))
            compras[1].append(quant)
            compras[3].append((itens(x, 1, 'valor', quest-1)) * quant)
        sair = 1
    return sair

valor_total = []
compras = [[],[],[],[]]

def carrinho():
    """
    Funçao que mostra todos os valores da compra e seu total.
    Sao colocados na Lista compras[] com a funçao adicionar_item().
    """
    print()
    print('-=' * 28)
    print(f' \033[1;36m{"CARRINHO":^54}\033[m{"|"}')
    print('-=' * 28)
    print(f'\033[35m{"No.":<3} - {"Produtos":^18}\033[m - \033[35m{"Qt.":^7} \033[m-\033[35m '
        f'{"V.Unt.":^7}\033[m -\033[35m {"Total":^7}\033[m {"|":>1}')
    print(f'{"|":>56}')
    for d in range(len(compras[0])):
        print(f'{d+1:^3} - {compras[0][d]:^18} - {compras[1][d]:^7} - {compras[2][d]:^7} - \033[1;31m{compras[3][d]:^7}\033[m {"|":<2}')
    print(f'{"|":>56}')
    print('-=' * 28)
    global total
    total = sum(compras[3])
    valor_total.append(total)
    print(f'Valor Total:  \033[1;31mR${total:<39.1f}\033[m{"|"}')
    print('-=' * 28)



def excluir():
    """
    Funçao para remover itens do carrinho.
    asking = Referente a decisao de remover ou nao.
    asking_rem = Referente a pergunta de qual item remover.
    """
    while True:
        try:
            sleep(1)
            carrinho()
            sleep(1.5)
            asking = str(input('Quer retirar algum item [S/N]: ')).upper()[0].strip()
            if asking == 'S':
                sleep(0.7)
                print('\nEscolha o item pelo numero respectivo no CARRINHO')
                asking_rem = int(input('Qual item: '))
                compras[0].pop((asking_rem-1)), compras[1].pop((asking_rem-1)), compras[2].pop((asking_rem-1)), compras[3].pop(asking_rem-1)
            elif asking == 'N':
                break
            else:
                print('Nao entendi oque disse.')
        except (IndexError, ValueError):
            Interrupçao(x='', y=True)
            sleep(1)
            continue
        except (KeyboardInterrupt):
            Interrupçao(x=True, y='')
            break
    return print(f'O Valor Total a ser pago é \033[1;31m{valor_total[0]}dels\033[m')


def Principal():
    """
    Funçao principal do sistema, para decidir entre Loja e Jogo.
    asking = Ponto de decisao do sistema.
    """
    while True:
        try:
            print('\n[1] Loja\n[2] Jogo de Adivinhar\n[0] Para sair')
            asking = int(input('Qual App quer entrar: '))
            if asking == 1:
                try:
                    adicionar_item()
                except (KeyboardInterrupt):
                    Interrupçao()
                    break
                excluir()
                break
            elif asking == 2:
                print('---------JOGO DE ADIVINHAÇAO--------')
                print('\nVamos começar...\n'), sleep(1)
                jogador = Jogador('David', 'Mago')
                jogador.escolha_classe()
                jogador.jogar()
                break
            elif asking == 0:
                print('Volte sempre que quiser...')
                break
            else:
                print('Nao entendi...')
                sleep(1)
        except (ValueError, TypeError):
            Interrupçao(x='', y=True)
            sleep(1)
            continue
        except (KeyboardInterrupt):
            Interrupçao(x=True, y='')
            break


Principal()