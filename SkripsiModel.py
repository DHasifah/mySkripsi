import psycopg2 as pg
import json

class SkripsiModel:
    TABLE   = 'kuliner'
    KEY     = 'id'
    COLUMNS = ['konten', 'preprocessing','tanggal', 'filtering', 'bobot', 'kategori','status']
    TYPES   = ['%s','%s','%s','%s','%s', '%s','%s']

    def __init__(self):
        self.conn   = pg.connect('user=postgres password=051997 dbname=skripsi')
        self.conn.autocommit = True
        self.cur    = self.conn.cursor()
        self.types  = ', '.join(self.TYPES) 

    def getAll(self):
        self.cur.execute('select * from '+self.TABLE)
        return self.cur.fetchall()

    def insert(self, konten, preprocessing, tanggal, filtering, bobot, kategori, status):
        col = ', '.join(self.COLUMNS)
        try:
            self.cur.execute('insert into '+self.TABLE+' ('+col+') values ('+self.types+')',(konten, preprocessing, tanggal, filtering, bobot, kategori, status))
        except Exception as e:
            print(e)

    def update(self, data, id):
        self.cur.execute('update '+self.TABLE+' set preprocessing=\''+data+'\' where '+self.KEY+'='+str(id))
 
    def fil(self, data, id):
        self.cur.execute('update '+self.TABLE+' set filtering=\''+data+'\' where '+self.KEY+'='+str(id))

    def getData(self):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE+' where status = true')
        return self.cur.fetchall()

    def getDataTesting(self):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE+' where status = false')
        return self.cur.fetchall()

    # def getDataTrain(self):
    #     self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE)
    #     return self.cur.fetchall()

    def testing(self,id):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE+' where id ='+str(id))
        return self.cur.fetchall()

    def test(self):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE+' where status = false')
        return self.cur.fetchall()

    def getDataByCategory(self,category):
        self.cur.execute('select id, preprocessing, filtering,bobot,kategori from '+self.TABLE+' where kategori=\''+json.dumps(category)+'\' and status = true')
        return self.cur.fetchall()
    
    def itdits(self, data, id):
        self.cur.execute('update '+self.TABLE+' set bobot=\''+json.dumps(data)+'\' where '+self.KEY+'='+str(id))

    def jumlahDoc(self):
        self.cur.execute('select kategori, count(id) from kuliner group by kategori')
        return self.cur.fetchall()

    def kategori_awal(self,data,id):
        self.cur.execute('update '+self.TABLE+' set kategori=\''+json.dumps(data)+'\' where '+self.KEY+'='+str(id))
