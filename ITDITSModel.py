import math
from SkripsiModel import SkripsiModel

# data = 'contoh contoh teks skripsi.py'

model = SkripsiModel()

#total kata yg menyusun dokumen
def get_doc(sent):
	doc_info = []
	length = 0
	for sent in data:
		length += 1
		no_id = 1
		temp = {'tweet_id' : no_id, 'panjang dokumen' : length}
	doc_info.append(temp)
	return doc_info

#jumlah sebuah kata pada dokumen
def create_frequency(words):
	freq=0
	frequency = {}
	for word in words:
		if word in frequency:
			frequency[word] += 1
		else:	
			frequency[word] = 1
	# print(frequency.values())
	return frequency

# perhitungan ITD skor menggunakan normalisasi frekuensi kata baku yang muncul dalam sebuah data 
#yaitu dengan memperhatikan jumlah kemunculan kata
def computeITD(doc_info, frequency):
	ITD_score = []
	maxFreq = max(frequency.values())
	for tempDict in frequency:
		temp = {'term' : tempDict,'ITD_s' : 0.5+0.5*frequency.get(tempDict)/maxFreq} 			
		ITD_score.append(temp)
	# print(ITD_score)
	return ITD_score

# #perhitungan ITS skor menggunakan Document frequency 
def computeITS(doc_info, frequency):
	ITS_score = []
	for tempDict in frequency:
		for k in frequency:
			temp ={'term' : tempDict, 'ITS_s' : math.log(len(frequency)/frequency.get(tempDict))}
		ITS_score.append(temp)
	return ITS_score

# #perhitungan ITD ITS skor
def computeITDITS(ITD_score, ITS_score,frequency):
	ITDITS_scores = []
	for i in ITD_score:
		for j in ITS_score:
			if i['term']==j['term']:
				temp = {'ITDITS_s' : i["ITD_s"]*j["ITS_s"]}
				ITDITS_scores.append(temp)
	return ITDITS_scores

for data in model.getData():
	current_texts = data[0].split(' ')
	# for kata in current_texts:
	doc_info = get_doc(current_texts)
	frequency = create_frequency(current_texts)

	ITD_score = computeITD(doc_info, frequency)
	ITS_score = computeITS(doc_info, frequency)
	ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
# print(math.log(3/1)
	# print(ITD_score)
# print(ITS_score)
# print(ITDITS_scores)