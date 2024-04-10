import sqlite3

db = 'clientes.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

class Main_db():
    def Conecta_db(self):
        self.t = 'david'
        self.cursor = cursor
        print('Conectado ao banco de dados')
        return self.cursor
        
    def Desconecta_db(self):
        self.conn = conn
        self.conn.commit()
        print(self.t)
        self.conn.close()
        print('Desconectado do banco de dados')
        
    def Monta_Tabela_Vendas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas(
                cod_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                cod_produto INTEGER,
                nome_produto CHAR(30),
                valor_venda INTEGER,
                cod_cliente INTEGER NOT NULL,
                nome_cliente CHAR(50),
                data TIMESTAMP
            );""")
        self.conn.commit()

    def Atualiza_Tabela_vendas(self):
        self.cursor.execute("""
                UPDATE vendas 
                SET data = strftime('%d-%m-%Y', substr(data, 1, 2) || '-' || substr(data, 3, 4) || '-' || '2024');
            """)
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

    def Monta_Tabela_Relatorio(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS investimentos(
                codigo_relatorio INTEGER PRIMARY KEY AUTOINCREMENT,
                produto CHAR(30)NOT NULL,
                valor INTEGER
            );""")
        self.conn.commit()

    def Organiza_Tabelas(self):
        self.Monta_Tabela_Vendas()
        self.Atualiza_Tabela_vendas()
        self.Monta_Tabela_Cadastro()
        self.Monta_Tabela_Relatorio()
        