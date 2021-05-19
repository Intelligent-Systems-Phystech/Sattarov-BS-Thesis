import os

test="l_heure_des_pros-Inatheque-636946.059-DLSAT___tv-C%2BN___20170314-0858___20170314-0944"

def date(char):
    x = char.split("___")
    y = x[2]
    return y[0:8]

def rename():
    basepath = "transcriptions/"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            try:
                os.rename(os.path.join(basepath, entry),os.path.join(basepath, "casedispute" + date(entry) + ".xml"))
            except:
                continue