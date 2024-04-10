import tkinter as tk
from View import Create_visual,View_Login,View_Vendas,View_Cadastro
from Model import Model_init

root = tk.Tk()

class Main():
    def __init__(self):
        self.root = root
        self.create = Create_visual.Create(self.root)
        self.login = View_Login.Infos_Login(self.root)
        self.vendas = View_Vendas.Infos_Vendas(self.root)
        self.cadastro = View_Cadastro.Infos_Cadastro(self.root)
        self.banco = Model_init.Main_db()
        self.banco.Conecta_db()
        self.Organiza_Funcs()
        self.root.mainloop()
        self.banco.Desconecta_db()

    def Organiza_Funcs(self):
        self.create.Janela(self.root)
        self.login.Organiza_Funcs_Login()

if __name__ == "__main__":
    Main()
    