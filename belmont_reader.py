import camelot
import io
import numpy as np
import pprint
import re 
import unicode_dates
import datetime

class RaceLine:
    lastRaceDate = ""
    lastRaceLoc = ""
    date = datetime.date(1,1,1)
    horseName = ""
    medications = ""
    equipment = ""
    aVal = ""
    weight = ""
    pp = ""
    st = ""
    quartFraction = "" #needs work
    threeEights = "" #needs work
    strVal = "" #needs work
    fin = "" #needs work
    jockey = ""
    purse = ""
    odds = ""
  
    def norm(self):
        x = re.findall(r'(\d{1,})(.)(\d{1,})', self.lastRaceDate[0].strip())
        month = unicode_dates.unicodeMonthToNumber(x[0][1])
        self.date = datetime.date(int(x[0][2]) + 2000, int(month), int(x[0][0]))
        x = re.findall(r'(\w+)', self.lastRaceLoc[0].strip())
        self.lastRaceLoc = x[0].strip()
        self.horseName = self.horseName[0].strip()
        self.medications = self.medications[0].strip()
        self.aVal = self.aVal[0].strip()
        self.weight = self.weight[0].strip()
        self.pp = self.pp[0].strip()
        self.st = self.st[0].strip()
        self.jockey = self.jockey[0].strip()
        self.purse = self.purse[0].strip()
        self.odds = self.odds[0].strip()
        self.quartFraction = self.quartFraction[0].strip()
        self.threeEights = self.threeEights[0].strip()
        self.fin = self.fin[0].strip()
        self.equipment = self.equipment[0].strip()
        self.strVal = self.strVal[0].strip()

    def __str__(self):
        return "[lastRaceDate:"    + str(self.date.strftime("%m/%d/%Y")) + \
                ", lastRaceLoc:"   + self.lastRaceLoc + \
                ", horseName:"     + self.horseName + \
                ", equipment:"     + self.equipment + \
                ", medications:"   + self.medications + \
                ", A:"             + self.aVal + \
                ", weight:"        + self.weight + \
                ", pp:"            + self.pp + \
                ", st:"            + self.st + \
                ", quartFraction:" + self.quartFraction + \
                ", threeEights:"   + self.threeEights + \
                ", strVal:"        + self.strVal + \
                ", fin:"           + self.fin + \
                ", jockey:"        + self.jockey + \
                ", purse:"         + self.purse + \
                ", odds:"          + self.odds + \
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

def getHorseThreeEightsFraction(line):
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
for horse in horses[4:5]:
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
    h.threeEights = getHorseThreeEightsFraction(b_horse)
    b_horse = b_horse[len(h.threeEights[0]):].strip()
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
    h.norm()
    print(h)
    
    



#^(.*?)\s.
#^(.*?)\s+
#^(.*?)[M\L]