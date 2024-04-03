import tkinter as tk
from tkinter import ttk
import Model
import pandas as pd

class Relatorios():
    def __init__(self, root):
        self.root_relatorio = root
        self.banco = Model.Main_db()

    def ToolBar(self):
        self.menubar = tk.Menu(self.root_relatorio)
        self.root_relatorio.config(menu=self.menubar)
        self.menutool_Opcao = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Relatorios", menu=self.menutool_Opcao)

        self.menutool_Opcao.add_command(label="Vendas Mensais", command=self.Relatorios_vendas)
        self.menutool_Opcao.add_command(label="Tela Vendas")
        self.menutool_Opcao.add_command(label="Quit", command=self.root_relatorio.quit) 
        
    def Janela_relatorio_mensal(self):
        self.root_treeview = tk.Toplevel(self.root_relatorio)
        self.root_treeview.title('Relatorio Mensal')
        self.root_treeview.configure(background="#2F4F4F")
        self.root_treeview.geometry("410x200")
        self.root_treeview.resizable(False, False)
        self.treeview = ttk.Treeview(
            self.root_treeview, columns=['PRODUTO', 'V. VENDA'], show='headings'
        )
        self.treeview.heading('PRODUTO', text='PRODUTO')
        self.treeview.heading('V. VENDA', text='V. VENDA')
        self.treeview.place(relx=0.5, rely=0.5,relwidth=0.95, relheight=0.82, anchor=tk.CENTER)
        self.inserir_dados()

    def inserir_dados(self):
        for i, row in self.df_dados.iterrows():
            self.treeview.insert('', tk.END, values=(row['PRODUTO'], (f"R$ {row['V. VENDA']:.2f}")))

    def Relatorios_vendas(self):
        query = """SELECT nome_produto, SUM(valor_venda) as valores
                FROM vendas
                WHERE data LIKE ?
                GROUP BY nome_produto
                UNION ALL
                SELECT 'Total', SUM(valor_venda)
                FROM vendas
                WHERE data LIKE ?;"""
        parametros = ('%_3','%_3')
        dados = self.banco.Organiza_query_db(typTela='relatorio', query=query, parametros=parametros)
        self.df_dados = pd.DataFrame(dados, columns=['PRODUTO', 'V. VENDA'])
        self.Janela_relatorio_mensal()