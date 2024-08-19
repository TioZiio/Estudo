
import traceback
import os
import pymysql
from dotenv import load_dotenv


class MainCommand():
    # C - Create / INSERT
    # R - Read / SELECT
    # U - Update / UPDATE
    # D - Delete / DELETE
    def __init__(self):
        load_dotenv()
        self.TABLE_NAME = 'customers'
        
        if self.startConnect() == True:
            self.organizeCommands()

    def startConnect(self):
        try:   
            self.conn = pymysql.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_DATABASE'),
                port=int(os.getenv('MYSQL_PORT'))
            )
            self.cursor = self.conn.cursor()
        except Exception as err:
            print('Conexão não estabelecida')
            print(f'Log startConnect: {err}')
            return False
        else:
            return True

    def tryExceptFinally(self, func):
        try:
            print(f'Log func completed: {func.__name__}')
            func()
        except Exception as err:
            print(30 * '_')
            print('Func Error: ', func.__name__)
            print('Name Error: ', type(err).__name__)
            print('Msg Error: ', str(err))
            print('\t**Traceback:**\n', traceback.format_exc())
            print(30 * '_')
        else:
            print(40 * '_')
        finally:
            self.conn.commit()

    def executeQuery(self, query='', datas='', verify=True):
        if len(datas) == 0 and len(query) == 0:
            return

        if len(datas) == 0 and len(query) > 0:
            self.cursor.execute(query)
            self.fet_datas = self.cursor.fetchall()
        else:
            if verify:
                self.cursor.execute(query, datas)
            else:
                self.cursor.executemany(query, datas)

    def testConnect(self):
        query = "SELECT VERSION()"
        self.executeQuery(query=query)
        self.showDatas(verify=False)
    
    def createTable(self):
        query = (f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(20) NOT NULL,
                idade INT NOT NULL,
                PRIMARY KEY (id)
            );""")
        self.executeQuery(query=query)
    
    def insertTable(self):
        query = (f"""
            INSERT INTO {self.TABLE_NAME} (
                name, idade
            ) VALUES (%s, %s);""")
        datas = ('david', 23)
        self.executeQuery(query=query, datas=datas)

    def insertDictTable(self):
        query = (f"""
            INSERT INTO {self.TABLE_NAME} (
                name, idade
            ) VALUES (%(nome)s, %(idade)s);""")
        # É necessário identificar as chaves do Dict;
        datas = {
            "nome": 'Lya',
            "idade": 24,
        }
        self.executeQuery(query=query, datas=datas)

    def insertManyTable(self):
        query = (f"""
            INSERT INTO {self.TABLE_NAME} (
                name, idade
            ) VALUES (%s, %s);""")

        many_datas = (
           ("TioZiio",24),
           ("Arthur Morgan",16),
           ("Percival Smith",15)
        )

        self.executeQuery(query=query, datas=many_datas, verify=False)

    def selectAllDatasToTable(self):
        query = (f"""
            SELECT * FROM {self.TABLE_NAME};
        """)

        self.executeQuery(query=query)
        self.showDatas()

    def showDatas(self, verify=True):
        if verify:
            for row in self.fet_datas:
                _id, _name, _age = row

                print('\n', 22 * '#', '\n')
                print('ID: ', _id)
                print('Name: ', _name)
                print('Age: ', _age)
        else:
            v = self.fet_datas
            print(f"Version MySQL: {v[0][0]}")

    def selectEspecificData(self):
        query = (F"""
            SELECT * FROM {self.TABLE_NAME}
            WHERE idade = 24;
        """)

        self.executeQuery(query=query)
        self.showDatas()

    def updateData(self):
        query = (f"""
            UPDATE {self.TABLE_NAME}
            SET name = %s
            WHERE name = %s;
        """)
        datas = ('tioziio', 'david')

        self.executeQuery(query=query, datas=datas)
        self.selectAllDatasToTable()

    def deleteData(self):
        query = (f"""
            DELETE FROM {self.TABLE_NAME}
            WHERE name = (%s);
        """)
        datas = 'tioziio'

        self.executeQuery(query=query, datas=datas)
        self.selectAllDatasToTable()

    def clearTable(self):
        query = (f"""
            TRUNCATE TABLE {self.TABLE_NAME};
        """)
        self.executeQuery(query=query)

    def organizeCommands(self):
        with self.conn:
            with self.cursor:
                self.tryExceptFinally(self.testConnect)
                # C - Create
                # self.tryExceptFinally(self.createTable)
                self.tryExceptFinally(self.insertTable)
                self.tryExceptFinally(self.insertDictTable)
                self.tryExceptFinally(self.insertManyTable)
                # R - Read
                self.tryExceptFinally(self.selectAllDatasToTable)
                self.tryExceptFinally(self.selectEspecificData)
                # U - Update
                self.tryExceptFinally(self.updateData)
                # D - Delete
                self.tryExceptFinally(self.deleteData)
                self.tryExceptFinally(self.clearTable)

if __name__ == '__main__':
    MainCommand()
