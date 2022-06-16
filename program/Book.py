from TextWorker import TextWorker

class Book:

    name = ""
    author = ""
    pages = 0
    year = 0
    ratingLiveLib = 0.0
    ratingLitRes = 0.0
    isReal = 0
    count = 0
    isDark = 0
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
        self.isReal = int(data[6])
        self.count = int(data[7])
        self.isDark = int(data[8])
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