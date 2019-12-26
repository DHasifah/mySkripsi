import Sastrawi
# import nltk
# import pandas
# import numpy
# from sklearn.feature_extraction.text import TfidfVectorizer
import re
import string
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math

text1 = "teks ini seharusnya berisi data teks crawling dari twitter pada file skripsi.py"
# text1 ="teks"
#preprocessing
def remove_string_special_character(s):
	stripped = re.sub('[^\w\s]', '', s)
	stripped = re.sub('_', '', stripped)
	stripped = re.sub('\s+', ' ', stripped)
	stripped = stripped.strip()
	return stripped

#jumlah kata pada dokumen
def get_doc(sent):
	doc_info = []
	i = 0
	for sent in text_sents_clean:
		i += 1
		count = count_words(sent)
		temp = {'tweet_id': count, 'doc_length' : i}
	doc_info.append(temp)
	return doc_info

#memisahkan dokumen tiap kata
def count_words(sent):
	count = 0
	words = sent.split(' ')
	for word in words:
		count += 1
	return count

#jumlah kata pada dokumen
def create_freq_dict(sents):
	i=1
	freqDict_list = []
	for sent in sents:
		# i += 1
		freq_dict = {}
		words = sent.split(' ')
		for word in words:
			word = word.lower()
			if word in freq_dict:
				freq_dict[word] += 1
			else:
				freq_dict[word] = words
			temp = {'tweet_id' : i, 'freq_dict' : freq_dict}
		freqDict_list.append(temp)
	return freqDict_list

#perhitungan ITD skor menggunakan normalisasi frekuensi kata baku yang muncul dalam sebuah data yaitu dengan memperhatikan jumlah kemunculan kata
def computeITD(doc_info, freqDict_list):
	ITD_score = []
	maxFreq = max(freqDict_list[0]['freq_dict'].values())
	# print(freqDict_list[2].values())
	for tempDict in freqDict_list:
		id = tempDict['tweet_id']
		for k in tempDict['freq_dict']:
			temp = {'term' : k,'ITD_score' : 0.5+0.5*tempDict['freq_dict'][k]/maxFreq} 			
			ITD_score.append(temp)		
	return ITD_score

#perhitungan ITS skor menggunakan Document frequency 
def computeITS(doc_info, freqDict_list):
	ITS_score = []
	for dict in freqDict_list:
		for k in dict['freq_dict'].keys():
			for l in freqDict_list:
				a = list(l['freq_dict'].keys())
				if a[0]==k:
					count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
					temp ={'term' : k, 'ITS_score' : l['freq_dict'][k]**2}
					ITS_score.append(temp)
	return ITS_score

#perhitungan ITD ITS skor
def computeITDITS(ITD_scores, ITS_scores,freqDict_list):
	ITDITS_scores = []
	for i in ITD_scores:
		for j in ITS_scores:
			if i['term']==j['term']:
				temp = {'term' : i['term'], 'skor' : i["ITD_score"]*j["ITS_score"]}
				ITDITS_scores.append(temp)
	return ITDITS_scores

# words = sent_tokenize(text1)
# print(words)
# words = text1.split(' ')
# print(words)

text_sents = text1.split(' ')
text_sents_clean = [remove_string_special_character(s) for s in text_sents]

doc_info = get_doc(text_sents_clean)
freqDict_list = create_freq_dict(text_sents_clean)
ITD_scores = computeITD(doc_info, freqDict_list)
# print(freqDict_list)
ITS_scores = computeITS(doc_info, freqDict_list)
ITDITS_scores = computeITDITS(ITD_scores, ITS_scores,freqDict_list)
print(doc_info)
print(freqDict_list)
# print(tempDict)
# print(ITD_scores)
# print(ITS_scores)
# print(ITDITS_scores)