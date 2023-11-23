
def catalogo():
    """
    Funçao do Catalago principal do sitema.
    """
    resultado = f'\n\033[1;31m{"CATALOGO":=^30}\033[m\n' \
                f'[1] \033[32mComidas\033[m\n[2] \033[32mArmas\033[m\n[3] \033[32mVestimentas\033[m\n' \
                f'[4] \033[32mAneis\033[m\n[5] \033[32mColares\033[m\n[6] \033[32mPoçoes Magicas\033[m\n' \
                f'[7] \033[1;36mCarrinho\033[m\n\033[31m[0] Para sair !!!\033[m'
    return resultado


def catalogo_itens(x):
    """
    x = Referente a um Catalago da lista Resultado.
    """
    resultado = [f'\n\033[31m{"COMIDAS":=^30}\033[m\n'
                 f'[1] \033[32mComida Promoçao\033[m - \033[35m30dels\033[m\n'
                 f'[2] \033[32mComida Cara\033[m - \033[35m55dels\033[m\n'
                 f'[3] \033[32mTorta de NitsZel\033[m - \033[35m120dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m',  # lista [0]

                 f'\n\033[31m{"ARMAS":=^30}\033[m\n'
                 f'[1] \033[32mArco\033[m - \033[35m100dels\033[m\n'
                 f'[2] \033[32mFlechas\033[m - \033[35m1del / 2 flechas\033[m\n'
                 f'[3] \033[32mAdaga\033[m - \033[35m110dels\033[m\n'
                 f'[4] \033[32mEspada Grande\033[m - \033[35m115dels\033[m\n'
                 f'[5] \033[32mEscudo\033[m - \033[35m80dels\033[m\n'
                 f'[6] \033[32mCajado\033[m - \033[35m100dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m',  # lista [1]

                 f'\n\033[31m{"VESTIMENTAS:=^30"}\033[m\n'
                 f'[1] \033[32mCota Malha de Aço\033[m - \033[35m115dels\033[m\n'
                 f'[2] \033[32mArmadura Leve\033[m - \033[35m140dels\033[m\n'
                 f'[3] \033[32mTunica\033[m - \033[35m125dels\033[m\n'
                 f'[4] \033[32mArmadura Pesada\033[m \033[35m150dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m',  # lista [2]

                 f'\n\033[31m{"ANEIS":=^30}\033[m\n'
                 f'[1] \033[32mAnel de Critico\033[m - \033[35m90dels\033[m\n'
                 f'[2] \033[32mAnel de Dano\033[m - \033[35m95dels\033[m\n'
                 f'[3] \033[32mAnel de Esquiva\033[m - \033[35m85dels\033[m\n'
                 f'[4] \033[32mAnel de Magia\033[m - \033[35m95dels\033[m\n'
                 f'[5] \033[32mAnel de Mana\033[m - \033[35m90dels\033[m\n'
                 f'[6] \033[32mAnel de Proteçao\033[m - \033[35m95dels\033[m\n'
                 f'[7] \033[32mAnel de Resistencia\033[m - \033[35m90dels\033[m\n'
                 f'[8] \033[32mAnel de Sorte\033[m - \033[35m85dels\033[m\n'
                 f'[9] \033[32mAnel de Velocidade\033[m - \033[35m85dels\033[m\n'
                 f'[10] \033[32mAnel de Vida\033[m - \033[35m95dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m',  # lista [3]

                 f'\n\033[31m{"COLARES":=^30}\033[m\n'
                 f'[1] \033[32mColar de Critico\033[m - \033[35m110dels\033[m\n'
                 f'[2] \033[32mColar de Dano\033[m - \033[35m115dels\033[m\n'
                 f'[3] \033[32mColar de Magia\033[m - \033[35m115dels\033[m\n'
                 f'[4] \033[32mColar de Mana\033[m - \033[35m100dels\033[m\n'
                 f'[5] \033[32mColar de Proteçao\033[m - \033[35m115dels\033[m\n'
                 f'[6] \033[32mColar de Sorte\033[m - \033[35m100dels\033[m\n'
                 f'[7] \033[32mColar de Velocidade\033[m - \033[35m100dels\033[m\n'
                 f'[8] \033[32mColar de Vida\033[m -\033[35m120dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m',  # lista [4]

                 f'\n\033[31m{"POÇOES MAGICAS":=^30}\033[m\n'
                 f'[1] \033[32mPoçao Cura Menor\033[m - \033[35m35dels\033[m\n'
                 f'[2] \033[32mPoçao Cura NitsZel\033[m - \033[35m100dels\033[m\n'
                 f'[3] \033[32mPoçao Mana Menor\033[m - \033[35m30dels\033[m\n'
                 f'[4] \033[32mPoçao Mana Nitszel\033[m - \033[35m90dels\033[m\n'
                 f'\033[31m[0] Para sair !!!\033[m'  # lista [5]

                 ]
    return resultado[x]



def itens(x=0, y=0, name='', z=0):
    """
    x = Refente a lista (Produtos)
    y = Referente ao item na lista (Comida, Armas, Vestimentas, Anel, colar, Poçoes)
    name = Refente ao item ou valor (Nomes dos itens ou valores deles)
    z = Referente ao produto escolhido pelo name
    """
    produtos = [[{"item": ['Comida Promoçao', 'Comida Cara', 'Torta de NitsZel']},
                 {"valor": [30, 55, 120]}],

                [{"item": ['Arco', 'Flechas', 'Adaga', 'Espada Grande', 'Escudo', 'Cajado']},
                 {"valor": [100, 1, 110, 115, 80, 100]}],

                [{"item": ['Cota Malha de Aço', 'Armadura leve', 'Tunica', 'Armadura Pesada']},
                 {"valor": [115, 140, 125, 150]}],

                [{"item": ['Anel de Critico', 'Anel de Dano', 'Anel de Esquiva', 'Anel de Magia', 'Anel de Mana',
                           'Anel de Protecao', 'Anel de Resistencia', 'Anel de Sorte', 'Anel de Velocidade',
                           'Anel de Vida']},
                 {"valor": [90, 95, 85, 95, 90, 95, 90, 85, 85, 95]}],

                [{"item": ['Colar de Critico', 'Colar de Dano', 'Colar de Magia', 'Colar de Mana',
                           'Colar de Proteçao', 'Colar de Sorte', 'Colar Velocidade', 'Colar de Vida']},
                 {"valor": [110, 115, 115, 100, 115, 100, 100, 120]}],

                [{"item": ['Poçao Cura Menor', 'Poçao Cura NitsZel',
                           'Poçao Mana Menor', 'Poçao Mana Nitszel']},
                 {"valor": [35, 100, 30, 90]}]]
                 
    return produtos[x][y][name][z]


def controle(y):
    """
    Funçao para controlar quantidade de itens que podem ser retirados
    """
    if y == 0:
        return 3
    elif y == 1:
        return 6
    elif y == 2:
        return 4
    elif y == 3:
        return 10
    elif y == 4:
        return 8
    elif y == 5:
        return 4
