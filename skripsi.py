from SkripsiModel import SkripsiModel
from crawling import Crawling
import string
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


crawler = Crawling()
model = SkripsiModel()
# pembobotan = ITDITSModel()

# data = crawler.run('\ ','id',5000)
# for tweet in data:
# 	model.insert(str(tweet.text), '', '{}',0,str(tweet.created_at),'')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

stop_factory = StopWordRemoverFactory().get_stop_words()
more_stopword = ['yg','utk','pd','jk','tdk','kpd','kita',
'dlm','bs','dgn','akn','jg','sdh','lg','sj','ttg','dpt','udah',
'jadi', 'jd','tanpa', 'lg','dmn','kmn','siapa','tp','yg','udh', 'dg','jg','aku','kau','knp','jadi','ga','gak','dah','tak']
katahubung = stop_factory + more_stopword
dictionary = ArrayDictionary(katahubung)
str = StopWordRemover(dictionary)

for data in model.getAll():
	removeRT = re.compile('RT').sub('', data[1], count=1).lower()
	#hapus tanda baca, url, akun, emoticon, hastag
	clean = ' '.join(re.sub("([@#][^\s]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)"," ",removeRT).split())
	print((clean).split())
	model.update(clean,data[0])

for data in model.getTweet():
	removeRT = re.compile('RT').sub('', data[1], count=1)
	hubung = str.remove(removeRT)
	alldata = stemmer.stem(hubung)
	print((alldata).split())
	model.fil(alldata, data[0])