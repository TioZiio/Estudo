import tkinter as tk
from tkinter import ttk
from View import Create_visual
import Model
import pandas as pd
import matplotlib.pyplot as plt
import locale

class Relatorios():
    def __init__(self, root):
        self.root_relatorio = root
        self.banco = Model.Main_db()
        self.create = Create_visual.Create(self.root_relatorio)
        
    def Janela_relatorio_mensal(self):
        self.root_treeview = tk.Toplevel(self.root_relatorio)
        self.root_treeview.title('Relatorio Mensal')
        self.root_treeview.configure(background="#2F4F4F")
        self.root_treeview.geometry("410x300")
        self.root_treeview.resizable(False, False)
        self.Tela_Relatorio_mensal()

    def Tela_Relatorio_mensal(self):
        self.caixa1 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.96, relheight=0.15, root=self.root_treeview
        )
        self.caixa2 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.2, relwidth=0.96, relheight=0.78, root=self.root_treeview
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
        treeview = ttk.Treeview(
            self.caixa2, columns=['PRODUTO', 'V. VENDA'], show='headings'
        )
        treeview.heading('PRODUTO', text='PRODUTO')
        treeview.heading('V. VENDA', text='V. VENDA')
        treeview.place(relx=0.5, rely=0.5,relwidth=0.95, relheight=0.82, anchor=tk.CENTER)
        for i, row in df_dados.iterrows():
            treeview.insert('', tk.END, values=(row['PRODUTO'], (f"R$ {row['V. VENDA']:.2f}")))

    def formatar_em_real(self, valor):
        return locale.currency(valor, grouping=True)

    def Relatorio_cliente(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        dados = self.banco.Relatorio_por_cliente()
        df_dados = pd.DataFrame(dados, columns=['COD CLIENTE', 'NOME', 'V.TOTAL'])
        df_dados_10 = df_dados.head(10)

        formatar_em_real = lambda x: locale.currency(x, grouping=True)
        plt.figure(figsize=(6,4))
        plt.bar(df_dados_10['NOME'], df_dados_10['V.TOTAL'], color='blue')
        plt.xlabel('Clientes')
        plt.ylabel('Compras do Cliente (R$)')
        plt.title('TOP 10 VENDAS POR CLIENTE')
        plt.show()
