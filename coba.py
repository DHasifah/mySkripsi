import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from keyboard import press
import math

text1 = "teks ini seharusnya berisi data crawling dari twitter pada file skripsi.py"

def remove_string_special_character(s):
	stripped = re.sub('[^\w\s]', '', s)
	stripped = re.sub('_', '', stripped)
	stripped = re.sub('\s+', ' ', stripped)
	stripped = stripped.strip()
	return stripped

def get_doc(sent):
	doc_info = []
	i = 0
	for sent in text_sents_clean:
		i += 1
		count = count_words(sent)
		temp = {'tweet_id' : i, 'doc_length' : count}
		doc_info.append(temp)
	return doc_info

def count_words(sent):
	count = 0
	words = word_tokenize(sent)
	for word in words:
		count += 1
	return count

def create_freq_dict(sents):
	i=0
	freqDict_list = []
	for sent in sents:
		i += 1
		freq_dict = {}
		words = word_tokenize(sent)
		for word in words:
			word = word.lower()
			if word in freq_dict:
				freq_dict[word] += 1
			else:
				freq_dict[word] = 1
			temp = {'tweet_id' : i, 'freq_dict' : freq_dict}
		freqDict_list.append(temp)
	return freqDict_list

def computeITD(doc_info, freqDict_list):
	ITD_score = []
	for tempDict in freqDict_list:
		id = tempDict['tweet_id']
		for k in tempDict['freq_dict']:
			temp = {'key' : k,'ITD_score' : 0.5+0.5*tempDict['freq_dict'][k]/doc_info[id-1]['doc_length']} 			
			ITD_score.append(temp)			
	return ITD_score

def computeITS(doc_info, freqDict_list):
	ITS_score = []
	counter = 0
	for dict in freqDict_list:
		counter += 0
		for dict in freqDict_list:
			for k in dict['freq_dict'].keys():
				count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
				temp = {'ITS_score' : math.log(len(doc_info)/count)/1*math.log(len(doc_info)/count), 'key' : k}
				ITS_score.append(temp)
		return ITS_score

def computeITDITS(ITD_scores, ITS_scores):
	ITDITS_scores = []
	for j in ITS_scores:
		for i in ITD_scores:
			if j == i:
				temp = {'skor': ITS_scores*ITD_scores, 
						'keterangan': i}
				ITDITS_scores.append(temp)
	return ITDITS_scores

text_sents = sent_tokenize(text1)
text_sents_clean = [remove_string_special_character(s) for s in text_sents]
doc_info = get_doc(text_sents_clean)

freqDict_list = create_freq_dict(text_sents_clean)
ITD_scores = computeITD(doc_info, freqDict_list)
ITS_scores = computeITS(doc_info, freqDict_list)
ITDITS_scores = computeITDITS(ITD_scores, ITS_scores)
# print(doc_info)
# print(freqDict_list)
print(ITD_scores) 
print(ITS_scores)
print(ITDITS_scores)