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
    halfFraction = ""
    threeQuarterFraction = ""
    strVal = ""
    fin = ""
    jockey = ""
    purse = ""
    odds = ""
    

    def __str__(self):
        return "[lastRaceData:"  + self.lastRaceDate[0] + \
                ", lastRaceLoc:" + self.lastRaceLoc[0] + \
                ", horseName:"   + self.horseName[0] + \
                ", equipment:"   + self.equipment[0] + \
                ", medications:" + self.medications[0] + \
                ", A:"           + self.aVal[0] + \
                ", weight:"      + self.weight[0] + \
                ", pp:"          + self.pp[0] + \
                ", st:"          + self.st[0] + \
                ", quartFraction:" + self.quartFraction[0] + \
                ", halfFraction:" + self.halfFraction[0] + \
                ", threeQuarterFraction:" + self.threeQuarterFraction[0] + \
                ", strVal:"      + self.strVal[0] + \
                ", fin:"         + self.fin[0] + \
                ", jockey:"      + self.jockey[0] + \
                ", purse:"       + self.purse[0] + \
                ", odds:"        + self.odds[0] + \
                "]"


buffer = io.StringIO()
tables = camelot.read_pdf("./race_charts/CD2019062301.pdf",flavor="stream")
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
    return re.findall(r'^(.*?)\s.', line.strip())
    

def getLastRaceLoc(line) :
    return re.findall(r'^(.*?)\s.', line.strip())


def getHorseName(line) :
    return re.findall(r'^(\w\'?.*?)[L]', line.strip())

def getHorseMedications(line) :
    x = re.findall(r'^([M|L])\s.', line.strip())
    if len(x) > 0 :
        return x
    else:
        return ['']

def getHorseEquipment(line) :
    x = re.findall(r'(?:b|f)+\s+', line.strip())
    if len(x) > 0:
        return x
    else:
        return ['']

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

def getHorseHalfFraction(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseThreeQuarterFraction(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseStrVal(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getHorseFin(line):
    return re.findall(r'^(.*?)\s.', line.strip())

def getJockey(line):
    return re.findall(r'^(\w.*?)[0-9]', line.strip())

def getPurse(line):
    return re.findall(r'^(\d+.*?)[0-9]', line.strip())

def getOdds(line):
    return re.findall(r'(\d+\.?\d*)', line.strip())

horseObjs = []
#for horse in horses[1: len(horses)] :
header = []

for line in horses[0]:
    if line.strip() :
        if line.find(r"M\Eqt") :
            elements = line.split(' ')
            for element in elements :
                header.append(element.strip())
            continue
                
        header.append(line.strip())

print(header)
for horse in horses[1:]:
    b_horse = ' '.join(horse).replace('\n', ' ').replace('\r', ' ')
    h = RaceLine()
    print(b_horse)
    h.lastRaceDate = getLastRaceDate(b_horse)
    b_horse = b_horse[len(h.lastRaceDate[0]):].strip()
    h.lastRaceLoc = getLastRaceLoc(b_horse )
    b_horse = b_horse[len(h.lastRaceLoc[0]):].strip()
    h.horseName = getHorseName(b_horse)
    b_horse = b_horse[len(h.horseName[0]):]
    h.medications = getHorseMedications(b_horse)
    b_horse = b_horse[len(h.medications[0]):].strip()
    h.equipment = getHorseEquipment(b_horse)
    b_horse = b_horse[len(h.equipment[0]):].strip()
    h.aVal = getHorseAVal(b_horse)
    b_horse = b_horse[len(h.aVal[0]):].strip()
    h.weight = getHorseWeight(b_horse)
    b_horse = b_horse[len(h.weight[0]):].strip()
    h.pp = getHorsePP(b_horse)
    b_horse = b_horse[len(h.pp[0]):].strip()
    h.st = getHorseSt(b_horse)
    b_horse = b_horse[len(h.st[0]):].strip()
    h.quartFraction = getHorseQuarterFraction(b_horse)
    b_horse = b_horse[len(h.quartFraction[0]) :].strip()
    h.halfFraction = getHorseHalfFraction(b_horse)
    b_horse = b_horse[len(h.halfFraction[0]) :].strip()    
    h.threeQuarterFraction = getHorseThreeQuarterFraction(b_horse)
    b_horse = b_horse[len(h.threeQuarterFraction[0]):].strip()
    h.strVal = getHorseStrVal(b_horse)
    b_horse = b_horse[len(h.strVal[0]) :].strip()
    h.fin = getHorseFin(b_horse)
    b_horse = b_horse[len(h.fin[0]):].strip()
    h.jockey = getJockey(b_horse)
    b_horse = b_horse[len(h.jockey[0]):].strip()
    h.purse = getPurse(b_horse)
    b_horse = b_horse[len(h.purse[0]):].strip()
    h.odds = getOdds(b_horse)
    horseObjs.append(h)
    print(h)
    



#^(.*?)\s.
#^(.*?)\s+
#^(.*?)[M\L]