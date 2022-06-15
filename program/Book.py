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
    text = ""

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
        count = int(data[7])
        otherDataCount = len(data)-8
        for i in range(otherDataCount):
            self.text += data[i+8]
        self.__analyzeData()
        print(f'Book {self.name} is finished')

    def __analyzeData(self):
        text = TextWorker(self.text)
        text.getData()