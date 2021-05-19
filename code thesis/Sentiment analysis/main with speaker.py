from word import Word
from speaker import Speaker
from speech_segment import Speech_Segment
import os

# each class contains all information mentioned iиририn .xml with the same name as in .xml;
# also speech_segment contains list of words in this segment
# tests for classes

speaker = Speaker(
    "ch=\"1\" dur=\"21.06\" gender=\"2\" spkid=\"S0\" lang=\"fre\" lconf=\"1.00\" nw=\"89\" tconf=\"0.91\"/>")
word = Word("id=\"1\" stime=\"0.00\" dur=\"0.06\" conf=\"0.84\"> en")
segment = Speech_Segment(
    "ch=\"1\" sconf=\"1.00\" stime=\"16.860\" etime=\"33.190\" spkid=\"S4\" lang=\"fre\" lconf=\"1.00\" trs=\"1\">")
print(word.id, word.stime, word.dur, word.conf, word.word)
print(speaker.id, speaker.dur, speaker.gender, speaker.spkid, speaker.lang, speaker.lconf, speaker.nw, speaker.tconf)
print(segment.ch, segment.sconf, segment.stime, segment.etime, segment.spkid, segment.lang, segment.lconf, segment.trs)


# function for reading one file

def read_transcription(file, Speaker_list, Speech_segmetns):
    for string in file:
        str = string.split(" ", 1)
        if str[0] == "<Speaker":
            Speaker_list.append(Speaker(str[1]))
        if str[0] == "<SpeechSegment":
            Speech_segmetns.append(Speech_Segment(str[1]))
        if str[0] == "<Word":
            Speech_segmetns[-1].words.append(Word(str[1]))

path = "transcriptions/"
listeEmissions = open("list.txt", "w")

sortedList = []
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        #print(entry)
        sortedList.append(entry)
sortedList.sort()
for i in range(len(sortedList)):
    if i!=0:
        listeEmissions.write(sortedList[i])
        listeEmissions.write("\n")
listeEmissions.close
# test of reading file
# speakers is a list of speakers mentioned in .xml
# speech_segments is a list of segments found in .xml
path = "transcriptions/"
f = open("list.txt", "r")

writing = open("result with speaker.csv", "w")
counter = 0
for current in f:
    current = path + current[:-1]
    if 'm' == current[-1]:
        print(current)
        continue
    ff = open(current, "r")
    speakers = []
    speech_segmetns = []
    read_transcription(ff, speakers, speech_segmetns)
    writing.write("number_of_text, speaker, text, length\n")
    for i in speech_segmetns:
        count = 0
        writing.write(str(counter))
        writing.write(",")
        writing.write(i.spkid)
        writing.write(",")
        for j in i.words:
            writing.write(j.word + " ")
            count += 1
        writing.write(",")
        writing.write(str(count))
        writing.write("\n")
    ff.close()
    counter+=1
f.close()
writing.close()
print(counter)
