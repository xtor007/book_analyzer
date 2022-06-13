class Book:

    name = ""
    author = ""
    pages = 0
    year = 0
    rating = 0.0
    count = 0
    text = ""

    def __init__(self, data):
        name = data[0]
        author = data[1]
        pages = int(data[2])
        year = int(data[3])
        rating = float(data[4])
        count = int(data[5])
        otherDataCount = len(data)-6
        for i in range(otherDataCount):
            self.text += data[i+6]
        self.__analyzeData()

    def __analyzeData(self):
        print(self.text)