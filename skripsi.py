from SkripsiModel import SkripsiModel
from crawling import Crawling
from db2 import Term
import string
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from ITDITSModel import create_frequency, computeITD, computeITS, computeITDITS
import math

crawler = Crawling()
database = SkripsiModel()
database2 = Term()

# # crawling data
# data = crawler.run('\ ','id',5)
# for tweet in data:
# 	database.insert(str(tweet.text), '',str(tweet.created_at),'','[]','[]')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

#kamus stopword yg berupa singkatan
stop_factory = StopWordRemoverFactory().get_stop_words()
more_stopword = ['yg','utk','pd','jk','tdk','kpd','kita','gk',
'dlm','bs','dgn','akn','jg','sdh','lg','sj','ttg','dpt','udah',
'jadi', 'jd','tanpa', 'lg','dmn','kmn','siapa','tp','yg','udh', 
'dg','jg','aku','kau','knp','jadi','ga','gak','dah','tak','ne','met','gw','c','a','gk','ar',
'b','klo','dr','mo','po','i','u','e','wkwk', 'nmun','mnrut','sprti', 'shgga', 
'and', 'tdak', 'tdk', 'krn', 'pd','hrs', 'smentara', 'stlah', 
'blum', 'blm', 'skitar', 'bg', 'dr', 'tlah', 'sbagai', 'msh', 'ktika', 'adlah','dlam', 'mreka','sy',
'trhdap', 'scara', 'bgitu', 'drpda', 'mk','ttg', 'sblum', 'spy','sdangkn', 'smentra', 'apakh','tnpa', 
'bleh', 'dpt','oke','stiap', 'stidaknya', 'psti', 'y', 'tgl', 'tntu','di','eh','ta','nah','noh','ama']
katahubung = stop_factory + more_stopword
dictionary = ArrayDictionary(katahubung)
str = StopWordRemover(dictionary)

#cleaning data crawling
for data in database.getAll():
	removeRT = re.compile('RT').sub('', data[1], count=1).lower()
	#hapus tanda baca, url, informasi akun, emoticon, hastag
	clean = ' '.join(re.sub("([@#][^\s]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)"," ",removeRT).split(' '))
	database.update(clean,data[0])

#stemming dan stopword data yg telah dilower 
for data in database.getData():
	hubung = str.remove(data[1])
	alldata = stemmer.stem(hubung)
	database.fil(alldata, data[0])

#single term pada tabel term
single_word=[]
for data in database.getData():
	x=data[2].split()
	x=list(set(x))
	for kata in x:
		if not kata in single_word:
			single_word.append(kata)
			database2.insert([kata])
# print(single_word)

#pembobotan kata itd its
for data in database.getData():
	current_texts = data[2].split(' ')
	frequency = create_frequency(current_texts)

	ITD_score = computeITD(frequency)
	ITS_score = computeITS(frequency)
	ITDITS_scores = computeITDITS(ITD_score, ITS_score,frequency)
	# print(ITD_score)
	# print(ITS_score)
	# print(ITDITS_scores)
	database.itdits(ITDITS_scores, data[0])