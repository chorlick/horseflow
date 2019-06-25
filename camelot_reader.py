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
    aVal = ""
    weight = ""
    pp = ""
    st = ""
    quartFraction = ""
    threeEights = ""
    strVal = ""
    fin = ""
    jockey = ""
    purse = ""
    odds = ""
    

    def __str__(self):
        return "[lastRaceData:"  + self.lastRaceDate + \
                ", lastRaceLoc:" + self.lastRaceLoc + \
                ", horseName:"   + self.horseName + \
                ", medications:" + self.medications + \
                ", A:"           + self.aVal + \
                ", weight:"      + self.weight + \
                ", pp:"          + self.pp + \
                ", st:"          + self.st + \
                ", quartFraction:" + self.quartFraction + \
                ", threeEights:" + self.threeEights + \
                ", strVal:"      + self.strVal + \
                ", fin:"         + self.fin + \
                ", jockey:"      + self.jockey + \
                ", purse:"       + self.purse + \
                ", odds:"        + self.odds + \
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
    return re.findall(r'^(.*?)\s.', line)
    

def getLastRaceLoc(line) :
    return re.findall(r'^(.*?)\s.', line.strip())


def getHorseName(line) :
    return re.findall(r'^(\w\'?.*?)[L|M]', line.strip())

def getHorseMedications(line) :
    return re.findall(r'^([M|L])\s.', line.strip())

def getHorseEquipment(line) :
    return re.findall(r'^(bf\s.*?)|(b\s.*?)|(f\s.*?)|(fb\s.*?)\s.', line.strip())

def getHorseAVal(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseWeight(line) :
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorsePP(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseSt(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseQuarterFraction(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseThreeEightsFraction(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseStrVal(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseFin(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getJockey(line):
    return re.findall(r'^(\w.*?)[0-9]', line.strip())

def getPurse(line):
    return re.findall(r'^(\d+.*?)[0-9]', line)

def getOdds(line):
    return re.findall(r'(\d+\.?\d*)', line)

horseObjs = []
#for horse in horses[1: len(horses)] :
for horse in horses[1: 3] :
    b_horse = ' '.join(horse).replace('\n', ' ').replace('\r', ' ')
    h = RaceLine()
    print(b_horse)
    h.lastRaceDate = getLastRaceDate(b_horse)
    b_horse = b_horse[len(h.lastRaceDate[0]):]
    h.lastRaceLoc = getLastRaceLoc(b_horse )
    b_horse = b_horse[len(h.lastRaceLoc[0]) + 2:]
    h.horseName = getHorseName(b_horse)
    b_horse = b_horse[len(h.horseName[0]):]
    h.medications = getHorseMedications(b_horse)
    b_horse = b_horse[len(h.medications[0]):]
    h.equipment = getHorseEquipment(b_horse)
    b_horse = b_horse[len(h.equipment[0]):]
    h.aVal = getHorseAVal(b_horse)
    b_horse = b_horse[len(h.aVal[0]) + 1:]
    h.weight = getHorseWeight(b_horse)
    b_horse = b_horse[len(h.weight[0]):]
    h.pp = getHorsePP(b_horse)
    b_horse = b_horse[len(h.pp[0]):]
    h.st = getHorseSt(b_horse)
    b_horse = b_horse[len(h.st[0]):]
    h.quartFraction = getHorseQuarterFraction(b_horse)
    b_horse = b_horse[len(h.quartFraction[0]):]
    h.threeEights = getHorseThreeEightsFraction(b_horse)
    b_horse = b_horse[len(h.threeEights[0]):]
    h.strVal = getHorseStrVal(b_horse)
    b_horse = b_horse[len(h.strVal[0]):]
    h.fin = getHorseFin(b_horse)
    b_horse = b_horse[len(h.fin[0]):]
    h.jockey = getJockey(b_horse)
    b_horse = b_horse[len(h.jockey[0]):]
    h.purse = getPurse(b_horse)
    b_horse = b_horse[len(h.purse[0]):]
    h.odds = getOdds(b_horse)
    horseObjs.append(h)

print(horseObjs[0])
    



#^(.*?)\s.
#^(.*?)\s+
#^(.*?)[M\L]