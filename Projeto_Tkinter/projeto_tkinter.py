import sqlite3
import tkinter as tk
from tkinter import ttk

class Funcs_Globais():
    # Funções muito reutilizadas, tornan-se globais.
    def Func_Criar_Caixas(self, root, relx, rely, relwidth, relheight):
        # Função que cria os Conteiners para armazenar os Botões, Labels e Entrys.
        caixa = tk.Frame(root, bd=4, bg="#B0C4DE", 
                         highlightbackground="#191970", highlightthickness=2)
        caixa.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return caixa

    def Func_Criar_Bt(self, caixa, texto, relx, rely, relwidth, relheight, command=None):
        # Função para criação de Botões em Conteiners.
        botao = tk.Button(caixa, text=texto, command=command)
        botao.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

    def Func_Criar_Lb(self, caixa, texto, relx, rely, relwidth=None, relheight=None):
        # Função para criação de Labels em Conteiners.
        label = tk.Label(caixa, text=texto, bg="#B0C4DE")
        label.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

    def Func_Criar_Entry(self, caixa, relx, rely, relwidth, relheight, options=None):
        # Função para criação de Entrys em Conteiners.
        entry = tk.Entry(caixa, show=options)
        entry.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        return entry

    def Func_Criar_Treeview(self, verificar=True):
        # Funçao responsavel pela criação da lista e scroll.
        if verificar == True:
            self.Lista_Treeview = ttk.Treeview(
                self.caixa2, height=3, column=(
                    "Cod PROD", "PRODUTO", "Qt PROD", "VALOR", "Cod CLIENTE", "NOME", "DATA"
                )
            )
        else:
            self.Lista_Treeview = ttk.Treeview(
                self.caixa2, height=3, column=("Cod CLIENTE", "NOME", "TELEFONE", "EENDEREÇO", "CIDADE")
            )
        self.scroolLista = tk.Scrollbar(self.caixa2, orient="vertical")
        self.scroolLista.place(relx=0.97, rely=0.01, relwidth=0.016, relheight=0.96)
        self.Lista_Treeview.configure(yscroll=self.scroolLista.set)
        self.Lista_Treeview.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.96)
        self.Lista_Treeview.bind("<Double-1>", self.Func_Double_Click)

    def Func_Criar_Cabecario_lista(self, valor, rotulo):
        self.Lista_Treeview.heading(valor, text=rotulo, anchor=tk.CENTER)

    def Func_Criar_Colunas_Lista(self, valor, tamanho):
        self.Lista_Treeview.column(valor, width=tamanho, anchor=tk.CENTER)

    def Func_Double_Click(self, event=None):
        # Funçao evento de double click na lista, puxa dados para Entry.
        try:
            selection = self.Lista_Treeview.selection()
            item = self.Lista_Treeview.item(selection[0], "values")
        except Exception as error:
            print(f"Houve o ERRO: {error}\nLinha 74")
        finally:
            if len(item) == 5:
                for entry, value in zip(self.Entrada_dados, item):
                    entry.insert(tk.END, value)
            elif len(item) == 7:
                lista = []
                for info in item:
                    lista.append(info)
                lista.pop(2); lista.pop(); lista.pop()
                for entry, value in zip(self.Entrada_dados, lista):
                    entry.insert(tk.END, value)       

    def Func_Select_Lista(self, verificar=True):
        # Função que atualiza e mostra os dados dentro da Lista.
        self.Conecta_bd()
        if verificar:
            self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
            variavel_local = self.cursor.execute(
                """SELECT cod_venda, cod_produto, nome_produto, valor_venda, cod_cliente, nome_cliente, data 
                FROM vendas ORDER BY cod_venda DESC;"""
            )
            for row in variavel_local:
                self.Lista_Treeview.insert(
                    "", tk.END, values=(row[0],f"{row[1]:0>3}",row[2],f"{row[3]:.2f}",row[4], row[5],row[6])
                )
        else:
            self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
            variavel_local = self.cursor.execute("""SELECT * FROM clients ORDER BY nome ASC;""")
            for row in variavel_local:
                self.Lista_Treeview.insert(
                    "", tk.END, values=(row[0], row[1], row[2], row[3], row[4])
                )
        self.Desconecta_bd()

    def Func_Limpar_entrys(self):
        # Limpa as Entrys da Tela Cadastro.
        for entry in self.Entrada_dados:
            entry.delete(0, tk.END)

    def Func_Erro_Dados(self, frase="Dados não inseridos."):
        self.error = tk.Label(self.caixa1, text=frase, fg="red", bg="#B0C4DE")
        self.error.place(relx=0.3, rely=0.8)

    def Organiza_bd_Add_Del_Alt(self, query, parametros, verificar=True):
        if parametros[0] == '':
                self.Func_Erro_Dados()
        else:
            try:
                self.Conecta_bd()
                self.cursor.execute(query, parametros)
                self.conn.commit()
            except Exception as error:
                print(f"Erro encontrado: {error}\nLinha 127")
            finally:
                self.Desconecta_bd()
                self.Func_Limpar_entrys()
                self.Func_Select_Lista(verificar)

    def Janela_fechada(self):
        self.iniciar.destroy()
        self.Organiza_Funcs_Vendas()

class JanelaUser():
    # Tela de Login.
    def Tela_Inicial(self, root):
        # Cria a Tela inicial de Login. 
        # Conteiner Inicial
        self.caixa0 = self.Func_Criar_Caixas(root, relx=0.3, rely=0.3, relwidth=0.4, relheight=0.3)

    def Info_Labls_Inicial(self):
        # Informações para criar as Labls da Tela de Login.
        botoes_info = [
            (self.caixa0, "Usuário", 0.45, 0.15),
            (self.caixa0, "Senha", 0.45, 0.5)]
        for info in botoes_info:
            self.Func_Criar_Lb(*info)

    def Info_Entrys_Inicial(self):
        # Informações para criar as Entrys da Tela de Login.
        entradas_info = [
            (0.2, 0.25, 0.6, 0.15),
            (0.2, 0.6, 0.6, 0.15, "*")]
        self.entradas_inicial = []
        for info in entradas_info:
            entry = self.Func_Criar_Entry(self.caixa0, *info)
            self.entradas_inicial.append(entry)

    def Info_Btoes_Inicial(self):
        # Informações para criar os Botões da Tela de Login.
        botoes_info = [
            (self.caixa0, "Validar", 0.3, 0.8, 0.4, 0.1, self.Validacao)]
        for info in botoes_info:
            self.Func_Criar_Bt(*info)

    def User_Passwd(self, event=None):
        # Funçao para puxar os dados de usuario e senha das Entrys para o login.
        self.v_user = self.entradas_inicial[0].get().lower()
        self.v_passwd = self.entradas_inicial[1].get().lower()
        if not self.v_user or not self.v_passwd:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0)

    def Validacao(self):
        self.User_Passwd()
        self.v_user = 'david' ;self.v_passwd = '123'
        if self.v_user == 'david' and self.v_passwd == '123':
            self.Organiza_Funcs_Vendas()
            self.Menu(self.root)
            self.caixa0.destroy()
        else:
            self.error = tk.Label(self.caixa0, text="Usuario ou senha Incorretos", fg="red", bg="#B0C4DE")
            self.error.place(relx= 0.3, rely=0)

class JanelaVendas():
    # Tela de Registro de Vendas.
    def Tela_Vendas(self, root):
        # Conteiner 1
        self.caixa1 = self.Func_Criar_Caixas(root, relx=0.02, rely=0.02, relwidth=0.65, relheight=0.3)
        # Conteiner 2
        self.caixa2 = self.Func_Criar_Caixas(root, relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6)
        # Conteiner 3
        self.caixa3 = self.Func_Criar_Caixas(root, relx=0.7, rely=0.02, relwidth=0.28, relheight=0.3)

    def Info_Btoes_Vendas(self):
        # Informações para criar os Botões da Tela de Vendas.
        # Variavel botoes_info recebe respectivamente (caixa, nome, relx, rely, relwidth, relheight, comando)
        botoes_info = [
            (self.caixa1, "Limpar Tela", 0.51, 0.05, 0.13, 0.15, self.Func_Limpar_entrys),
            (self.caixa1, "Adicionar", 0.64, 0.05, 0.13, 0.15, self.Add_Vendas),
            (self.caixa1, "Alterar", 0.77, 0.05, 0.1, 0.15, self.Alt_Vendas),
            (self.caixa1, "Apagar", 0.87, 0.05, 0.1, 0.15, self.Del_Vendas)
        ]
        for info in botoes_info:
            botao = self.Func_Criar_Bt(*info)

    def Info_Labls_Vendas(self):
        # Informações para criar as Labels da Tela de Vendas.
        # Variavel rotulos_info recebe respectivamente (caixa, nome, relx, rely)
        rotulos_info = [
            (self.caixa1, "Cod. Venda", 0.02, 0.02),
            (self.caixa1, "Cod. Produto", 0.02, 0.3, 0.13),
            (self.caixa1, "Valor", 0.25, 0.3),
            (self.caixa1, "Cod. Cliente", 0.4, 0.3, 0.13)
        ]
        for info in rotulos_info:
            rotulo = self.Func_Criar_Lb(*info)
            
    def Info_Entrys_Vendas(self):
        # Informações para criar as Entrys da Tela de Vendas.
        # Variavel entradas_info recebe respectivamente (relx, rely, relwidth, relheight)
        self.Entrada_dados = []
        entradas_info = [
            (0.02, 0.15, 0.1, 0.15),
            (0.02, 0.45, 0.15, 0.15),
            (0.2, 0.45, 0.15, 0.15),
            (0.38, 0.45, 0.15, 0.15),
        ]
        for info in entradas_info:
            entry = self.Func_Criar_Entry(self.caixa1, *info)
            self.Entrada_dados.append(entry)

    def Variaveis_caixa3(self):
        # Cria e informa todos os codigos de cada produto.
        # Precisa ser atualizado, para reduzir codigo.
        mini = "Pacote Mini 25gr {:_>11}".format("001")
        cone = "Pacote Cone 45gr {:_>10}".format("002")
        pequeno = "Pacote Pequeno 100gr {:_>6}".format("003")
        grande = "Pacote Grande 250gr {:_>7}".format("004")
        piposqueira = "Piposqueira {:_>15}".format("005")
        kit_degustacao = "Kit. Degustação {:_>12}".format("006")
        # Balões
        self.lb_pacote_mini = tk.Label(self.caixa3, text=mini, bg="#B0C4DE", font=('Arial', 14))
        self.lb_pacote_cone = tk.Label(self.caixa3, text=cone, bg="#B0C4DE", font=('Arial', 14))
        self.lb_pacote_pequ = tk.Label(self.caixa3, text=pequeno, bg="#B0C4DE", font=('Arial', 14))
        self.lb_pacote_gran = tk.Label(self.caixa3, text=grande, bg="#B0C4DE", font=('Arial', 14))
        self.lb_piposqueira = tk.Label(self.caixa3, text=piposqueira, bg="#B0C4DE", font=('Arial', 14))
        self.lb_kit_degustacao = tk.Label(self.caixa3, text=kit_degustacao, bg="#B0C4DE", font=('Arial', 14))

        # Posicionando as labels
        self.lb_pacote_mini.place(relx=0, rely=0.05)
        self.lb_pacote_cone.place(relx=0, rely=0.2)
        self.lb_pacote_pequ.place(relx=0, rely=0.35)
        self.lb_pacote_gran.place(relx=0, rely=0.5)
        self.lb_piposqueira.place(relx=0, rely=0.65)
        self.lb_kit_degustacao.place(relx=0, rely=0.8)

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

    def Variaveis_Vendas_internas(self):
        # Variaveis das Entrys da Tela Cadastro.
        lista = ['0', '0', '0', '0']
        for n in range(len(lista)):
            lista[n] = self.Entrada_dados[n].get()
        if lista[1] == '' or lista[3] == '' or int(lista[1]) > 6:
            self.Func_Erro_Dados()
            lista = ['0', '0', '0', '0']
            return lista 
        else:
            return lista

    def Info_Cod_Prod_Vendas(self):
        produtos = ["Erro", "Mini 25gr", "Cone 45gr", "Pacote 100gr", "Pacote 250gr", "Piposqueira", "Kit Degustação"]
        nome_produto = produtos[int(self.Variaveis_Vendas_internas()[1])]
        return nome_produto

    def Variaveis_Vendas_externas(self, codigo=None):
        from datetime import datetime
        data = datetime.now().strftime('%d/%m')
        self.Conecta_bd()
        self.cursor.execute(f"""SELECT nome FROM clients WHERE codigo = {codigo};""")
        nome_cliente = self.cursor.fetchall()
        if not nome_cliente:
            self.Func_Erro_Dados("Código cliente ou produto não cadastrado")
            return [0]
        else:
            lista = [nome_cliente[0][0], data]
            return lista
        self.Desconecta_bd()

    def Organiza_Variaveis_Vendas(self):
        lista = []
        for info in self.Variaveis_Vendas_internas():
            if info == '':
                info = '0'
            lista.append(info)
        lista.insert(2, self.Info_Cod_Prod_Vendas())
        for info in self.Variaveis_Vendas_externas(codigo=lista[4]):
            if info == 0:
                lista.clear(); lista.append(info)
            else:
                lista.append(info)
        return lista

    def Add_Vendas(self):
        lista = self.Organiza_Variaveis_Vendas()
        if len(lista) == 1:
            self.Func_Limpar_entrys()
            self.Func_Select_Lista(verificar=True)
        else:
            query = """INSERT INTO vendas (
                cod_produto, nome_produto, valor_venda, cod_cliente, nome_cliente, data
            ) VALUES (?, ?, ?, ?, ?, ?)"""
            lista.pop(0)
            self.Organiza_bd_Add_Del_Alt(query, lista, verificar=True)

    def Del_Vendas(self):
        codigo_venda = self.Entrada_dados[0].get()
        if codigo_venda == '':
            self.Func_Erro_Dados()
            return
        query = """DELETE FROM vendas WHERE cod_venda = ?"""
        self.Organiza_bd_Add_Del_Alt(query, [codigo_venda])

    def Alt_Vendas(self):
        variavel_local = self.Variaveis_Vendas_internas()
        if not variavel_local[1].strip() and not variavel_local[3].strip():
            self.Func_Erro_Dados()
        else:
            query = """
                UPDATE vendas
                SET cod_produto = ?, nome_produto = ?, valor_venda = ?, 
                cod_cliente = ?, nome_cliente = ?, data = ?
                WHERE cod_venda = ?
            """
            lista = self.Organiza_Variaveis_Vendas()
            variavel_local_2 = lista[0]
            lista.pop(0); lista.append(variavel_local_2)
            self.Organiza_bd_Add_Del_Alt(query, lista, verificar=True)

class JanelaCadastro():
    # Tela de Cadastro de clientes.
    def Janela_Cadastro(self, root):
        # Janela Cadastro
        root.title("Cadastro Clientes")
        root.configure(background="#2F4F4F")
        root.geometry("1000x500")
        root.resizable(True, True)
        self.Tela_Cadastro(root)

    def Tela_Cadastro(self, root):
        # Conteiner 1
        self.caixa1 = self.Func_Criar_Caixas(root, relx=0.02, rely=0.02, relwidth=0.96, relheight=0.3)
        # Conteiner 2
        self.caixa2 = self.Func_Criar_Caixas(root, relx=0.02, rely=0.35, relwidth=0.96, relheight=0.6)

    def Info_Btoes_Cadastro(self):
        # Informações para criar os Botões da Tela de Cadastro.
        # Variavel botoes_info recebe respectivamente (caixa, nome, relx, rely, relwidth, relheight, comando)
        botoes_info = [
            (self.caixa1, "Buscar", 0.15, 0.05, 0.1, 0.15, self.Bus_clients),
            (self.caixa1, "Limpar Tela", 0.25, 0.05, 0.1, 0.15, self.Func_Limpar_entrys),
            (self.caixa1, "Adicionar", 0.45, 0.05, 0.1, 0.15, self.Add_Clients),
            (self.caixa1, "Alterar", 0.55, 0.05, 0.1, 0.15, self.Alt_Clients),
            (self.caixa1, "Apagar", 0.65, 0.05, 0.1, 0.15, self.Del_Clients)
        ]
        for info in botoes_info:
            self.Func_Criar_Bt(*info)
    
    def Info_Labls_Cadastro(self):
        # Informações para criar as Labels da Tela de Cadastro.
        # Variavel rotulos_info recebe respectivamente (caixa, nome, relx, rely)
        rotulos_info = [
            (self.caixa1, "Cod. Cliente", 0.02, 0.02),
            (self.caixa1, "Nome", 0.02, 0.3),
            (self.caixa1, "Telefone", 0.2, 0.3),
            (self.caixa1, "Endereço", 0.43, 0.3),
            (self.caixa1, "Cidade", 0.65, 0.3)
        ]
        for info in rotulos_info:
            self.Func_Criar_Lb(*info)

    def Info_Entrys_Cadastro(self):
        # Informações para criar as Labels da Tela de Cadastro.
        # Variavel entradas_info recebe respectivamente (relx, rely, relwidth, relheight)
        self.Entrada_dados = []
        entradas_info = [
            (0.02, 0.15, 0.05, 0.15),
            (0.02, 0.5, 0.15, 0.15),
            (0.2, 0.5, 0.2, 0.15),
            (0.43, 0.5, 0.2, 0.15),
            (0.65, 0.5, 0.2, 0.15)
        ]
        for info in entradas_info:
            entry = self.Func_Criar_Entry(self.caixa1, *info)
            self.Entrada_dados.append(entry)

    def Info_Cabecario_Cadastro(self):
        info_cabecario = [
            ("#1", "Cod"), ("#2", "NOME"), ("#3", "TELEFONE"), ("#4", "ENDEREÇO"), ("#5", "CIDADE")
        ]
        for info in info_cabecario:
            self.Func_Criar_Cabecario_lista(*info)

    def Info_Colunas_Cadastro(self):
        info_colunas =[
            ("#0", 1),("#1", 20),("#2", 180),
            ("#3", 180),("#4", 280),("#5", 150)
        ]
        for info in info_colunas:
            self.Func_Criar_Colunas_Lista(*info)

    def Variaveis_Cadastro(self):
        # Variaveis das Entrys da Tela Cadastro.
        self.dd_codigo = self.Entrada_dados[0].get()
        self.dd_nome = self.Entrada_dados[1].get().capitalize()
        self.dd_telefone = self.Entrada_dados[2].get()
        self.dd_endereco = self.Entrada_dados[3].get().upper()
        self.dd_cidade = self.Entrada_dados[4].get().upper()
        lista = [self.dd_codigo, self.dd_nome, self.dd_telefone, self.dd_endereco, self.dd_cidade]
        return lista

    def Bus_clients(self):
        self.Lista_Treeview.delete(*self.Lista_Treeview.get_children())
        lista = [(1, 'nome'), (3, 'endereco'), (4, 'cidade')]
        for value, variavel_local in lista:
            if self.Entrada_dados[value].get().strip() != '':
                v = f"{self.Entrada_dados[value].get().upper()}%"
                self.Conecta_bd()
                self.cursor.execute(f"SELECT * FROM clients WHERE {variavel_local} LIKE ? ORDER BY nome ASC", (v,))
                buscar_nome = self.cursor.fetchall()
                for row in buscar_nome:
                    self.Lista_Treeview.insert("", tk.END, values=row)
                self.Func_Limpar_entrys()
                self.Desconecta_bd()
                break
        else:
            self.Func_Limpar_entrys()
            self.Func_Select_Lista(verificar=False)

    def Add_Clients(self):
        if not self.Variaveis_Cadastro()[0].strip() and not self.Variaveis_Cadastro()[2].strip():
            self.Func_Erro_Dados()
        else:
            query = """INSERT INTO clients (nome, telefone, endereco, cidade) VALUES (?, ?, ?, ?)"""
            lista = []
            for n in self.Variaveis_Cadastro()[1:]:
                lista.append(n)
            self.Organiza_bd_Add_Del_Alt(query, lista, verificar=False)

    def Del_Clients(self):
        codigo_cliente = self.Entrada_dados[0].get()
        if codigo_cliente == '':
            self.Func_Erro_Dados()
            return
        query = """DELETE FROM clients WHERE codigo = ?"""
        self.Organiza_bd_Add_Del_Alt(query, [codigo_cliente], verificar=False)

    def Alt_Clients(self):
        if not self.Variaveis_Cadastro()[1].strip() and '' in self.Variaveis_Cadastro()[3].strip():
            self.Func_Erro_Dados()
        else:
            query = """
                UPDATE clients
                SET nome = ?, telefone = ?, endereco = ?, cidade = ?
                WHERE codigo = ?
            """
            lista =[]
            for n in self.Variaveis_Cadastro()[1:]:
                lista.append(n)
            lista.append(self.Variaveis_Cadastro()[0])
            self.Organiza_bd_Add_Del_Alt(query, lista, verificar=False)

class Banco_de_dados():
    def Conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()

    def Desconecta_bd(self):
        self.conn.close()

    def Monta_Tabela_Vendas(self):
        self.Conecta_bd()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS vendas(
                cod_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_produto INTEGER,
                nome_produto CHAR(30),
                valor_venda INTEGER,
                cod_cliente INTEGER NOT NULL,
                nome_cliente CHAR(50),
                data CHAR(10)
            );""")
        self.conn.commit()
        self.Desconecta_bd()

    def Monta_Tabela_Cadastro(self):
        self.Conecta_bd()
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome CHAR(50) NOT NULL,
                telefone INTEGER,
                endereco CHAR(50),
                cidade CHAR(30)
            );""")
        self.conn.commit()
        self.Desconecta_bd()

class ToolBar():
    def Menu(self, root):
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)
        self.menutool_Opcao = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Opções", menu=self.menutool_Opcao)

        self.menutool_Opcao.add_command(label="Tela Clientes", command=self.Organiza_Funcs_Cadastro)
        self.menutool_Opcao.add_command(label="Tela Vendas", command=self.Organiza_Funcs_Vendas)
        self.menutool_Opcao.add_command(label="Quit", command=root.quit)

class Main(Funcs_Globais, JanelaUser, Banco_de_dados, ToolBar, JanelaVendas, JanelaCadastro):
    def __init__(self, master=None):
        self.root = tk.Tk()
        self.JanelaPrincipal()
        self.Monta_Tabela_Cadastro()
        self.Monta_Tabela_Vendas()
        self.Organiza_Funcs_Inicial()
        self.root.mainloop()

    def JanelaPrincipal(self):
        self.root.title("Menu")
        self.root.configure(background="#2F4F4F")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

    def Organiza_Funcs_Inicial(self):
        self.Tela_Inicial(self.root)
        self.Info_Labls_Inicial()
        self.Info_Entrys_Inicial()
        self.Info_Btoes_Inicial()

    def Organiza_Funcs_Vendas(self):
        self.Tela_Vendas(self.root)
        self.Variaveis_caixa3()
        self.Info_Btoes_Vendas()
        self.Info_Labls_Vendas()
        self.Info_Entrys_Vendas()
        self.Func_Criar_Treeview(verificar=True)
        self.Info_Cabecario_Vendas()
        self.Info_Colunas_Vendas()
        self.Func_Select_Lista(verificar=True)

    def Organiza_Funcs_Cadastro(self):
        self.iniciar = tk.Toplevel(self.root)
        self.Janela_Cadastro(self.iniciar)
        self.Info_Btoes_Cadastro()
        self.Info_Labls_Cadastro()
        self.Info_Entrys_Cadastro()
        self.Func_Criar_Treeview(verificar=False)
        self.Info_Cabecario_Cadastro()
        self.Info_Colunas_Cadastro()
        self.Func_Select_Lista(verificar=False)
        self.iniciar.protocol("WM_DELETE_WINDOW", self.Janela_fechada)

if __name__ == "__main__":
    Main()
