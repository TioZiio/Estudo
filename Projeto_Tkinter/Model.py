import sqlite3
import View_IV

class Main_db():
    def __init__(self, root):
        self.root = root
        self.create = View_IV.Create(self.root)
        self.Monta_Tabela_Vendas()
        self.Monta_Tabela_Cadastro()
        
    def Conecta_db(self):
        db = 'clientes.db'
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        
    def Desconecta_db(self):
        self.cursor.close()
        
    def Monta_Tabela_Vendas(self):
        self.Conecta_db()
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
        self.Desconecta_db()

    def Monta_Tabela_Cadastro(self):
        self.Conecta_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome CHAR(50) NOT NULL,
                telefone INTEGER,
                endereco CHAR(50),
                cidade CHAR(30)
            );""")
        self.conn.commit()
        self.Desconecta_db()

    def Puxa_nome(self, codigo=0):
        self.Conecta_db()
        try:
            self.cursor.execute(f"""SELECT nome FROM clients WHERE codigo = {codigo};""")
            nome_cliente = self.cursor.fetchall()
            self.Desconecta_db()
            return nome_cliente[0][0]
        except (TypeError, IndexError) as error:
            print(f'Erro!! {error}')
            self.Desconecta_db()
            return False

    def Func_Select_Lista(self, verificar=True):
        # Função que atualiza e mostra os dados dentro da Lista.
        self.Conecta_db()
        if verificar:
            dados = self.cursor.execute(
                """SELECT * FROM vendas ORDER BY cod_venda DESC;"""
            )
        else:
            dados = self.cursor.execute("""SELECT * FROM clients ORDER BY nome ASC;""")
        variavel_local = [n for n in dados]
        self.Desconecta_db()
        return variavel_local

    def Organiza_query_db(self, query, parametros):
        self.Conecta_db()
        try:
            self.cursor.execute(query, parametros)
            self.conn.commit()
            self.Desconecta_db()
        except Exception as error:
            print(f"Erro query db: {error}\nLinha 80")

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