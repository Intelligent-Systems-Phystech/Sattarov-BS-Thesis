class Word(object):
    def __init__(self, string):
        flag = False
        str = string.split(" ")
        if str[0][:3] == "id=":
            self.id = str[0][4:len(str[0]) - 1]
        else:
            flag = True
        if str[1][:6] == "stime=":
            self.stime = str[1][7:len(str[1]) - 1]
        else:
            flag = True
        if str[2][:4] == "dur=":
            self.dur = str[2][5:len(str[2]) - 1]
        else:
            flag = True
        if str[3][:5] == "conf=":
            self.conf = str[3][6:len(str[3]) - 2]
        else:
            flag = True
        self.word = str[4]
        if flag:
            raise Exception("wrong format in string \""+ string+ "\"")