
def parseRaceLine(line):
    print(line)

def findUnicodeCharacter(line = "line", offset = "offset"):
    for char in line :
        #if ( ord(char) >= 48) and (ord(char) <= 57):
        #    pass
        #elif ( ord(char) >= 65) and (ord(char) <= 122) :
        #    pass
        #else :
        #print("Found weird unicode thing {} value {}".format(char, ord(char)))
        pass

def findLastRace(line):
    return line.split(' ', 1)

def iteratLines(lines):
    for line in lines:
        if line.strip():
            print("[{}] : {}".format(lines.index(line),line.strip()))
            print("Last Race {}".format(findLastRace(line)))
            findUnicodeCharacter(line)

def reorderHorseLines(lines):
    i = 0
    ret = {}
    for line in lines :
        if line.strip() :
            if line.count(' ') == 1 :
                ret[i] = ret[i] + " " + line.strip()
                i += 1
            else :
                if i in ret:
                    ret[i] = ret[i] + " " + line.strip()
                else:
                    ret[i] = line.strip()
    return ret

def findHorseBlock(lines):
    ret = [-1] * 2
    for line in lines :
        if line.find("Cl'g Pr Odds $1") > -1:
            #print ("Found Start Line")
            ret[0] = lines.index(line) + 1
        if line.find("OFF AT") > -1:
            #print ("Found End Line")
            ret[1] = lines.index(line)
    return ret

def initPdf(fileName):
    lines = tuple (open (fileName, "r"))
    lineNumbers = findHorseBlock(lines)
    horseBlock = lines[lineNumbers[0]  : lineNumbers[1]]
    #print(horseBlock)
    correctHorseLines = reorderHorseLines(horseBlock)
    for value in correctHorseLines.values() :
        parseRaceLine(value)

if __name__ == "__main__":
    initPdf("./race_charts/BEL2019061901.txt")
