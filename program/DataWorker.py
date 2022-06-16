import sys

class DataWorker:

    maxValues = [0]*17
    minValues = [sys.maxsize]*17

    def updateData(self, book):
        data = [
            book.year,
            book.pages,
            book.ratingLiveLib,
            book.ratingLitRes,
            book.isReal,
            book.analyzeResult['count'],
            book.analyzeResult['woman_count'],
            book.analyzeResult['man_count'],
            book.analyzeResult['twist_count'],
            book.analyzeResult['race_count'],
            book.analyzeResult['friends_count'],
            book.analyzeResult['lovers_count'],
            book.analyzeResult['families_count'],
            book.analyzeResult['enemies_count'],
            book.analyzeResult['location_count'],
            book.count,
            book.isDark
        ]
        for i in range(len(data)):
            if data[i] > self.maxValues[i]:
                self.maxValues[i] = data[i]
            if data[i] < self.minValues[i]:
                self.minValues[i] = data[i]

    def saveData(self):
        print(self.minValues)
        print(self.maxValues)