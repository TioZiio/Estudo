import tkinter as tk
from tkinter import ttk
from View import Create_visual,View_Cadastro
from Control import Control_Principal

class Infos_Vendas():
    def __init__(self, root):
        self.root_vendas = root
        self.create = Create_visual.Create(self.root_vendas)
        self.cadastro = View_Cadastro.Infos_Cadastro(self.root_vendas)

    def Tela_Vendas(self):
        # Conteiner 1
        self.caixa1 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.65, relheight=0.3, root=self.root_vendas
        )
        # Conteiner 2
        self.caixa2 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6, root=self.root_vendas
        )
        # Conteiner 3
        self.caixa3 = self.create.Func_Criar_Caixas(
            relx=0.7, rely=0.02, relwidth=0.28, relheight=0.3, root=self.root_vendas
        )

    def Info_Labls_Vendas(self):
        # Informações para criar as Labels da Tela de Vendas.
        # Variavel rotulos_info recebe respectivamente (caixa, nome, relx, rely)
        fonte = ('Arial', 14)
        rotulos_info = [
            (self.caixa1, "", 0.9, 0.2),
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
                rotulo = self.create.Func_Criar_Lb(*info, font=fonte)
            else:
                rotulo = self.create.Func_Criar_Lb(*info)
            
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
            entry = self.create.Func_Criar_Entry(self.caixa1, *info)
            self.quant_entrys.append(entry)

    def Info_Btoes_Vendas(self):
        botoes_info = [
            (self.caixa1, "Limpar Tela", 0.51, 0.05, 0.13, 0.15, 
                lambda: self.controle.Limpar_entrys()),
            (self.caixa1, "Adicionar", 0.64, 0.05, 0.13, 0.15, 
                lambda: self.controle.Atualiza_db_vendas(typFunc='add')),
            (self.caixa1, "Alterar", 0.77, 0.05, 0.1, 0.15, 
                lambda: self.controle.Atualiza_db_vendas(typFunc='alt')),
            (self.caixa1, "Apagar", 0.87, 0.05, 0.1, 0.15, 
                lambda: self.controle.Atualiza_db_vendas(typFunc='del')),
            (self.caixa1, "Clientes Help", 0.7, 0.68, 0.25, 0.15, 
                lambda: self.cadastro.Organiza_Funcs_Cadastro()),
            (self.caixa1, 'JAN', 0.05, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='JAN'))),
            (self.caixa1, 'VEF', 0.12, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='VEF'))),
            (self.caixa1, 'MAR', 0.19, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='MAR'))),
            (self.caixa1, 'ABR', 0.26, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='ABR'))),
            (self.caixa1, 'MAI', 0.33, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='MAI'))),
            (self.caixa1, 'JUN', 0.40, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='JUN'))),
            (self.caixa1, 'JUL', 0.47, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='JUL'))),
            (self.caixa1, 'AGO', 0.54, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='AGO'))),
            (self.caixa1, 'SET', 0.61, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='SET'))),
            (self.caixa1, 'OUT', 0.68, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='OUT'))),
            (self.caixa1, 'NOV', 0.75, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='NOV'))),
            (self.caixa1, 'DEZ', 0.82, 0.9, 0.07, 0.12,
                lambda: self.controle.Atualiza_TreeView(frame='!frame3.!treeview', 
                typTela='vendas', mes=self.create.Data_mes(mes='DEZ')))
        ]
        for info in botoes_info:
            botao = self.create.Func_Criar_Bt(*info)

    def Info_Cabecario_Vendas(self):
        info_cabecario = [
            ("#1", "Cod VENDA"), ("#2", "Cod PROD"), ("#3", "PRODUTO"), ("#4", "VALOR"),
            ("#5", "Cod CLNT"), ("#6", "NOME"), ("#7", "DATA")
        ]
        for info in info_cabecario:
            self.create.Func_Criar_Cabecario_lista(*info, frame='!frame3.!treeview')

    def Info_Colunas_Vendas(self):
        info_colunas = [
            ("#0", 1),("#1", 30),("#2", 100),("#3", 160),
            ("#4", 100),("#5", 95), ("#6", 210), ("#7", 160)
        ]
        for info in info_colunas:
            self.create.Func_Criar_Colunas_Lista(*info, frame='!frame3.!treeview')

    def Info_Cod_Produto(self, codigo=0):
        produtos = ["Erro", "Mini 25gr", "Cone 45gr", "Pacote 100gr", "Pacote 250gr", "Piposqueira", "Kit Degustação"]
        nome_produto = produtos[int(codigo)]
        return nome_produto

    def Organiza_Funcs_Vendas(self):
        self.Tela_Vendas()
        self.Info_Labls_Vendas()
        self.Info_Entrys_Vendas()
        self.controle = Control_Principal.Principal(self.root_vendas, entrys=self.quant_entrys)
        self.Info_Btoes_Vendas()
        self.controle.Func_Criar_Treeview(typTela='vendas')
        self.Info_Cabecario_Vendas()
        self.Info_Colunas_Vendas()
        self.controle.Atualiza_TreeView(typTela='vendas', frame='!frame3.!treeview', mes=['JAN'])
        