import math
from SkripsiModel import SkripsiModel

# data = 'contoh contoh teks skripsi.py'

database = SkripsiModel()

#total kata yg menyusun dokumen
def get_doc(sent):
	doc_info = []
	i = 0
	count=0
	for sent in current_texts:
		i += 1
		count = count_words(sent)
		temp = {'tweet_id' : i, 'panjang dokumen' : count}
	doc_info.append(temp)
	print(doc_info)
	return doc_info

def count_words(sent):
	count = 0
	words = sent.split()
	for word in words:
		count += 1
	return count

#jumlah sebuah kata pada dokumen
def create_frequency(words):
	freq=0
	frequency = {}
	for word in words:
		if word in frequency:
			frequency[word] += 1
		else:	
			frequency[word] = 1
	# print(frequency)
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
			temp ={'term' : tempDict, 'ITS_s' : math.log(len(frequency)/frequency.get(tempDict))+1}
		ITS_score.append(temp)
	return ITS_score

# #perhitungan ITD ITS skor
def computeITDITS(ITD_score, ITS_score,frequency):
	ITDITS_scores = []
	for i in ITD_score:
		for j in ITS_score:
			if i['term']==j['term']:
				temp = {'term' : i['term'], 'ITDITS_s' : i["ITD_s"]*j["ITS_s"]}
				ITDITS_scores.append(temp)
	return ITDITS_scores

for data in database.getData():
	current_texts = data[0].split(' ')
	doc_info = get_doc(current_texts)
	frequency = create_frequency(current_texts)
	ITD_score = computeITD(doc_info, frequency)
	ITS_score = computeITS(doc_info, frequency)
	ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
# print(math.log(3/1)
	# print(ITDITS_scores)
# print(ITS_score)
# print(ITDITS_scores)