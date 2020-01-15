import psycopg2 as pg
import json

class Term:
    TABLE   = 'term'
    KEY     = 'id'
    COLUMNS = ['term']
    TYPES   = ['%s']

    def __init__(self):
        self.conn   = pg.connect('user=postgres password=051997 dbname=skripsi')
        self.conn.autocommit = True
        self.cur    = self.conn.cursor()
        self.types  = ', '.join(self.TYPES)

    def getAll(self):
        self.cur.execute('select term from '+self.TABLE)
        return self.cur.fetchall()

    def insert(self, term):
        col = ', '.join(self.COLUMNS)
        try:
            self.cur.execute('insert into '+self.TABLE+' ('+col+') values ('+self.types+')',(term))
        except Exception as e:
            print(e)

    def term(self, data, id):
        self.cur.execute('update '+self.TABLE+' set term=\''+data+'\' where '+self.KEY+'='+str(id))