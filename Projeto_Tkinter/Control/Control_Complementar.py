from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from View import View_Relatorios


class Funcs_Complementar():
    def __init__(self, root):
        self.root_complementar = root
        self.relatorios = View_Relatorios.Relatorios(self.root_complementar)
        
    def Transform_frames(self, frame):
        frame = self.root_complementar.nametowidget(frame)
        return frame

    def Data(self):
        data_atual = datetime.now().date()
        return data_atual.strftime('%d-%m-%Y')

    def Janela_mensagem_erro(self, mensagem='Cliente ou produto não cadastrado'):
        messagebox.showerror('Erro', mensagem)

    def ToolBar(self):
        self.menubar = tk.Menu(self.root_complementar)
        self.root_complementar.config(menu=self.menubar)
        self.menutool_Opcao = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Relatorios", menu=self.menutool_Opcao)

        self.menutool_Opcao.add_command(
            label="Vendas Mensais", command=lambda: self.relatorios.Organiza_Funcs_Relatorios(typFunc='mensal')
        )
        self.menutool_Opcao.add_command(label="Vendas por Cliente", command=self.relatorios.Relatorio_cliente)
        self.menutool_Opcao.add_command(
            label='Investimento', command=lambda: self.relatorios.Organiza_Funcs_Relatorios(typFunc='investimento')
        )
        self.menutool_Opcao.add_command(
            label="Novos Clientes", command=lambda: self.relatorios.Organiza_Funcs_Relatorios(typFunc='clientes_novos')
        )
        self.menutool_Opcao.add_command(label="Quit", command=self.root_complementar.quit)
        