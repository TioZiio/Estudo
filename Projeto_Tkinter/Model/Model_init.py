import sqlite3
from Model import Backup

db = 'clientes.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

class Main_db():
    def Conecta_db(self):
        self.cursor = cursor
        print('Conectado ao banco de dados')
        self.Organiza_Tabelas()
        return self.cursor
        
    def Desconecta_db(self):
        backup = Backup.main()
        self.conn = conn
        self.conn.commit()
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
        conn.commit()

    def Atualiza_Tabela_vendas(self):
        # Apenas na primeira atualização, depois gerara problema. Atualizando as datas para string vazia
        self.cursor.execute("""
                UPDATE vendas 
                SET data = strftime('%d-%m-%Y', substr(data, 1, 2) || '-' || substr(data, 3, 4) || '-' || '2024');
            """)
        conn.commit()

    def Monta_Tabela_Cadastro(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome CHAR(50) NOT NULL,
                telefone INTEGER,
                endereco CHAR(50),
                cidade CHAR(30)
            );""")
        conn.commit()

    def Monta_Tabela_Relatorio(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS investimentos(
                codigo_relatorio INTEGER PRIMARY KEY AUTOINCREMENT,
                produto CHAR(30)NOT NULL,
                valor INTEGER
            );""")
        conn.commit()

    def Monta_Tabela_Cadastro_Log(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acao TEXT,
            codigo INTEGER,
            nome CHAR(50),
            telefone INTEGER,
            endereco CHAR(50),
            cidade CHAR(30),
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""")
        conn.commit()

    def Monta_Trigger_Log_cadastro(self):
        self.cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS clients_trigger
            AFTER INSERT ON clients
            FOR EACH ROW
            BEGIN
                INSERT INTO clients_log (acao, codigo, nome, telefone, endereco, cidade)
                VALUES ('Inserção', NEW.codigo, NEW.nome, NEW.telefone, NEW.endereco, NEW.cidade);
            END;""")
        conn.commit()

    def Organiza_Tabelas(self):
        self.Monta_Tabela_Vendas()
        self.Monta_Tabela_Cadastro()
        self.Monta_Tabela_Relatorio()
        self.Monta_Tabela_Cadastro_Log()
        self.Monta_Trigger_Log_cadastro()
        