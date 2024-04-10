import tkinter as tk
from tkinter import ttk
from View import Create_visual
from Control import Control_Principal

class Infos_Cadastro():
    def __init__(self, root):
        self.root = root
        self.create = Create_visual.Create(self.root)

    def Janela_Cadastro(self):
        self.root_cadastro = tk.Toplevel(self.root)
        self.root_cadastro.title("Cadastro Clientes")
        self.root_cadastro.configure(background="#2F4F4F")
        self.root_cadastro.geometry("1000x500")
        self.root_cadastro.resizable(True, True)
    
    def Tela_Cadastro(self, root):
        # Conteiner 1
        self.caixa1 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3, root=root
        )
        # Conteiner 2
        self.caixa2 = self.create.Func_Criar_Caixas(
            relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6, root=root
        ) 

    def Info_Btoes_Cadastro(self):
        botoes_info = [
            (self.caixa1, "Buscar", 0.15, 0.05, 0.1, 0.15,
                lambda: self.controle.buscar_cadastro()),
            (self.caixa1, "Limpar Tela", 0.25, 0.05, 0.1, 0.15, 
                lambda: self.controle.Limpar_entrys()),
            (self.caixa1, "Adicionar", 0.45, 0.05, 0.1, 0.15, 
                lambda: self.controle.Atualiza_db_cadastro(typFunc='add')),
            (self.caixa1, "Alterar", 0.55, 0.05, 0.1, 0.15,
                lambda: self.controle.Atualiza_db_cadastro(typFunc='alt')),
            (self.caixa1, "Apagar", 0.65, 0.05, 0.1, 0.15, 
                lambda: self.controle.Atualiza_db_cadastro(typFunc='del'))
        ]
        for info in botoes_info:
            self.create.Func_Criar_Bt(*info)
    
    def Info_Labls_Cadastro(self):
        rotulos_info = [
            (self.caixa1, "Cod. Cliente", 0.02, 0.02),
            (self.caixa1, "Nome", 0.02, 0.3),
            (self.caixa1, "Telefone", 0.2, 0.3),
            (self.caixa1, "Endereço", 0.43, 0.3),
            (self.caixa1, "Cidade", 0.65, 0.3)
        ]
        for info in rotulos_info:
            self.create.Func_Criar_Lb(*info)

    def Info_Entrys_Cadastro(self):
        entradas_info = [
            (0.02, 0.15, 0.05, 0.15),
            (0.02, 0.5, 0.15, 0.15),
            (0.2, 0.5, 0.2, 0.15),
            (0.43, 0.5, 0.2, 0.15),
            (0.65, 0.5, 0.2, 0.15)
        ]
        self.quant_entrys = []
        for info in entradas_info:
            entry = self.create.Func_Criar_Entry(self.caixa1, *info)
            self.quant_entrys.append(entry)

    def verificador_treeview(self, typFrame):
        valores = ['','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
        for n in valores:
            try:
                frame = f'.!toplevel{n}.!frame2'
                frame_lista = self.root.nametowidget(frame)
                if frame_lista:
                    break
            except Exception as er:
                print(f'Log Verificador: {n}')
                pass
        if typFrame == 'frame':
            return frame_lista
        elif typFrame == 'treeview':
            return frame

    def recebe_treeview(self):
        frame_local = self.verificador_treeview(typFrame='treeview')
        frame_local = frame_local + '.!treeview'
        frame_real = self.root.nametowidget(frame_local)
        return frame_real

    def Info_Cabecario_Cadastro(self):
        info_cabecario = [
            ("#1", "Cod"), ("#2", "NOME"), ("#3", "TELEFONE"), ("#4", "ENDEREÇO"), ("#5", "CIDADE")
        ]
        frame = self.recebe_treeview()
        for info in info_cabecario:
            self.create.Func_Criar_Cabecario_lista(*info, frame=frame)

    def Info_Colunas_Cadastro(self):
        info_colunas =[
            ("#0", 1),("#1", 20),("#2", 180),
            ("#3", 180),("#4", 280),("#5", 150)
        ]
        frame = self.recebe_treeview()
        for info in info_colunas:
            self.create.Func_Criar_Colunas_Lista(*info, frame=frame)

    def Organiza_Funcs_Cadastro(self):
        self.Janela_Cadastro()
        self.Tela_Cadastro(self.root_cadastro)
        self.Info_Labls_Cadastro()
        self.Info_Entrys_Cadastro()
        self.controle = Control_Principal.Principal(self.root_cadastro, entrys=self.quant_entrys)
        self.Info_Btoes_Cadastro()
        self.controle.Func_Criar_Treeview()
        self.Info_Cabecario_Cadastro()
        self.Info_Colunas_Cadastro()
        frame = self.recebe_treeview()
        self.controle.Atualiza_TreeView(frame=frame, typTela='cadastro')
        