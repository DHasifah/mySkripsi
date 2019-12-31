# import Sastrawi
# import re
# import string
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
# from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math

# kata_kunci ='soto'
text1 = 'contoh contoh teks skripsi.py'

#total kata yg menyusun dokumen
def get_doc(sent):
	doc_info = []
	length = 0
	for sent in text_sent:
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
	#frekuensi kemunculan tiap term
	freq = list(frequency.values())
	for tempDict in frequency:
		#kurang perhitungan frekuensi kemunculan tiap term
		temp = {'term' : tempDict,'ITD_score' : 0.5+0.5*frequency.get(tempDict)/maxFreq} 			
		ITD_score.append(temp)
	# print(ITD_score)
	return ITD_score

# #perhitungan ITS skor menggunakan Document frequency 
def computeITS(doc_info, frequency):
	ITS_score = []
	for tempDict in frequency:
		for k in frequency:
			# a = list(frequency.keys())
			# if a[0]==k:
			count = sum([k in tempDict for tempDict in frequency])
			temp ={'term' : tempDict, 'ITS_score' : math.log(len(frequency)/frequency.get(tempDict))}
		ITS_score.append(temp)
		# print(frequency.get(tempDict))
	return ITS_score

# #perhitungan ITD ITS skor
def computeITDITS(ITD_score, ITS_score,frequency):
	ITDITS_scores = []
	for i in ITD_score:
		for j in ITS_score:
			if i['term']==j['term']:
				temp = {'term' : i['term'], 'ITDITS_scores' : i["ITD_score"]*j["ITS_score"]}
				ITDITS_scores.append(temp)
	return ITDITS_scores

text_sent = text1.split(' ')

doc_info = get_doc(text_sent)
frequency = create_frequency(text_sent)

ITD_score = computeITD(doc_info, frequency)
ITS_score = computeITS(doc_info, frequency)
ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
print(ITD_score)
print(ITS_score)
print(ITDITS_scores)