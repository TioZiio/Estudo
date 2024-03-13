import tkinter as tk
import View_IV
import View_C
import Model

class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.create = View_IV.Create(self.root)
        self.organiza_IV = View_IV.Organiza_Funcs_IV(self.root)
        self.banco = Model.Main_db(self.root)
        self.cadastro = View_C.Tela_Cadastro(self.root)
        self.Organiza_all_funcs()
        self.root.mainloop()

    def Organiza_all_funcs(self):
        self.create.Janela(self.root)
        self.organiza_IV.Organiza_Funcs_Inicial()

if __name__ == "__main__":
    Main()