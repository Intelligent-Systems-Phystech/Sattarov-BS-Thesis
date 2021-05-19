class Speaker(object):
    def __init__(self, string):
        flag = False
        str = string.split(" ")
        if str[0][:3] == "ch=":
            self.id = str[0][4:len(str[0]) - 1]
        else:
            flag = True
        if str[1][:4] == "dur=":
            self.dur = str[1][5:len(str[1]) - 1]
        else:
            flag = True
        if str[2][:7] == "gender=":
            self.gender = str[2][8:len(str[2]) - 1]
        else:
            flag = True
        if str[3][:6] == "spkid=":
            self.spkid = str[3][7:len(str[3]) - 1]
        else:
            flag = True
        if str[4][:5] == "lang=":
            self.lang = str[4][6:len(str[4]) - 1]
        else:
            flag = True
        if str[5][:6] == "lconf=":
            self.lconf = str[5][7:len(str[5]) - 1]
        else:
            flag = True
        if str[6][:3] == "nw=":
            self.nw = str[6][4:len(str[6]) - 1]
        else:
            flag = True
        if str[7][:6] == "tconf=":
            self.tconf = str[7][7:len(str[7]) - 3]
        else:
            flag = True
        if flag:
            raise Exception("wrong format in string \""+ string+ "\"")
