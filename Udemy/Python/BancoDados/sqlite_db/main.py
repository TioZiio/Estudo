
import sqlite3

from variables import db_file, table_name

class DataBase():
    # C - Create / INSERT
    # R - Read / SELECT
    # U - Update / UPDATE
    # D - Delete / DELETE
    def __init__(self):
        self.organizeCommands()

    def initDb(self):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def closeDb(self):
        self.cursor.close()
        self.conn.close()

    def createTables(self):
        self.conn.execute(f"""
            CREATE TABLE IF NOT EXISTS  {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                height REAL
            )"""
        )
        self.conn.commit()

    def insertDatas(self):
        # Comando conn.execute para querys unicas
        # Comando conn.executemany para querys com vários dados
        query = f"""INSERT INTO {table_name} (name, height) VALUES (?,?)"""
        values = ["Zaratrusta", 2.10]
        many_values = (
            ("TioZiio", 1.82),
            ("Arthur Morgan", 1.61),
            ("Percival Smith", 1.96)
        )
        self.conn.execute(query, values)
        self.conn.executemany(query, many_values)
        self.conn.commit()

    def clearSequence(self):
        # Limpa a sequence do AUTOINCREMENT;
        self.deleteAll()
        self.conn.execute(f"""
            DELETE FROM sqlite_sequence WHERE name="{table_name}";
        """)
        self.conn.commit()

    def deleteCases(self):
        query = f'DELETE FROM {table_name} WHERE id = ?'
        values = '2'
        self.conn.execute(query, values)
        self.conn.commit()

    def deleteAll(self):
        self.conn.execute(f"DELETE FROM {table_name};")
        self.conn.commit()

    def selectDatas(self):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        for row in self.cursor.fetchall():
            _id, _name, _height = row

            print('ID: ', _id)
            print('Name: ', _name)
            print('Height: ', _height)
            print('\n', 22 * '#', '\n')
        self.conn.commit()

    def updateDatas(self):
        query = f"""
            UPDATE {table_name}
            SET name = ?
            WHERE id = 3;
        """
        val = ('Marcola',)
        self.conn.execute(query, val)
        self.conn.commit()

    def organizeCommands(self):
        self.initDb()

        self.createTables()
        self.clearSequence()

        self.insertDatas()
        self.selectDatas()
        self.updateDatas()
        self.selectDatas()
        
        self.closeDb()

if __name__ == '__main__':
    DataBase()
