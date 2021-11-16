import sqlite3
from sqlite3 import Error


class CreateDB:

    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None

    def create_connect(self):
        try:
            self.conn = sqlite3.connect(self.dbname)
            print('Yes connect db %s' % self.dbname)
            self.__create_table()
        except Error as e:
            print(e)

    def __create_table(self):
        curr = self.conn.cursor()
        table = """ CREATE TABLE IF NOT EXISTS MESSAGE (
                    id INTEGER PRIMARY KEY,
                    text TEXT NOT NULL,
                    date_create datetime NOT NULL,
                    published BOOLEAN DEFAULT TRUE);
                """
        curr.execute(table)
        self.conn.close()
