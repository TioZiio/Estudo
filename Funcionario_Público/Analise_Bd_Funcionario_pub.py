import pandas as pd
import locale
import matplotlib.pyplot as plt
import numpy as np

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

arquivo = 'remuneracaoServidores.csv'
dados = pd.read_csv(
    arquivo, sep=';',  decimal=',', dtype={
        'BRUTO': float, 'LÍQUIDO': float, 'REMUNERAÇÃO BÁSICA': float, 'FUNÇÃO': str 
    },
    converters={'ÓRGÃO': str.strip}
)
dados['SITUAÇÃO'] = dados['SITUAÇÃO'].str.upper().str.strip().replace('', pd.NA)
dados['FUNÇÃO'] = dados['FUNÇÃO'].str.lower().str.strip().replace('', pd.NA)

def espaço_amostral():
    # 1
    print('Qual o espaço amostral compreendido nesta base de dados?\n  |->', end='')
    return print(f" {dados.shape[0]} linhas e {dados.shape[1]} colunas\n")

def corpo_bombeiros():
    # 2 
    # Foi necessário utilzar 3 codigos de órgãos pois a dois orgãos de corpo de bombeiro,
    # sendo um deles com 2 codigos e o outro com apenas 1. Eles são diferentes na escrita também.
    print('Quantos servidores estão lotados no corpo de bombeiros?\n  |->', end='')
    cod_bombeiro = [1699072, 1599072, 100212]
    quant_bombeiros = [(dados['CÓDIGO DO ÓRGÃO'] == cod).sum() for cod in cod_bombeiro]
    total = lambda x, y, z: x + y + z
    print(f' Possui {total(*quant_bombeiros)} bombeiros\n')

def quant_funcionarios():
    # 3
    print('Qual o órgão público com maior número de funcionários?\n  |->', end='')
    quant_funcionarios = dados['ÓRGÃO'].value_counts()
    maior_orgao_funcionario = quant_funcionarios.idxmax()
    num_maior_orgao_funcionario = quant_funcionarios.max()
    print(f'A {maior_orgao_funcionario} possui o maior número de funcionários, com {num_maior_orgao_funcionario}\n')

def probabilidade_educacao():
    # 4
    print('Qual a probabilidade de ao escolher uma linha ao acaso, ser de um', end=' ')
    print('funcionário que trabalha na secretaria de educação?\n  |->', end='')
    educacao = (dados['CÓDIGO DO ÓRGÃO'] == 100652).sum()
    probabilidade = (educacao / int(dados.shape[0])) * 100
    print(f' A probabilidade: {probabilidade:.2f}%\n')

def profissoes():
    # 5
    tratamento = (dados['FUNÇÃO'].str.lower().str.strip().replace('', pd.NA).dropna()).unique()
    contagem_profissoes = len(tratamento)
    print('Liste todas as funções contidas na base.\n  |-> Profissões:')
    print(f'{tratamento}\n Total: {contagem_profissoes}')

def media_salarial():
    # 6
    print('Qual órgão publico possui a maior média salarial?\n  |->', end='')
    media = dados.groupby(['ÓRGÃO'])['BRUTO'].mean()
    print(f' {media.idxmax()} com valor de {locale.currency(media.max(), grouping=True)}\n')

def maior_remuneraçao_basica_individual():
    # 7
    print('O servidor com maior remuneração básica pertence a qual órgão?\n  |->', end='')
    remuneraçao = dados['REMUNERAÇÃO BÁSICA'].max(); orgao_remuneraçao = dados['REMUNERAÇÃO BÁSICA'].idxmax()
    print(f" {dados['ÓRGÃO'][orgao_remuneraçao]} com valor de {locale.currency(remuneraçao, grouping=True)}\n")

def valor_pago_todos_funcionarios():
    # 8
    print('Qual o valor pago para todos os funcionários públicos?\n  |-> ', end='')
    remuneraçao_bruta = dados['BRUTO'].sum()
    print(f'Valor total bruto: {locale.currency(remuneraçao_bruta, grouping=True)}')
    remuneraçao_liquida = dados['LÍQUIDO'].sum()
    print(f'  |-> Valor total líquido: {locale.currency(remuneraçao_liquida, grouping=True)}\n')

def grafico_pizza():
    # 9
    print('Elabore um gráfico de pizza com a remuneração bruta dos servidores por orgão\n')
    salarios = dados.groupby(['ÓRGÃO'])['BRUTO'].sum()
    top_n = 8
    top_salarios = salarios.nlargest(top_n)
    salario_restante = salarios.drop(top_salarios.index).sum()
    top_salarios['Outros 104 Órgãos'] = salario_restante

    formatar_em_real = lambda x: locale.currency(x, grouping=True)
    plt.pie(top_salarios, labels=top_salarios.index, 
            autopct=lambda pct: formatar_em_real(pct * sum(top_salarios.values) / 100), startangle=260)
    plt.title(f'Top {top_n} Salários Brutos dos Servidores por Órgão')
    plt.axis('equal')
    plt.show()

def boxplot():
    # 10
    print('Elabore um gráfico de boxplot com a situação do servidor e sua remuneração liquida\n')
    top_10_situacoes = dados['SITUAÇÃO'].value_counts().nlargest(9).index[2:]

    dados_top = dados[dados['SITUAÇÃO'].isin(top_10_situacoes)]
    dados_top.boxplot(column='LÍQUIDO', by='SITUAÇÃO')
    plt.show()

def medidas_dispercao():
    # 11
    print("""Identifique qual órgão possui salário liquido com menos variações, 
    utilizando para isto medidas de dispersão.\n""")
    desvio_padrao = dados.groupby(['ÓRGÃO'])['LÍQUIDO'].std()
    media = dados.groupby(['ÓRGÃO'])['LÍQUIDO'].mean()
    calc = lambda x, y: (x / y) * 100
    result = (calc(desvio_padrao, media)).sort_values()
    print(f'O {result.idxmin()} possui a menor variação com valor de {result.min():.2f}%')
    print(f'O {result.idxmax()} possui a maior variação com valor de {result.max():.2f}%\n')

def indice_correlacao():
    print("""Calcule o índice de correlação entre o IRRF e os salários liquido e bruto. Em
    qual dos casos o índice de correlação foi maior?""")
    correlacao_irrf_Lq = dados['IRRF'].corr(dados['LÍQUIDO'])
    correlacao_irrf_Bt = dados['IRRF'].corr(dados['BRUTO'])
    print(f'Correlação de IRRF e LÍQUIDO: {round(correlacao_irrf_Lq, 5)}')
    print(f'Correlação de IRRF e BRUTO: {round(correlacao_irrf_Bt, 5)}')
    print('Logo, a correlação de BRUTO e maior que a correlação de LÍQUIDO\n')

def nova_coluna():
    """
    Adicione uma nova coluna que irá conter a diferença entre o salario bruto e
    liquido, e responda as seguintes questões;
    a. Qual a correlação entre o IRRF pago e esta nova coluna?
    b.Qual órgão apresenta índice de correlação entre IRRF e diferença salarial maior?"""
    dados['DIFERENÇA'] = dados['BRUTO'] - dados['LÍQUIDO']
    correlacao_irrf_Dif = dados['IRRF'].corr(dados['DIFERENÇA'])
    print(f'O Valor da correlação entre IRRF e diferença de BRUTO - LÍQUIDO é: {round(correlacao_irrf_Dif, 5)}')
    pd.set_option('display.max_rows', None)
    correlacoes_por_orgao = dados.groupby('ÓRGÃO').apply(lambda x: x['IRRF'].corr(x['DIFERENÇA']))
    orgao_maior_correlacao = correlacoes_por_orgao.idxmin()
    maior_correlacao = correlacoes_por_orgao.min()
    print(
        f"""O órgão com o maior índice de correlação entre IRRF e 
    diferença salarial é {orgao_maior_correlacao}, com uma correlação de {round(maior_correlacao, 5)}.
        """
    )

if __name__ == '__main__':
    espaço_amostral()
    corpo_bombeiros()
    quant_funcionarios()
    probabilidade_educacao()
    profissoes()
    media_salarial()
    maior_remuneraçao_basica_individual()
    valor_pago_todos_funcionarios()
    grafico_pizza()
    boxplot()
    medidas_dispercao()
    indice_correlacao()
    nova_coluna()