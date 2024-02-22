import tkinter as tk
from tkinter import ttk
import Control
import Model

class Create():
    def __init__(self, root):
        self.root = root

    def Janela(self, root):
        self.root.title("Menu")
        self.root.configure(background="#2F4F4F")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

    def Func_Criar_Caixas(self, relx, rely, relwidth, relheight):
        # Função que cria os Conteiners para armazenar os Botões, Labels e Entrys.
        caixa = tk.Frame(self.root, bd=4, bg="#B0C4DE", 
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

    def Func_Criar_Cabecario_lista(self, valor, rotulo):
        frame = '.!frame3.!treeview'
        self.Lista_Treeview = self.root.nametowidget(frame)
        self.Lista_Treeview.heading(valor, text=rotulo, anchor=tk.CENTER)

    def Func_Criar_Colunas_Lista(self, valor, tamanho):
        frame = '.!frame3.!treeview'
        self.Lista_Treeview = self.root.nametowidget(frame)
        self.Lista_Treeview.column(valor, width=tamanho, anchor=tk.CENTER)

    def Func_Erro_Dados(self, root, frase="Dados inseridos Incorretamente."):
        frame = '.!frame2'
        self.frame_lista = self.root.nametowidget(frame)
        self.error = tk.Label(self.frame_lista, text=frase, fg="red", bg="#B0C4DE")
        self.error.place(relx=0.3, rely=0.8)

    def Func_Validar_user(self):
        dados = self.controle.Puxa_dados()
        dados[0] = 'david'; dados[1] = '123'
        if not dados[0] and not dados[1]:
            self.Info_Labls_Inicial_Erro()
        else:
            if dados[0] == 'david' and dados[1] == '123':
                self.caixa0.destroy()
                self.Organiza_Funcs_Vendas()
            else:
                self.Info_Labls_Inicial_Erro()

    def ToolBar(self):
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.menutool_Opcao = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Opções", menu=self.menutool_Opcao)

        self.menutool_Opcao.add_command(label="Tela Clientes")
        self.menutool_Opcao.add_command(label="Tela Vendas", command=self.Organiza_Funcs_Vendas)
        self.menutool_Opcao.add_command(label="Quit", command=self.root.quit) 

class Infos():        
    def Tela_Inicial(self):
        self.caixa0 = self.Func_Criar_Caixas(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.3)
        
    def Info_Labls_Inicial(self):
        # Informações para criar as Labls da Tela de Login.
        botoes_info = [
            (self.caixa0, "Usuário", 0.45, 0.13),
            (self.caixa0, "Senha", 0.45, 0.48)]
        for info in botoes_info:
            self.Func_Criar_Lb(*info)

    def Info_Entrys_Inicial(self):
        # Informações para criar as Entrys da Tela de Login.
        entradas_info = [
            (0.2, 0.25, 0.6, 0.15),
            (0.2, 0.6, 0.6, 0.15, "*")]
        self.quant_entrys_inicial = []
        for info in entradas_info:
            entry = self.Func_Criar_Entry(self.caixa0, *info)
            self.quant_entrys_inicial.append(entry)

    def Info_Btoes_Inicial(self):
        # Informações para criar os Botões da Tela de Login.
        info = [
            (self.caixa0, "Validar", 0.3, 0.8, 0.4, 0.1, lambda: self.Func_Validar_user())]
        self.Func_Criar_Bt(*info[0])

    def Info_Labls_Inicial_Erro(self):
        self.Func_Criar_Lb(self.caixa0, text='Usuario ou senha Inválido', relx=0.3, rely=0.0, fg='red')

    def Tela_Vendas(self):
        # Conteiner 1
        self.caixa1 = self.Func_Criar_Caixas(relx=0.02, rely=0.02, relwidth=0.65, relheight=0.3)
        # Conteiner 2
        self.caixa2 = self.Func_Criar_Caixas(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6)
        # Conteiner 3
        self.caixa3 = self.Func_Criar_Caixas(relx=0.7, rely=0.02, relwidth=0.28, relheight=0.3)

    def Info_Labls_Vendas(self):
        # Informações para criar as Labels da Tela de Vendas.
        # Variavel rotulos_info recebe respectivamente (caixa, nome, relx, rely)
        fonte = ('Arial', 14)
        rotulos_info = [
            (self.caixa1, "Cod. Venda", 0.02, 0.02),
            (self.caixa1, "Cod. Produto", 0.02, 0.3, 0.13),
            (self.caixa1, "Valor", 0.25, 0.3),
            (self.caixa1, "Cod. Cliente", 0.4, 0.3, 0.13),
            (self.caixa3, "Pacote Mini 25gr {:_>11}".format("001"), 0, 0.05),
            (self.caixa3, "Pacote Cone 45gr {:_>10}".format("002"), 0, 0.2),
            (self.caixa3, "Pacote Pequeno 100gr {:_>6}".format("003"), 0, 0.35),
            (self.caixa3, "Pacote Grande 250gr {:_>7}".format("004"), 0, 0.5),
            (self.caixa3, "Piposqueira {:_>15}".format("005"), 0, 0.65),
            (self.caixa3, "Kit. Degustação {:_>12}".format("006"), 0, 0.8)
        ]
        for info in rotulos_info:
            if info[0] == self.caixa3:
                rotulo = self.Func_Criar_Lb(*info, font=fonte)
            else:
                rotulo = self.Func_Criar_Lb(*info)
            
    def Info_Entrys_Vendas(self):
        # Informações para criar as Entrys da Tela de Vendas.
        # Variavel entradas_info recebe respectivamente (relx, rely, relwidth, relheight)
        entradas_info = [
            (0.02, 0.15, 0.1, 0.15),
            (0.02, 0.45, 0.15, 0.15),
            (0.2, 0.45, 0.15, 0.15),
            (0.38, 0.45, 0.15, 0.15),
        ]
        self.quant_entrys = []
        for info in entradas_info:
            entry = self.Func_Criar_Entry(self.caixa1, *info)
            self.quant_entrys.append(entry)

    def Info_Btoes_Vendas(self):
        self.banco = Model.Main_db(self.root)
        botoes_info = [
            (self.caixa1, "Limpar Tela", 0.51, 0.05, 0.13, 0.15, 
                lambda: self.controle.Limpar_entrys()),
            (self.caixa1, "Adicionar", 0.64, 0.05, 0.13, 0.15, 
                lambda: self.Atualiza_db(value='add', verificar=True)),
            (self.caixa1, "Alterar", 0.77, 0.05, 0.1, 0.15, 
                lambda: self.Atualiza_db(value='alt', verificar=False)),
            (self.caixa1, "Apagar", 0.87, 0.05, 0.1, 0.15, 
                lambda: self.Atualiza_db(value='del', verificar=False))
        ]
        for info in botoes_info:
            botao = self.Func_Criar_Bt(*info)

    def Info_Cabecario_Vendas(self):
        info_cabecario = [
            ("#1", "Cod VENDA"), ("#2", "Cod PROD"), ("#3", "PRODUTO"), ("#4", "VALOR"),
            ("#5", "Cod CLNT"), ("#6", "NOME"), ("#7", "DATA")
        ]
        for info in info_cabecario:
            self.Func_Criar_Cabecario_lista(*info)

    def Info_Colunas_Vendas(self):
        info_colunas = [
            ("#0", 1),("#1", 30),("#2", 100),("#3", 160),
            ("#4", 100),("#5", 95), ("#6", 210), ("#7", 160)
        ]
        for info in info_colunas:
            self.Func_Criar_Colunas_Lista(*info)

    def Info_Cod_Produto(self, codigo=0):
        produtos = ["Erro", "Mini 25gr", "Cone 45gr", "Pacote 100gr", "Pacote 250gr", "Piposqueira", "Kit Degustação"]
        nome_produto = produtos[int(codigo)]
        return nome_produto

class Organiza_Funcs_IV(Create, Infos):
    def Organiza_Funcs_Inicial(self):
        self.Tela_Inicial()
        self.Info_Entrys_Inicial()
        self.controle = Control.Controller(self.root, entrys=self.quant_entrys_inicial)
        self.Info_Btoes_Inicial()
        self.Info_Labls_Inicial()

    def Organiza_Funcs_Vendas(self):
        self.Tela_Vendas()
        self.ToolBar()
        self.Info_Entrys_Vendas()
        self.controle = Control.Controller(self.root, entrys=self.quant_entrys)
        self.controle.Func_Criar_Treeview()
        self.Info_Btoes_Vendas()
        self.Info_Labls_Vendas()
        self.Info_Cabecario_Vendas()
        self.Info_Colunas_Vendas()
        self.controle.Atualiza_TreeView(verificar=True)
        self.controle.vizualizador_widget()

    def Atualiza_db(self, value, verificar):
        dados_v, dados = self.controle.Processamento_dados_venda_2(verificar)
        if dados_v == True:
            if value == 'add':
                self.banco.Adicionar_db_vendas(dados)
                self.controle.Atualiza_TreeView(verificar=True)
                self.controle.Limpar_entrys()
            elif value == 'alt':
                self.banco.Alterar_db_vendas(dados)
                self.controle.Atualiza_TreeView(verificar=True)
                self.controle.Limpar_entrys()
            elif value == 'del':
                self.banco.Apagar_db_vendas(dados)
                self.controle.Atualiza_TreeView(verificar=True)
                self.controle.Limpar_entrys()
        else:
            self.Func_Erro_Dados(self.root)