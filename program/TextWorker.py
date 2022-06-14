from FileWorker import ControlFile

class TextWorker:

    __count = 0
    __womanCount = 0
    __manCount = 0
    __twistCount = 0
    __raceCount = 0
    __locationCount = 0
    __frindlyCount = 0
    __loveCount = 0
    __familyCount = 0
    __enemyCount = 0

    def __init__(self, text):
        #init control words
        friendly = ControlFile("controlWords/friendly.bp").getControlWords()
        enemy = ControlFile("controlWords/enemy.bp").getControlWords()
        race = ControlFile("controlWords/race.bp").getControlWords()
        love = ControlFile("controlWords/love.bp").getControlWords()
        locations = ControlFile("controlWords/locations.bp").getControlWords()
        femaleNames = ControlFile("controlWords/femaleNames.bp").getControlWords()
        family = ControlFile("controlWords/family.bp").getControlWords()
        twist = ControlFile("controlWords/twist.bp").getControlWords()
        maleNames = ControlFile("controlWords/maleNames.bp").getControlWords()

        #analyze
        textArray = text.split(" ")
        self.__count = len(textArray)
        for word in textArray:
            l = len(word)
            if word in maleNames or (l>2 and word[:l-1] in maleNames) or (l>3 and word[:l-2] in maleNames):
                self.__manCount += 1
                continue
            if word in femaleNames or (l>2 and word[:l-1] in femaleNames) or (l>3 and word[:l-2] in femaleNames):
                self.__womanCount += 1
                continue
            word.lower
            if word in twist or (l>2 and word[:l-1] in twist) or (l and word[:l-2] in twist):
                self.__twistCount += 1
            if word in race or (l>2 and word[:l-1] in race) or (l>3 and word[:l-2] in race):
                self.__raceCount += 1
            if word in locations or (l>2 and word[:l-1] in locations) or (l>3 and word[:l-2] in locations):
                self.__locationCount += 1
            if word in friendly or (l>2 and word[:l-1] in friendly) or (l>3 and word[:l-2] in friendly):
                self.__frindlyCount += 1
                continue
            if word in love or (l > 2 and word[:l - 1] in love) or (l > 3 and word[:l - 2] in love):
                self.__loveCount += 1
                continue
            if word in family or (l>2 and word[:l-1] in family) or (l>3 and word[:l-2] in family):
                self.__familyCount += 1
                continue
            if word in enemy or (l>2 and word[:l-1] in enemy) or (l>3 and word[:l-2] in enemy):
                self.__enemyCount += 1

    def getData(self):
        print(self.__count)
        print(self.__womanCount)
        print(self.__manCount)
        print(self.__twistCount)
        print(self.__raceCount)
        print(self.__locationCount)
        print(self.__frindlyCount)
        print(self.__loveCount)
        print(self.__familyCount)
        print(self. __enemyCount)