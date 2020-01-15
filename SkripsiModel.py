import psycopg2 as pg
import json

class SkripsiModel:
    TABLE   = 'kuliner'
    KEY     = 'id'
    COLUMNS = ['konten', 'preprocessing','tanggal', 'filtering', 'bobot', 'kategori']
    TYPES   = ['%s','%s','%s','%s','%s', '%s']

    def __init__(self):
        self.conn   = pg.connect('user=postgres password=051997 dbname=skripsi')
        self.conn.autocommit = True
        self.cur    = self.conn.cursor()
        self.types  = ', '.join(self.TYPES) 

    def getAll(self):
        self.cur.execute('select * from '+self.TABLE)
        return self.cur.fetchall()

    def insert(self, konten, preprocessing, tanggal, filtering, bobot, kategori):
        col = ', '.join(self.COLUMNS)
        try:
            self.cur.execute('insert into '+self.TABLE+' ('+col+') values ('+self.types+')',(konten, preprocessing, tanggal, filtering, bobot, kategori))
        except Exception as e:
            print(e)

    def update(self, data, id):
        self.cur.execute('update '+self.TABLE+' set preprocessing=\''+data+'\' where '+self.KEY+'='+str(id))
 
    def fil(self, data, id):
        self.cur.execute('update '+self.TABLE+' set filtering=\''+data+'\' where '+self.KEY+'='+str(id))

    def getData(self):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE)
        return self.cur.fetchall()
    
    def itdits(self, data, id):
        self.cur.execute('update '+self.TABLE+' set bobot=\''+json.dumps(data)+'\' where '+self.KEY+'='+str(id))

    def jumlahDoc(self):
        self.cur.execute('select kategori, count(id) from kuliner group by kategori')
        return self.cur.fetchall()

    def kategori_awal(self,data,id):
        self.cur.execute('update '+self.TABLE+' set kategori=\''+json.dumps(data)+'\' where '+self.KEY+'='+str(id))