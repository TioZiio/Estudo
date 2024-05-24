import sqlite3
from Model import Model_init

class Func_db():
    def __init__(self):
        self.banco = Model_init.Main_db()
        self.cursor = self.banco.Conecta_db()

    def Puxa_nome(self, codigo=0):
        try:
            self.cursor.execute(f"""SELECT nome FROM clients WHERE codigo = {codigo};""")
            nome_cliente = self.cursor.fetchall()
            return nome_cliente[0][0]
        except (TypeError, IndexError) as error:
            print(f'Log Puxa_nome: {error}')
            nome_cliente = 'nulo'
            return nome_cliente

    def Func_Select_Lista(self, typTela='cadastro', mes=None):
        # Função que atualiza e mostra os dados dentro da Lista.
        match typTela:
            case 'vendas':
                query = """SELECT * FROM vendas 
                        WHERE data LIKE ?
                        ORDER BY data DESC;"""
                dados = self.cursor.execute(query, [mes[0]])
                variavel_local = [n for n in dados]
                return variavel_local
            case 'cadastro':
                dados = self.cursor.execute("""SELECT * FROM clients ORDER BY nome ASC;""")
                variavel_local = [n for n in dados]
                return variavel_local
            case 'investimento':
                self.cursor.execute("""
                    SELECT * FROM investimentos 
                    UNION ALL 
                    SELECT '->', 'Total', SUM(valor) 
                    FROM investimentos;""")
                dados = self.cursor.fetchall()
                return dados
            case _:
                print('Log Erro Func_Select_Lista')

    def Organiza_query_db(self, query, parametros=None, typTela='vendas'):
        if typTela == 'vendas':
            self.cursor.execute(query, parametros)
        elif typTela == 'relatorio':
            if parametros != None:
                self.cursor.execute(query, parametros)
            else:
                self.cursor.execute(query)
            dados = self.cursor.fetchall()
            return dados            

    def Adicionar_db_vendas(self, dados):
        try:
            query = """INSERT INTO vendas (
                cod_produto, nome_produto, valor_venda, cod_cliente, nome_cliente, data
            ) VALUES (?, ?, ?, ?, ?, ?)"""
            valores = (
                dados['Cod Produto'], dados['Nome Produto'],
                dados['Valor'], dados['Cod Cliente'],
                dados['Nome Cliente'], dados['Data']
            )
            self.Organiza_query_db(query, valores)
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
            valores = (
                dados['Cod Produto'], dados['Nome Produto'],
                dados['Valor'], dados['Cod Cliente'],
                dados['Nome Cliente'], dados['Data'], dados['Cod Venda']
            )
            self.Organiza_query_db(query, valores)
        except Exception as erro:
            print(f'Erro alt Vendas: {erro}')

    def Apagar_db_vendas(self, dados):
        try:
            query = """DELETE FROM vendas WHERE cod_venda = ?"""
            self.Organiza_query_db(query, [dados['Cod Venda']])
        except Exception as erro:
            print(f'Erro del Vendas: {erro}')

    def buscar_db_cadastro(self, coluna, pesquisa):
        try:
            self.cursor.execute(f"SELECT * FROM clients WHERE {coluna} LIKE ? ORDER BY nome ASC", (pesquisa,))
            buscar_coluna = self.cursor.fetchall()
            return buscar_coluna
        except Exception as erro:
            print(f'Erro busc Cadatro: {erro}')
            return False

    def Adicionar_db_cadastro(self, dados):
        try:
            query = """INSERT INTO clients (nome, telefone, endereco, cidade) VALUES (?, ?, ?, ?)"""
            valores = (
                dados['nome'], dados['telefone'], dados['endereco'], dados['cidade']
            )
            self.Organiza_query_db(query, valores)
        except Exception as erro:
            print(f'Erro add Cadastro: {erro}')
            
    def Alterar_db_cadastro(self, dados):
        try:
            query = """
                UPDATE clients
                SET nome = ?, telefone = ?, endereco = ?, cidade = ?
                WHERE codigo = ?
            """
            valores = (
                dados['nome'], dados['telefone'],
                dados['endereco'], dados['cidade'], dados['codigo']
            )
            self.Organiza_query_db(query, valores)
        except Exception as erro:
            print(f'Erro alt Cadastro: {erro}')

    def Apagar_db_cadastro(self, dados):
        try:
            query = """DELETE FROM clients WHERE codigo = ?"""
            self.Organiza_query_db(query, [dados['codigo']])
        except Exception as erro:
            print(f'Erro del Cadastro: {erro}')

    def Relatorio_mensal(self, parametros):
        try:
            query = """SELECT nome_produto, SUM(valor_venda) as valores
                    FROM vendas
                    WHERE data LIKE ?
                    GROUP BY nome_produto
                    UNION ALL
                    SELECT 'Total', SUM(valor_venda)
                    FROM vendas
                    WHERE data LIKE ?;"""
            dados = self.Organiza_query_db(typTela='relatorio', query=query, parametros=parametros)
            return dados
        except Exception as erro:
            print(f'Erro Relatorio mensal: {erro}')

    def Relatorio_por_cliente(self):
        try:
            query = """
                SELECT cod_cliente, nome_cliente, SUM(valor_venda) AS total_vendas 
                FROM vendas 
                GROUP BY cod_cliente, nome_cliente
                ORDER BY total_vendas DESC;"""
            dados = self.Organiza_query_db(query=query, typTela='relatorio')
            return dados
        except Exception as erro:
            print(f'Erro Relatorio por cliente: {erro}')

    def Adicionar_investimento(self, dados):
        try:
            query = """INSERT INTO investimentos (produto, valor) VALUES (?,?);"""
            valores = (dados['produto'], dados['valor'])
            self.Organiza_query_db(query, parametros=valores, typTela='relatorio')
        except Exception as erro:
            print(f'Erro add Relatorio: {erro}')

    def Apagar_investimentos(self, dados):
        try:
            query = """DELETE FROM investimentos WHERE codigo_relatorio = ?"""
            self.Organiza_query_db(query=query, parametros=[dados['cod.invest']])
        except Exception as erro:
            print(f'Erro del Investimento: {erro}')

    def Log_Clientes_Novos(self):
        try:
            query = """
                SELECT codigo, nome, telefone, endereco FROM clients_log
                ORDER BY id ASC"""
            dados = self.Organiza_query_db(query=query, typTela='relatorio')
            return dados
        except Exception as erro:
            print(f'Erro Clientes Novos: {erro}')
