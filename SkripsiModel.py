import psycopg2 as pg

class SkripsiModel:
    TABLE   = 'kuliner'
    KEY     = 'id'
    COLUMNS = ['konten', 'preprocessing', 'bobot', 'kategori','tanggal, filtering']
    TYPES   = ['%s','%s','%s','%s','%s', '%s']

    def __init__(self):
        self.conn   = pg.connect('user=postgres password=051997 dbname=skripsi')
        self.conn.autocommit = True
        self.cur    = self.conn.cursor()
        self.types  = ', '.join(self.TYPES) 

    def getAll(self):
        self.cur.execute('select * from '+self.TABLE)
        return self.cur.fetchall()

    def insert(self, konten, preprocessing, bobot, kategori, tanggal, filtering):
        col = ', '.join(self.COLUMNS)
     #    print('insert into '+self.TABLE+' ('+col+') values ('+self.types+')')
     #    print(','.join(data))
        try:
            self.cur.execute('insert into '+self.TABLE+' ('+col+') values ('+self.types+')',(konten, preprocessing, bobot, kategori, tanggal, filtering))
        except Exception as e:
            print(e)

    def update(self, data, id):
        self.cur.execute('update '+self.TABLE+' set preprocessing=\''+data+'\' where '+self.KEY+'='+str(id))
 
    def getTweet(self):
        self.cur.execute('select id, preprocessing from '+self.TABLE)
        return self.cur.fetchall()

    def fil(self, data, id):
        self.cur.execute('update '+self.TABLE+' set filtering=\''+data+'\' where '+self.KEY+'='+str(id))
 