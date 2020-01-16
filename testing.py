import numpy as np
from testingModel import TestingModel
from SkripsiModel import SkripsiModel
from db2 import Term
from ITDITSModel import create_frequency, computeITD, computeITS, computeITDITS

database_kuliner = SkripsiModel()
database2 = Term()
database_testing = TestingModel()

# J_0	: soto
# J_1	: gudeg
# J_2	: rawon
# J_3	: sate
# J_4	: rujak
# J_5	: pempek
# J_6	: rendang
# J_7	: pecel
# J_8	: kuliner lain
# J_9	: bukan kuliner

#total dokumen
x = database_kuliner.getData()
D=len(x)
# print({'total dokumen ': D})

#bobot kelas (prior probability)
Dj = database_kuliner.jumlahDoc()
term=[]
kelas={}
dataKelas = {}
for key,value in Dj:
	term.append(key)
	bobot_kelas=value/D
	kelas[key]=bobot_kelas
	# print(value)
	# print({'kelas ': key, 'bobot kelas ': bobot_kelas})
	dtk = database_kuliner.getDataByCategory(key)
	dataKelas[key] = dtk


#jumlah dokumen kelas tersebut
# for Dj in database_kuliner.jumlahDoc():
	# print(Dj)

#frekuensi term pada setiap dokumen
data=database_kuliner.getData()
def get_doc(tweets):
	doc_info = []
	ID = 0
	count=0
	for tweet in tweets:
		ID += 1
		count = count_words(tweet[2])
		# temp = {'id' : ID, 'length' : count}
		temp = count
		doc_info.append(temp)
	return doc_info

def count_words(tweet):
	count = 0
	words = tweet.split()
	return len(words)
# print({'frekuensi' :get_doc(data)})

#total term
y=database2.getAll()
Nj=len(y)
# print({'total term ': Nj})

#bobot kata (conditional probability)
ada = False
for data in database_testing.test():
	ada = True
	filtering = data[2].split()
	tertinggi = 0
	kls = ''
	for key,value in dataKelas.items():
		hasilPerkalian = 1
		for kata in filtering:
			bobotTertinggi=0
			for val in value:
				if val[3][kata] > bobotTertinggi:
					bobotTertinggi = val[3][kata] 
			hasilPerkalian = hasilPerkalian * bobotTertinggi
		hasilPerkalian = hasilPerkalian * kelas[key]
		if hasilPerkalian>tertinggi:
			tertinggi = hasilPerkalian
			kls = key
	print(tertinggi)
	print(kls)
			# for k,val in value.list():
			# 	print(val)
			# 	die()
		


if not ada:
	print("Tidak ada")
	# hasil_perkalian = hasil_perkalian*bobot_kata
		# print(hasil_perkalian)
	# print(skor)

#pengujian Naive Bayes
# 	tertinggi = 0
# 	kls = 0
# 	for key,value in kelas.items():
# 		# print(key)
# 		tot = float(value)*hasil_perkalian
# 		if tot > tertinggi:
# 			tertinggi = tot
# 			kls = key
# 	# print(kls)
# 	# print(data[4])
# 	if str(kls) == str(data[4]):
# 		benar = benar +1

# # print(benar)
# akurasi = (benar/jml_data)*100	
# print(akurasi)