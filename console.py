import sqlite3
import tkinter as tk
from tkinter import ttk

class Telas():
    def TelaInicial(self, root):
        self.root = root
        # Conteiner Inicial
        self.caixa0 = tk.Frame(self.root, bd=4, bg="#B0C4DE", 
                               highlightbackground="#191970", highlightthickness=2)
        self.caixa0.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.3)

        # Balões
        self.lb_user = tk.Label(self.caixa0, text="Usuario", bg="#B0C4DE")
        self.lb_user.place(relx=0.45, rely=0.15)
        self.lb_passwd = tk.Label(self.caixa0, text="Senha", bg="#B0C4DE")
        self.lb_passwd.place(relx=0.45, rely=0.5)

        # Entrys Login
        self.et_user = tk.Entry(self.caixa0)
        self.et_user.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.15)
        self.et_passwd = tk.Entry(self.caixa0, show='*')
        self.et_passwd.place(relx=0.2, rely=0.60, relwidth=0.6, relheight=0.15)

        # Validation
        self.bt_validacao = tk.Button(self.caixa0, text="Validar", command=self.Validation)
        self.bt_validacao.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

    def Get_user(self, event=None):
        # Retorna tuplas!!
        self.v_user = self.et_user.get().lower()
        self.v_passwd = self.et_passwd.get().lower()
        if not self.v_user or not self.v_passwd:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0)
            return


    def Cadastro(self, root):
        self.root = root
        # Conteiner 1
        self.caixa1 = tk.Frame(self.root, bd=4, bg="#B0C4DE", 
                               highlightbackground="#191970", highlightthickness=2)
        self.caixa1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3)
        # Conteiner 2
        self.caixa2 = tk.Frame(self.root, bd=4, bg="#B0C4DE", 
                               highlightbackground="#191970", highlightthickness=2)
        self.caixa2.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6)

        # Botões
        self.bt_cadastro = tk.Button(self.caixa1, text="Cadastro")
        self.bt_cadastro.place(relx=0, rely=0, relwidth=0.12, relheight=0.1)
        self.bt_quit = tk.Button(self.caixa1, text="Quit", command=self.root.quit)
        self.bt_quit.place(relx=0.92, rely=0, relwidth=0.08, relheight=0.1)
        self.bt_adicionar = tk.Button(self.caixa1, text="Adicionar", command=self.Add_clients)
        self.bt_adicionar.place(relx=0.62, rely=0.15, relwidth=0.1, relheight=0.12)

        # Balões
        self.lb_nome = tk.Label(self.caixa1, text="Nome", bg="#B0C4DE")
        self.lb_nome.place(relx=0.02, rely=0.15)
        self.lb_telefone = tk.Label(self.caixa1, text="Telefone", bg="#B0C4DE")
        self.lb_telefone.place(relx=0.35, rely=0.15)
        self.lb_endereco = tk.Label(self.caixa1, text="Endereço", bg="#B0C4DE")
        self.lb_endereco.place(relx=0.02, rely=0.45)

        # Entrys
        self.et_nome = tk.Entry(self.caixa1)
        self.et_nome.place(relx=0.02, rely=0.25, relwidth=0.3, relheight=0.15)
        self.et_telefone = tk.Entry(self.caixa1)
        self.et_telefone.place(relx=0.35, rely=0.25, relwidth=0.25, relheight=0.15)
        self.et_endereco = tk.Entry(self.caixa1)
        self.et_endereco.place(relx=0.02, rely=0.55, relwidth=0.52, relheight=0.15)

    def Lista(self):
        self.lista_clients = ttk.Treeview(self.caixa2, height=3, column=("","Nome", "Telefone", "Endereço"))
        # Cabeçario lista cadastro
        self.lista_clients.heading("#0", text="")
        self.lista_clients.heading("#1", text="Cod", anchor=tk.CENTER)
        self.lista_clients.heading("#2", text="NOME", anchor=tk.CENTER)
        self.lista_clients.heading("#3", text="TELEFONE", anchor=tk.CENTER)
        self.lista_clients.heading("#4", text="ENDEREÇO", anchor=tk.CENTER)
        # Coluna Lista cadastro
        self.lista_clients.column("#0", width=1, anchor=tk.CENTER)
        self.lista_clients.column("#1", width=50, anchor=tk.CENTER)
        self.lista_clients.column("#2", width=200, anchor=tk.CENTER)
        self.lista_clients.column("#3", width=250, anchor=tk.CENTER)
        self.lista_clients.column("#4", width=600, anchor=tk.CENTER)
        # Scrool Lista cadastro
        self.scroolLista = tk.Scrollbar(self.caixa2, orient='vertical')
        self.lista_clients.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.01, relwidth=0.016, relheight=0.96)
        self.lista_clients.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.96)

    def select_lista(self):
        self.lista_clients.delete(*self.lista_clients.get_children())
        self.Conecta_bd()
        variavel = self.cursor.execute("""SELECT * FROM dd_clientes ORDER BY cliente ASC;""")
        
        for row in variavel:
            self.lista_clients.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))

        self.Desconecta_bd()

    def Limpar_entrys(self):
        self.et_nome.delete(0 , tk.END)
        self.et_telefone.delete(0 , tk.END)
        self.et_endereco.delete(0 , tk.END)

class Banco_de_dados():
    def Conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()
        print("Conexão feita.")

    def Desconecta_bd(self):
        self.conn.close()
        print("Desconexão feita")

    def MontaTabelas(self):
        self.Conecta_bd()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS dd_clientes(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente CHAR(50) NOT NULL,
                telefone INTEGER,
                endereco CHAR(50)
            );""")
        self.conn.commit()
        self.Desconecta_bd()
    
    def Add_clients(self):
        self.error = tk.Label(self.caixa1, text="Dados não inseridos.", fg="red", bg="#B0C4DE")
        self.dd_nome = self.et_nome.get().capitalize()
        self.dd_telefone = self.et_telefone.get()
        self.dd_endereco = self.et_endereco.get().upper()
        if not self.dd_nome or not self.dd_telefone or not self.et_endereco:
            self.error.place(relx= 0.3, rely=0.8, relwidth=0.2, relheight=0.1)
        else:
            self.error.config(text='')
            self.Conecta_bd()
            self.cursor.execute(""" INSERT INTO dd_clientes (cliente, telefone, endereco)
                VALUES (?, ?, ?)""", (self.dd_nome, self.dd_telefone, self.dd_endereco))
            self.conn.commit()
            self.Desconecta_bd()
            self.Limpar_entrys()
            self.select_lista()
        

class Aplicativo(Telas,Banco_de_dados):
    def __init__(self, master=None):
        self.root = tk.Tk()
        self.Janela_principal()
        self.TelaInicial(self.root)
        self.MontaTabelas()
        self.root.mainloop()

    def Janela_principal(self):
        self.root.title("Menu")
        self.root.configure(background="#2F4F4F")
        self.root.geometry("1200x650")
        self.root.resizable(False, False)

    def Validation(self):
        self.Get_user()
        if self.v_user == 'david' and self.v_passwd == '123':
            self.Cadastro(self.root)
            self.Lista()
            self.select_lista()
            self.caixa0.destroy()
        else:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0) 

if __name__ == "__main__":
    Aplicativo()
