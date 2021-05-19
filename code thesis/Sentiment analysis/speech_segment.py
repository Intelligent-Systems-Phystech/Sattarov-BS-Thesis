class Speech_Segment(object):
    def __init__(self, string):
        flag = False
        str = string.split(" ")
        if str[0][:3] == "ch=":
            self.ch = str[0][4:len(str[0]) - 1]
        else:
            flag = True
        if str[1][:6] == "sconf=":
            self.sconf = str[1][7:len(str[1]) - 1]
        else:
            flag = True
        if str[2][:6] == "stime=":
            self.stime = str[2][7:len(str[2]) - 1]
        else:
            flag = True
        if str[3][:6] == "etime=":
            self.etime = str[3][7:len(str[3]) - 1]
        else:
            flag = True
        if str[4][:6] == "spkid=":
            self.spkid = str[4][7:len(str[4]) - 1]
        else:
            flag = True
        if str[5][:5] == "lang=":
            self.lang = str[5][6:len(str[5]) - 1]
        else:
            flag = True
        if str[6][:6] == "lconf=":
            self.lconf = str[6][7:len(str[6]) - 1]
        else:
            flag = True
        if str[7][:4] == "trs=":
            self.trs = str[7][5:len(str[7]) - 2]
        else:
            flag = True
        if flag:
            raise Exception("wrong format in string \""+ string+ "\"")
        self.words = []