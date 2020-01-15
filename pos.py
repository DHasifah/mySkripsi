# from nltk.tag import CRFTagger
# from db2 import ITDITS

# database2 = ITDITS()
# ct = CRFTagger()

# for data in database2.getAll():
# 	ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
# 	hasil = ct.tag_sents([data])
# 	print(hasil)

#VB:kata kerja, NN:kata benda, NNP: ,NND: ,JJ:kata sifat, CD:, FW:, MD:, IN: , WH: , PRP: , SC:


from SkripsiModel import SkripsiModel

db_kuliner = SkripsiModel();

#informasi jumlah term pada 1 dokumen
data=db_kuliner.getData()
def get_doc(sents):
	doc_info = []
	i = 0
	count=0
	for sent in sents:
		i += 1
		count = count_words(sent[2])
		temp = {'tweet_id' : i, 'length' : count}
		doc_info.append(temp)
	# print(doc_info)
	return doc_info

def count_words(sent):
	count = 0
	words = sent.split()
	return len(words)

print(get_doc(data))