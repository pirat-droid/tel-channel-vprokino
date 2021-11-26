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
                    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    date_create datetime NOT NULL,
                    published BOOLEAN DEFAULT TRUE,
                    image VARCHAR (100) NULL );
                """
        curr.execute(table)
        index = 'CREATE INDEX "message_id" ON "MESSAGE" ("id");'
        curr.execute(index)
        index = 'CREATE INDEX "message_date_create" ON "MESSAGE" ("date_create");'
        curr.execute(index)
        self.conn.close()
