import sqlite3

class Main_db():
    def __init__(self, root):
        self.root = root
        db = 'clientes.db'
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.Monta_Tabela_Vendas()
        self.Monta_Tabela_Cadastro()
        print('Entrou no BD')
        
    def Desconecta_db(self):
        self.cursor.close()
        print('Saiu no BD')
        
    def Monta_Tabela_Vendas(self):
        self.cursor.execute("""
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

    def Monta_Tabela_Cadastro(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome CHAR(50) NOT NULL,
                telefone INTEGER,
                endereco CHAR(50),
                cidade CHAR(30)
            );""")
        self.conn.commit()

    def Puxa_nome(self, codigo=0):
        try:
            self.cursor.execute(f"""SELECT nome FROM clients WHERE codigo = {codigo};""")
            nome_cliente = self.cursor.fetchall()
            return nome_cliente[0][0]
        except (TypeError, IndexError) as error:
            print(f'Erro!! {error}')
            return False

    def Func_Select_Lista(self, typTela):
        # Função que atualiza e mostra os dados dentro da Lista.
        if typTela == 'vendas':
            dados = self.cursor.execute(
                """SELECT * FROM vendas ORDER BY cod_venda DESC;"""
            )
        else:
            dados = self.cursor.execute("""SELECT * FROM clients ORDER BY nome ASC;""")
        variavel_local = [n for n in dados]
        return variavel_local

    def Organiza_query_db(self, query, parametros):
        self.cursor.execute(query, parametros)
        self.conn.commit()

    def Adicionar_db_vendas(self, dados):
        try:
            query = """INSERT INTO vendas (
                cod_produto, nome_produto, valor_venda, cod_cliente, nome_cliente, data
            ) VALUES (?, ?, ?, ?, ?, ?)"""
            self.Organiza_query_db(query, dados)
        except Exception as erro:
            print(f'Erro add Vendas: {erro}')

    def Alterar_db_vendas(self, dados):
        try:
            query = """
                UPDATE vendas
                SET cod_produto = ?, nome_produto = ?, valor_venda = ?, 
                cod_cliente = ?, nome_cliente = ?, data = ?
                WHERE cod_venda = ?
            """
            new_dados = dados[6][0]
            dados[6] = new_dados
            self.Organiza_query_db(query, dados)
        except Exception as erro:
            print(f'Erro alt Vendas: {erro}')

    def Apagar_db_vendas(self, dados):
        try:
            query = """DELETE FROM vendas WHERE cod_venda = ?"""
            self.Organiza_query_db(query, dados[6])
        except Exception as erro:
            print(f'Erro del Vendas: {erro}')

    def Adicionar_db_cadastro(self, dados):
        try:
            query = """INSERT INTO clients (nome, telefone, endereco, cidade) VALUES (?, ?, ?, ?)"""
            self.Organiza_query_db(query, dados)
        except Exception as erro:
            print(f'Erro add Cadastro: {erro}')
            
    def Alterar_db_cadastro(self, dados):
        try:
            query = """
                UPDATE clients
                SET nome = ?, telefone = ?, endereco = ?, cidade = ?
                WHERE codigo = ?
            """
            variavel_local = dados[4][0]
            dados.pop(4)
            dados.append(variavel_local)
            self.Organiza_query_db(query, dados)
        except Exception as erro:
            print(f'Erro alt Cadastro: {erro}')

    def Apagar_db_cadastro(self, dados):
        try:
            query = """DELETE FROM clients WHERE codigo = ?"""
            self.Organiza_query_db(query, dados[4])
        except Exception as erro:
            print(f'Erro del Cadastro: {erro}')