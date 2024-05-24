import tkinter as tk
from tkinter import ttk
from View import Create_visual
from Control import Control_Principal


class Infos_Login():
    def __init__(self, root):
        self.root = root
        self.create = Create_visual.Create(self.root)

    def Tela_Login(self):
        self.caixa0 = self.create.Func_Criar_Caixas(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.3, root=self.root)
        
    def Info_Labls_Login(self):
        # Informações para criar as Labls da Tela de Login.
        botoes_info = [
            (self.caixa0, "Usuário", 0.45, 0.13),
            (self.caixa0, "Senha", 0.45, 0.48)]
        for info in botoes_info:
            self.create.Func_Criar_Lb(*info)

    def Info_Entrys_Login(self):
        # Informações para criar as Entrys da Tela de Login.
        entradas_info = [
            (0.2, 0.25, 0.6, 0.15),
            (0.2, 0.6, 0.6, 0.15, "*")]
        self.quant_entrys_Login = []
        for info in entradas_info:
            entry = self.create.Func_Criar_Entry(self.caixa0, *info)
            self.quant_entrys_Login.append(entry)

    def Info_Btoes_Login(self):
        # Informações para criar os Botões da Tela de Login.
        info = [
            (self.caixa0, "Validar", 0.3, 0.8, 0.4, 0.1, lambda: self.controle.Func_Validar_user())]
        self.create.Func_Criar_Bt(*info[0])

    def Organiza_Funcs_Login(self):
        self.Tela_Login()
        self.Info_Entrys_Login()
        self.controle = Control_Principal.Principal(self.root, entrys=self.quant_entrys_Login)
        self.Info_Btoes_Login()
        self.Info_Labls_Login()
