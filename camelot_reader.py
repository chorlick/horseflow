import camelot
import io
import numpy as np
import pprint
import re 

class RaceLine:
    lastRaceDate = ""
    lastRaceLoc = ""
    horseName = ""
    medications = ""
    equipment = ""
    A = ""
    weight = ""
    pp = ""
    st = ""
    quartFraction = ""
    threeEights = ""
    strVal = ""
    fin = ""
    purse = ""
    odds = ""

    def __str__(self):
        return "[lastRaceData:"  + self.lastRaceDate + \
                ", lastRaceLoc:" + self.lastRaceLoc + \
                ", horseName:"   + self.horseName + \
                "]"


buffer = io.StringIO()
tables = camelot.read_pdf("./race_charts/BEL2019061901.pdf",flavor="stream")
np_matrix = tables[0].df.values
horseBlock = False
horses = []
for row in np_matrix:
    for col in row:
        if col.find("Odds $1") > -1 :
            horseBlock = True
        if col.find("OFF  AT") > -1 :
            horseBlock = False
    if(horseBlock == True) :
        horses.append(row)


def getLastRaceDate(line) :
    return line[:line.index(' ')].strip()

def getLastRaceLoc(line, offset) :
    t = line[offset + 1:]
    t = t.strip()
    t = t[:line.index(' ')]
    return t.strip()

def getHorseName(line, offset) : 
    t = line[offset + 2:]
    t = t.strip()
    print(t)
    x = re.findall(".+?(?=L|b|bf|[0-9])", t)
    return x[0].strip()

horseObjs = []
#for horse in horses[1: len(horses)] :
for horse in horses[1: 2] :
    b_horse = ' '.join(horse).replace('\n', ' ').replace('\r', ' ')
    h = RaceLine()
    print(b_horse)
    h.lastRaceDate = getLastRaceDate(b_horse)
    h.lastRaceLoc = getLastRaceLoc(b_horse, len(h.lastRaceDate) )
    h.horseName = getHorseName(b_horse, len(h.lastRaceDate) + len(h.lastRaceLoc))
    horseObjs.append(h)

print(horseObjs[0])
    
