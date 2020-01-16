from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


factoryStem=StemmerFactory()
stemmer=factoryStem.create_stemmer()

factory=StopWordRemoverFactory()
stopword=factory.get_stop_words()
remover=factory.create_stop_word_remover()
#sentistrength
from sentistrength.sentistrength_idn import sentistrength
from collections import OrderedDict
import numpy as np
import re
#kamus sentistrength
config = dict()
config["negation"] = True
config["booster"]  = True
config["ungkapan"]  = True
config["consecutive"]  = True
config["repeated"]  = True
config["emoticon"]  = True
config["question"]  = True
config["exclamation"]  = True
config["punctuation"]  = True
senti = sentistrength(config)


class Textproc:
    def __init__(self):    
        self.kata=[]
        self.kamus=[]
        self.k=[]
        self.words=[]
        self.length=[]
        self.setTf=[]
        self.wordSetIdf=[]
        self.setTfIdf=[]
        self.text=[]
    
    def search(self, cursor):
        negasi = [line.replace('\n','') for line in open("sentistrength/kata-dasar.original.txt").read().splitlines()]
        #print(len(negasi))
        pro=[]
        cek=[]
        tu=[]
        wordSet=[]
        words=[]
        for i in cursor:
            kata=i['komen']
            tu=re.split(r'[^A-Za-z]+',kata)
            ak=" ".join(tu)
            stop = remover.remove(ak)
            output=stemmer.stem(stop)
            # print(output)
            Set=senti.main(ak)
            pisah=output.split()
            jadi=[]
            for k in pisah:
                for l in negasi:
                    if(k==l):
                        print(i)
                        jadi.append(l)
                        break   
            ids={'i':i['id_com'], 'kata':kata, 'd':jadi, 'senti':Set}
            cek.append(ids)
            lets={'id':i['id_com'], 'kata':stop}
            words.append(lets)
            wordSet=set(wordSet).union(set(jadi))
            pro.append({'token':tu,'stopword':stop,'stem':output, 'jadi':" ".join(jadi), 'senti':Set})
            print(pro)
            print(pisah)
            print('hasilnya = ', end='')
            print(jadi, end=' / ')
        self.text=pro
        self.kata=cek
        self.kamus=wordSet
        self.words=words

    #save length of each word
    def saveLength(self, cek, Set):
        k=[]
        for j in cek:
            wordSetA=dict.fromkeys(Set, 0)
            for i in j['d']:
                wordSetA[i]+=1
            t={'id': j['i'], 'kata':j['kata'], 'd':j['d'], 'set':wordSetA, 'senti':j['senti']}
            k.append(t)
        self.k=k

    #calculate length of each sentence
    def calcLength(self, cek):
        length=[]
        for word in cek:
            n=len(word['d'])
            length.append(n)
        self.length=length

    #calculate tf
    def tf(self, k, length, Set):
        a=0
        tf=[]
        for i in k:
            wordSetTf=dict.fromkeys(Set, 0)
            for l, j in i['set'].items():
                #wordSetTf[l]=j/length[a]
                if(length[a]!=0):
                    wordSetTf[l]=j/length[a]
                else:
                    wordSetTf[l]=0
            t={'id':i['id'], 'kata':i['kata'], 'd':i['d'], 'set':wordSetTf, 'senti':i['senti']}
            tf.append(t)
            a+=1
        self.setTf=tf

    def idf(self, k, wordSet):
    #calculate idf
        wordSetIdf=dict.fromkeys(wordSet, 0)
        import math
        b=1
        panjang=len(k)
        print(panjang)
        for i in k:
            for j, k in i['set'].items():
                if k > 0:
                    wordSetIdf[j]+=1
        #print(sorted(wordSetIdf.values()))
        #print(wordSetIdf)
        for m, n in wordSetIdf.items():
            #print(n)
            wordSetIdf[m]=math.log10(panjang/n)
        self.wordSetIdf=wordSetIdf
        

    def tfIdf(self, term, wordSetIdf, Set):
    #calculate tf&idf
        TI={}
        tfIdf=[]
        #print('Set',end=' ')
        #print(Set)
        for j in term:
            TI=dict.fromkeys(Set, 0)
            for i, m in j['set'].items():
                #print(i)
                TI[i]=m*wordSetIdf[i]
            t={'id':j['id'], 'kata':j['kata'], 'set':TI, 'senti':j['senti']}
            tfIdf.append(t)
            
        self.setTfIdf=tfIdf
