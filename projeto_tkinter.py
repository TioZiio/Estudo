import sqlite3
import tkinter as tk
from tkinter import ttk

class Funcoes():
    def JanelaInicial(self, root):
        # Cria a Tela inicial de Login. 
        # Variaveis contidas: Balões e Entrys (Tudo Visual).
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

        # Validacao
        self.bt_validacao = tk.Button(self.caixa0, text="Validar", command=self.Validacao)
        self.bt_validacao.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

    def User_Passwd(self, event=None):
        # Funçao para puxar dados de usuario e senha para o Login.
        self.v_user = self.et_user.get().lower()
        self.v_passwd = self.et_passwd.get().lower()
        if not self.v_user or not self.v_passwd:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0)

    def JanelaCadastro(self, root):
        # Cria a Tela do Cliente. Configurações como Cadastras, Alterar e Apagar clientes do Banco de Dados.
        # Variaveis aqui contidas: Botões, Entrys e Balões (Visual e funcional).
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
        self.bt_adicionar = tk.Button(self.caixa1, text="Adicionar", command=self.Add_clients)
        self.bt_adicionar.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = tk.Button(self.caixa1, text="Alterar", command=self.Alt_clients)
        self.bt_alterar.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = tk.Button(self.caixa1, text="Apagar", command=self.Del_clients)
        self.bt_apagar.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.15)

        # Balões
        self.lb_codigo = tk.Label(self.caixa1, text="Código", bg="#B0C4DE")
        self.lb_codigo.place(relx=0.02, rely=0.15)
        self.lb_nome = tk.Label(self.caixa1, text="Nome", bg="#B0C4DE")
        self.lb_nome.place(relx=0.12, rely=0.15)
        self.lb_telefone = tk.Label(self.caixa1, text="Telefone", bg="#B0C4DE")
        self.lb_telefone.place(relx=0.35, rely=0.15)
        self.lb_endereco = tk.Label(self.caixa1, text="Endereço", bg="#B0C4DE")
        self.lb_endereco.place(relx=0.02, rely=0.45)

        # Entrys
        self.et_codigo = tk.Entry(self.caixa1)
        self.et_codigo.place(relx=0.02, rely=0.25, relwidth=0.05, relheight=0.15)
        self.et_nome = tk.Entry(self.caixa1)
        self.et_nome.place(relx=0.12, rely=0.25, relwidth=0.2, relheight=0.15)
        self.et_telefone = tk.Entry(self.caixa1)
        self.et_telefone.place(relx=0.35, rely=0.25, relwidth=0.2, relheight=0.15)
        self.et_endereco = tk.Entry(self.caixa1)
        self.et_endereco.place(relx=0.02, rely=0.55, relwidth=0.52, relheight=0.15)

    def Limpar_entrys(self):
        # Limpa as Entrys da Tela Cadastro.
        self.et_codigo.delete(0, tk.END)
        self.et_nome.delete(0 , tk.END)
        self.et_telefone.delete(0 , tk.END)
        self.et_endereco.delete(0 , tk.END)

    def Variaveis(self):
        # Variaveis das Entrys da Tela Cadastro.
        self.dd_codigo = self.et_codigo.get()
        self.dd_nome = self.et_nome.get().capitalize()
        self.dd_telefone = self.et_telefone.get()
        self.dd_endereco = self.et_endereco.get().upper()

    def Lista(self):
        # Funçao responsavel pela criação da lista e scroll.
        # Variaveis principal: lista.clients
        self.lista_clients = ttk.Treeview(self.caixa2, height=3, column=("","Código", "Nome", "Telefone", "Endereço"))
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
        self.scroolLista = tk.Scrollbar(self.caixa2, orient="vertical")
        self.lista_clients.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.01, relwidth=0.016, relheight=0.96)
        self.lista_clients.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.96)
        self.lista_clients.bind("<Double-1>", self.DoubleClick)

    def select_lista(self):
        # Função que atualiza e mostra os dados dentro da Lista.
        self.lista_clients.delete(*self.lista_clients.get_children())
        self.Conecta_bd()
        variavel_local = self.cursor.execute("""SELECT * FROM dd_clientes ORDER BY cliente ASC;""")
        
        for row in variavel_local:
            self.lista_clients.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))
        self.Desconecta_bd()

    def DoubleClick(self, event=None):
        # Funçao evento de double click na lista, puxa dados para Entry.
        # Cria a Variavel self.dd_codigo
        self.Limpar_entrys()
        self.lista_clients.selection()

        for n in self.lista_clients.selection():
            col1, col2, col3, col4 = self.lista_clients.item(n, "values")
            self.et_codigo.insert(tk.END, col1)
            self.et_nome.insert(tk.END, col2)
            self.et_telefone.insert(tk.END, col3)
            self.et_endereco.insert(tk.END, col4)

    def Add_clients(self):
        # Funçao de Adicionar clientes, adicionando diretamente no Banco de Dados.
        # Sempre que adicionar de primeira sem erro, Gera um erro na variavel self.error
        self.Variaveis()
        if not self.dd_nome.strip() or not self.dd_telefone.strip() or not self.dd_endereco.strip():
            self.Erro_Dados()
        else:
            try:
                self.error.config(text='')
            except Exception as error:
                print(f"Erro encontrado: {error}")
            finally:
                self.Conecta_bd()
                self.cursor.execute(""" INSERT INTO dd_clientes (cliente, telefone, endereco)
                    VALUES (?, ?, ?)""", (self.dd_nome, self.dd_telefone, self.dd_endereco))
                self.conn.commit()
                self.Desconecta_bd()
                self.Limpar_entrys()
                self.select_lista()

    def Del_clients(self):
        # Função de Delete de clintes do Banco de Dados.
        # Transformar variavel self.dd_codigo em lista para conseguir passar mais digitos: 1 ou 11 ou 111.
        self.Variaveis()
        if not self.dd_codigo:
            self.Erro_Dados()
        else:
            self.dd_codigo = [self.dd_codigo]
            self.Conecta_bd()
            self.cursor.execute("""DELETE FROM dd_clientes WHERE codigo = ?""", (self.dd_codigo))
            self.conn.commit()
            self.Desconecta_bd()
            self.Limpar_entrys()
            self.select_lista()

    def Alt_clients(self):
        # Função de Atualizar dados dos clintes no Banco de Dados.
        self.Variaveis()
        if not self.dd_codigo:
            self.Erro_Dados()
        else:
            self.Conecta_bd()
            self.cursor.execute(
                """UPDATE dd_clientes
                SET codigo = ?, cliente = ?, telefone = ?, endereco = ?
                WHERE codigo = ?
                """, (self.dd_codigo, self.dd_nome, self.dd_telefone, self.dd_endereco, self.dd_codigo))
            self.conn.commit()
            self.Desconecta_bd()
            self.Limpar_entrys()
            self.select_lista()
    
    def Erro_Dados(self):
        self.error = tk.Label(self.caixa1, text="Dados não inseridos.", fg="red", bg="#B0C4DE")
        self.error.place(relx= 0.3, rely=0.8, relwidth=0.2, relheight=0.1)

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

class ToolBar():
    def Menu(self, root):
        self.root = root
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        menutool = tk.Menu(menubar)
        menutool_2 = tk.Menu(menubar)

        menubar.add_cascade(label="Clientes", menu=menutool)
        menubar.add_cascade(label="Opçoes", menu=menutool_2)

        menutool.add_command(label="Adicionar", command=self.Add_clients)
        menutool.add_command(label="Alterar", command=self.Alt_clients)
        menutool.add_command(label="Apagar", command=self.Del_clients)
        menutool_2.add_command(label="Quit", command=self.root.quit)

class Main(Funcoes,Banco_de_dados,ToolBar):
    def __init__(self, master=None):
        self.root = tk.Tk()
        self.Janela_principal()
        self.JanelaInicial(self.root)
        self.MontaTabelas()
        self.root.mainloop()

    def Janela_principal(self):
        self.root.title("Menu")
        self.root.configure(background="#2F4F4F")
        self.root.geometry("1200x650")
        self.root.resizable(False, False)

    def Validacao(self):
        self.User_Passwd()
        if self.v_user == 'david' and self.v_passwd == '123':
            self.TelaCadastro()
            self.Menu(self.root)
            self.caixa0.destroy()
        else:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0)

    def TelaCadastro(self, root=None):
        if root is None:
            root = self.root
        self.Menu(root)
        self.JanelaCadastro(root)
        self.Lista()
        self.select_lista()

if __name__ == "__main__":
    Main()
