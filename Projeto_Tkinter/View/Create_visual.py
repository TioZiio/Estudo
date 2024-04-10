import tkinter as tk
from tkinter import ttk

class Create():
    def __init__(self, root):
        self.root = root

    def Janela(self, root):
        self.root.title("Menu")
        self.root.configure(background="#2F4F4F")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

    def Func_Criar_Caixas(self, relx, rely, relwidth, relheight, root):
        # Função que cria os Conteiners para armazenar os Botões, Labels e Entrys.
        caixa = tk.Frame(root, bd=4, bg="#B0C4DE", 
                         highlightbackground="#191970", highlightthickness=2)
        caixa.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return caixa
    
    def Func_Criar_Bt(self, caixa, text, relx, rely, relwidth, relheight, command=None):
        # Função para criação de Botões em Conteiners.
        botao = tk.Button(caixa, text=text, command=command)
        botao.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

    def Func_Criar_Lb(self, caixa, text, relx, rely, relwidth=None, relheight=None, fg=None, font=None):
        # Função para criação de Labels em Conteiners.
        label = tk.Label(caixa, text=text, fg=fg, bg="#B0C4DE", font=font)
        label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

    def Func_Criar_Entry(self, caixa, relx, rely, relwidth, relheight, options=None):
        # Função para criação de Entrys em Conteiners.
        entry = tk.Entry(caixa, show=options)
        entry.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return entry

    def Func_Criar_Cabecario_lista(self, valor, rotulo, frame):
        self.Lista_Treeview = self.root.nametowidget(frame)
        self.Lista_Treeview.heading(valor, text=rotulo, anchor=tk.CENTER)

    def Func_Criar_Colunas_Lista(self, valor, tamanho, frame):
        frame_local = frame
        self.Lista_Treeview = self.root.nametowidget(frame_local)
        self.Lista_Treeview.column(valor, width=tamanho, anchor=tk.CENTER)

    def Data_mes(self, mes):
        meses = {
            'JAN': '___01',
            'VEF': '___02',
            'MAR': '___03',
            'ABR': '___04',
            'MAI': '___05',
            'JUN': '___06',
            'JUL': '___07',
            'AGO': '___08',
            'SET': '___09',
            'OUT': '___10',
            'NOV': '___11',
            'DEZ': '___12'
        }
        temp = meses[mes] + '-%'
        return (temp, temp)
