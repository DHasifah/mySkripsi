import math
from SkripsiModel import SkripsiModel

database = SkripsiModel()

#jumlah frequeansi sebuah kata pada dokumen
def create_frequency(words):
	freq=0
	frequency = {}
	for word in words:
		if word in frequency:
			frequency[word] += 1
		else:	
			frequency[word] = 1
	return frequency

# perhitungan ITD skor menggunakan normalisasi frekuensi 
def computeITD(frequency):
	ITD_score = []
	maxFreq = max(frequency.values())
	for tempDict in frequency:
		temp = {'term' : tempDict,'ITD_s' : 0.5+0.5*frequency.get(tempDict)/maxFreq} 			
		ITD_score.append(temp)
	return ITD_score

# #perhitungan ITS skor menggunakan Document frequency 
def computeITS(frequency):
	ITS_score = []
	for tempDict in frequency:
		for k in frequency:
			temp ={'term' : tempDict, 'ITS_s' : math.log10(len(frequency)/frequency.get(tempDict))+1}
		ITS_score.append(temp)
	return ITS_score

#perhitungan ITD ITS skor
def computeITDITS(ITD_score, ITS_score,frequency):
	ITDITS_scores = {}
	for i in ITD_score:
		for j in ITS_score:
			if i['term']==j['term']:
				ITDITS_scores.update({i['term']:i["ITD_s"]*j["ITS_s"]})		
	return ITDITS_scores


for data in database.getData():
	current_texts = data[2].split(' ')
	frequency = create_frequency(current_texts)
	ITD_score = computeITD(frequency)
	ITS_score = computeITS(frequency)
	ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
	# print(frequency)