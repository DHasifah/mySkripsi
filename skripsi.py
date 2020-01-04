from SkripsiModel import SkripsiModel
from crawling import Crawling
import string
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from ITDITSModel import get_doc, create_frequency, computeITD, computeITS, computeITDITS
import math


crawler = Crawling()
database = SkripsiModel()

#crawling data
# data = crawler.run('\ ','id',5000)
# for tweet in data:
# 	database.insert(str(tweet.text), '', '{}',0,str(tweet.created_at),'')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

#kamus stopword yg berupa singkatan
stop_factory = StopWordRemoverFactory().get_stop_words()
more_stopword = ['yg','utk','pd','jk','tdk','kpd','kita',
'dlm','bs','dgn','akn','jg','sdh','lg','sj','ttg','dpt','udah',
'jadi', 'jd','tanpa', 'lg','dmn','kmn','siapa','tp','yg','udh', 'dg','jg','aku','kau','knp','jadi','ga','gak','dah','tak']
katahubung = stop_factory + more_stopword
dictionary = ArrayDictionary(katahubung)
str = StopWordRemover(dictionary)

#cleaning data mentah di preprocessing
for data in database.getAll():
	removeRT = re.compile('RT').sub('', data[1], count=1).lower()
	#hapus tanda baca, url, akun, emoticon, hastag
	clean = ' '.join(re.sub("([@#][^\s]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)"," ",removeRT).split(' '))
	# print((clean).split())
	# database.update(clean,data[0])

#stemming dan stopword data yg telah di lower karena ada kata hubung  huruf kapital 
for data in database.getTweet():
	removeRT = re.compile('RT').sub('', data[1], count=1)
	hubung = str.remove(removeRT)
	alldata = stemmer.stem(hubung)
	# print((alldata).split())
	# database.fil(alldata, data[0])

#pembobotan kata itd its
for data in database.getData():
	current_texts = data[0].split(' ')
	doc_info = get_doc(current_texts)
	frequency = create_frequency(current_texts)

	ITD_score = computeITD(doc_info, frequency)
	ITS_score = computeITS(doc_info, frequency)
	ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
	# print(ITD_score)
	# print(ITS_score)
	print(ITDITS_scores)
	# database.itdits(ITDITS_scores,data)
	# print(data[0])