import sys
from FileWorker import MaxMinFile

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
            book.isDark,
            book.count
        ]
        for i in range(len(data)):
            if data[i] > self.maxValues[i]:
                self.maxValues[i] = data[i]
            if data[i] < self.minValues[i]:
                self.minValues[i] = data[i]

    def loadData(self, dbData):
        result = []
        file = MaxMinFile("solution/MaxMin.bp")
        self.maxValues = file.getMaxArray()
        self.minValues = file.getMinArray()
        for data in dbData:
            array = [
                data['year'],
                data['pages'],
                data['ratingLiveLib'],
                data['ratingLitRes'],
                data['isRealistic'],
                data['charactersNumber'],
                data['femaleNumber'],
                data['maleNumber'],
                data['plotTwists'],
                data['raceNumber'],
                data['friendsNumber'],
                data['lovesNumber'],
                data['relativesNumber'],
                data['enemiesNumber'],
                data['locationsNumber'],
                data['isDark'],
                data['countOfRate']
            ]
            subResult = []
            for i in range(len(array)):
                subResult.append((array[i] - self.minValues[i])/(self.maxValues[i] - self.minValues[i]))
            result.append(subResult)
        return result

    def saveMaxMinData(self):
        file = MaxMinFile("solution/MaxMin.bp","w")
        file.writeToFile(self.maxValues)
        file.writeToFile(self.minValues)

