from SkripsiModel import SkripsiModel
from db2 import Term

database = Term();
database_kuliner = SkripsiModel();

single_word=[]
for data in database.getAll():
	single_word.append(data[0])

data_kuliner=[]
for data2 in database_kuliner.getData():
	ID = data2[0]
	term = []
	kelas = {};
	for key,value in data2[3].items():
		term.append(key)
		kelas[key]=value
	for i in single_word:
		if not i in term:
			kelas[i]=0.0

	kelas_kategori = input(data2[2]+' | Kategori : ')
	database_kuliner.kategori_awal(kelas_kategori,data2[0])
	database_kuliner.itdits(kelas,data2[0])