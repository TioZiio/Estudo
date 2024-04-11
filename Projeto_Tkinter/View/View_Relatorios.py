import tkinter as tk
from tkinter import ttk, messagebox
from View import Create_visual
from Model import Model_Func
import pandas as pd
import matplotlib.pyplot as plt
import locale
from Control import Control_Principal

class Relatorios():
    def __init__(self, root):
        self.root_temp = root
        self.banco = Model_Func.Func_db()
        self.create = Create_visual.Create(self.root_temp)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        
    def Janela_relatorio(self):
        self.root_relatorio = tk.Toplevel(self.root_temp)
        self.root_relatorio.title('Relatorios')
        self.root_relatorio.configure(background="#2F4F4F")
        self.root_relatorio.geometry("410x300")
        self.root_relatorio.resizable(True, True)
    
    def Infos_Relatorios_mensal(self):
        self.caixa1 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15, root=self.root_relatorio
        )
        self.caixa2 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.2, relwidth=0.96, relheight=0.78, root=self.root_relatorio
        )
        botoes = [
            (self.caixa1, 'JAN', 0.0, 0.02, 0.165, 0.5, 
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('JAN'))),
            (self.caixa1, 'VEF', 0.165, 0.02, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('VEF'))),
            (self.caixa1, 'MAR', 0.33, 0.02, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('MAR'))),
            (self.caixa1, 'ABR', 0.495, 0.02, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('ABR'))),
            (self.caixa1, 'MAI', 0.66, 0.02, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('MAI'))),
            (self.caixa1, 'JUN', 0.825, 0.02, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('JUN'))),
            (self.caixa1, 'JUL', 0.0, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('JUL'))),
            (self.caixa1, 'AGO', 0.165, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('AGO'))),
            (self.caixa1, 'SET', 0.33, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('SET'))),
            (self.caixa1, 'OUT', 0.495, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('OUT'))),
            (self.caixa1, 'NOV', 0.66, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('NOV'))),
            (self.caixa1, 'DEZ', 0.825, 0.5, 0.165, 0.5,
                lambda: self.Relatorio_mensal(mes=self.create.Data_mes('DEZ')))
        ]
        for info in botoes:
            self.create.Func_Criar_Bt(*info)

    def Relatorio_mensal(self, mes):
        dados = self.banco.Relatorio_mensal(parametros=mes)
        if dados[0][1] == None:
            dados = [('Total', 0)]
        df_dados = pd.DataFrame(dados, columns=['PRODUTO', 'V. VENDA'])
        self.treeview_relatorio(dados=df_dados)

    def treeview_relatorio(self, dados):
        treeview = ttk.Treeview(
            self.caixa2, columns=['PRODUTO', 'V. VENDA'], show='headings'
        )
        treeview.heading('PRODUTO', text='PRODUTO')
        treeview.heading('V. VENDA', text='V. VENDA')
        treeview.place(relx=0.5, rely=0.5,relwidth=0.95, relheight=0.82, anchor=tk.CENTER)
        for i, row in dados.iterrows():
            treeview.insert('', tk.END, values=(row['PRODUTO'], (f"R$ {row['V. VENDA']:.2f}")))

    def Relatorio_cliente(self):
        dados = self.banco.Relatorio_por_cliente()
        df_dados = pd.DataFrame(dados, columns=['COD CLIENTE', 'NOME', 'V.TOTAL'])
        df_dados_10 = df_dados.head(10)
        plt.figure(figsize=(6,4))
        plt.bar(df_dados_10['NOME'], df_dados_10['V.TOTAL'], color='blue')
        plt.xlabel('Clientes')
        plt.ylabel('Compras do Cliente (R$)')
        plt.title('TOP 10 VENDAS POR CLIENTE')
        plt.show()

    def Infos_Relatorios_investimento(self):
        self.caixa1 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2, root=self.root_relatorio
        )
        self.caixa2 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.25, relwidth=0.96, relheight=0.73, root=self.root_relatorio
        )
        rotulos_info = [
            (self.caixa1, "Codigo", 0.02, 0.0),
            (self.caixa1, "Produto", 0.2, 0.0),
            (self.caixa1, "Valor", 0.55, 0.0)
        ]
        entradas_info = [
            (0.02, 0.35, 0.16, 0.4),
            (0.2, 0.35, 0.3, 0.4),
            (0.55, 0.35, 0.15, 0.4)
        ]
        self.quant_entrys = []
        for info in zip(rotulos_info, entradas_info):
            self.create.Func_Criar_Lb(*info[0])
            entry = self.create.Func_Criar_Entry(self.caixa1, *info[1])
            self.quant_entrys.append(entry)

    def Processamento_dados_investimento(self):
        dados = self.controle.Puxa_dados()
        if dados['cod.invest'] == '':
            if dados['produto'] == '' or dados['valor'] == '':
                messagebox.showerror('Erro', 'Produto ou Valor não inserido')
            else:
                if ',' in dados['valor']:
                    alt = float(dados['valor'].replace(',', '.').strip())
                    dados['valor'] = alt
                self.controle.Limpar_entrys()
                return dados
        else:
            self.controle.Limpar_entrys()
            return dados

    def botoes_investimento(self):
        botoes_info = [
            (self.caixa1, "Adicionar", 0.8, 0.1, 0.2, 0.4,
                lambda: self.Funcs_Investimentos('add')),
            (self.caixa1, "Apagar", 0.8, 0.5, 0.2, 0.4,
                lambda: self.Funcs_Investimentos('del'))
        ]
        for info in botoes_info:
            self.create.Func_Criar_Bt(*info)

    def formatar_em_real(self, valor):
        return locale.currency(valor, grouping=True)

    def Atualiza_dados(self):
        df_dados = pd.DataFrame(
            self.banco.Func_Select_Lista(typTela='investimento'), columns=['Cod.Produto','Produto', 'Valor']
        )
        df_dados['Valor'] = df_dados['Valor'].apply(self.formatar_em_real)
        self.textos = tk.Text(self.caixa2)
        self.textos.insert(tk.END, df_dados.to_string(index=False, justify='center'))
        self.textos.pack()

    def Atualiza_texto(self):
        self.textos.destroy()

    def Funcs_Investimentos(self, typFunc):
        if typFunc == 'add':
            self.banco.Adicionar_investimento(dados=self.Processamento_dados_investimento())
        elif typFunc == 'del':
            self.banco.Apagar_investimentos(dados=self.Processamento_dados_investimento())
        self.Atualiza_texto()
        self.Atualiza_dados()
        
    def Log_Clientes_Novos(self):
        dados = self.banco.Log_Clientes_Novos()
        df_dados = pd.DataFrame(dados, columns=['CODIGO', 'NOME', 'TELEFONE', 'ENDERECO'])
        self.caixa3 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.98, relheight=0.98, root=self.root_relatorio
        )
        self.textos = tk.Text(self.caixa3)
        self.textos.insert(tk.END, df_dados.to_string(index=False, justify='center'))
        self.textos.pack()

    def Organiza_Funcs_Relatorios(self, typFunc):
        self.Janela_relatorio()
        match typFunc:
            case 'mensal':
                self.Infos_Relatorios_mensal()
            case 'investimento':
                self.Infos_Relatorios_investimento()
                self.controle = Control_Principal.Principal(root=self.root_relatorio, entrys=self.quant_entrys)
                self.botoes_investimento()
                self.Atualiza_dados()
            case 'clientes_novos':
                self.Log_Clientes_Novos()