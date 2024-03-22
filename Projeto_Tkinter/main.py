import tkinter as tk
from View import Create_visual
from View import View_Login
from View import View_Vendas
from View import View_Cadastro
import Model

root = tk.Tk()

class Main():
    def __init__(self):
        self.root = root
        self.create = Create_visual.Create(self.root)
        self.login = View_Login.Infos_Login(self.root)
        self.vendas = View_Vendas.Infos_Vendas(self.root)
        self.cadastro = View_Cadastro.Infos_Cadastro(self.root)
        self.banco = Model.Main_db(self.root)
        self.Organiza_funcs()
        self.root.mainloop()
        self.banco.Desconecta_db()

    def Organiza_funcs(self):
        self.create.Janela(self.root)
        self.login.Organiza_Funcs_Login()

if __name__ == "__main__":
    Main()