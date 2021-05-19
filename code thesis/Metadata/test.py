from word import Word
from speaker import Speaker
from speech_segment import Speech_Segment
import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

#test="transon_n_est_pas_couche-Inatheque-7261477.001-DLTV___tv-FR2___20200125-2327___20200126-0218.XML"

def title(str):
    x = str.split("-")
    return x[0]

def date(str):
    x = str.split("___")
    y = x[2]
    return y[0:8]

def date2(str):
    x = str.split("-")
    y = x[1]
    return y[0:8]

def num(str):
    x = str.split("___")
    y = x[2]
    year = int(y[0:4])
    month = int(y[4:6])
    day = int(y[6:8])
    rep_date = datetime.datetime(year,month,day)
    day_of_year = rep_date.timetuple().tm_yday
    return day_of_year

def num2(str):
    x = str.split("-")
    y = x[1]
    year = int(y[0:4])
    month = int(y[4:6])
    day = int(y[6:8])
    rep_date = datetime.datetime(year,month,day)
    day_of_year = rep_date.timetuple().tm_yday
    return day_of_year

def read_transcription(file, Speaker_list, Speech_segmetns):
    for string in file:
        str = string.split(" ", 1)
        if str[0] == "<Speaker":
            Speaker_list.append(Speaker(str[1]))
        if str[0] == "<SpeechSegment":
            Speech_segmetns.append(Speech_Segment(str[1]))
        if str[0] == "<Word":
            Speech_segmetns[-1].words.append(Word(str[1]))

def med_words(str):
    current = str
    ff = open(current, "r")
    speakers = []
    segments = []
    read_transcription(ff,speakers,segments)
    count_seg = []
    for i in segments:
        count = 0
        for j in i.words:
            count += 1
        count_seg.append(count)
    ff.close()
    return np.mean(count_seg)

def rename():
    basepath = "transcriptions/"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            try:
                os.rename(os.path.join(basepath, entry),os.path.join(basepath, title(entry) + "-" + date(entry) + ".xml"))
            except:
                continue
            
def compute():
    count_words = []
    basepath = "transcriptions/"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            try:
                current = emission(os.path.join(basepath, entry))
                count_words.append(current.med_words)
            except:
                continue
    plt.plot(count_words)
    plt.show()
    
            

class emission:
    def __init__(self, str):
        self.title = title(str)
        self.date = date2(str)
        self.num_in_year = num2(str)
        #Début : 01/01/2008
        self.overall_index = (int(self.date[0:4])-2008)*365+self.num_in_year
        self.med_words = med_words(str)

#test_em = emission(test)
#print(test_em.title)
#print(test_em.date)
#print(test_em.num_in_year)
#print(test_em.overall_index)
#print(test_em.med_words)

#rename()
compute()