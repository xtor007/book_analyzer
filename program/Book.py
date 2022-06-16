from TextWorker import TextWorker

class Book:

    name = ""
    author = ""
    pages = 0
    year = 0
    ratingLiveLib = 0.0
    ratingLitRes = 0.0
    isReal = False
    count = 0
    isDark = False
    text = ""

    analyzeResult = None

    def __init__(self, data):
        self.name = data[0]
        print(f'Book {self.name} is on work')
        self.author = data[1]
        self.pages = int(data[2])
        self.year = int(data[3])
        self.ratingLiveLib = float(data[4])
        self.ratingLitRes = float(data[5])
        if data[6] == 0:
            self.isReal = False
        else:
            self.isReal = True
        self.count = int(data[7])
        if data[8] == 0:
            self.isDark = False
        else:
            self.isDark = True
        otherDataCount = len(data)-9
        for i in range(otherDataCount):
            self.text += data[i+9]
        self.__analyzeData()
        print(f'Book {self.name} is finished')

    def __analyzeData(self):
        text = TextWorker(self.text)
        self.analyzeResult = text.getData()

    def getName(self):
        newName = ""
        for char in self.name:
            if char == "'":
                newName += "\\"
            newName += char
        return newName