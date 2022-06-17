import numpy as np
import matplotlib.pyplot as plt
import random

class LogisticRegresion:

    data = None
    names = [
        "year","pages",
        "ratingLiveLib","ratingLitRes",
        "isRealistic",
        "characters","female","male",
        "twists","race",
        "friends","loves","family","enemy",
        "locations",
        "isDark",
        "countOfRate"
    ]

    yColumnIndex = 15
    meaningfulParameters = []

    percentOfDark = 0

    def __init__(self, data):
        self.data = data
        print("--------------------------------------------")
        print("Logistic regresion start")

    def go(self):
        self.checkData()
        self.overSamplingData()

    def checkData(self):
        print("Data checking start")
        # y - це колонка isDark (15), дослідимо параметри на значемість
        for i in range(len(self.names)-1):
            avarege = 0
            avarege0 = 0
            n0 = 0
            avarege1 = 0
            n1 = 0
            for example in self.data:
                avarege += example[i]
                if example[self.yColumnIndex] == 0:
                    avarege0 += example[i]
                    n0 += 1
                else:
                    avarege1 += example[i]
                    n1 += 1
            avarege /= len(self.data)
            if i == self.yColumnIndex:
                self.percentOfDark = avarege
            avarege0 /= n0
            avarege1 /= n1
            print(f'Avarage in column {self.names[i]} is {avarege}; \nLight fantazy - {avarege0}\nDark fantazy - {avarege1}')
        self.meaningfulParameters = [0,1,3,4,11,12,13]

    def overSamplingData(self):
        #вирівнюємо вибірку
        countOfNewData = 0
        neededNewCount = int(len(self.data)*(1-2*self.percentOfDark))
        for example in self.data:
            if example[self.yColumnIndex] == 1:
                newExample = example
                for paramIndex in self.meaningfulParameters:
                    newExample[paramIndex] *= random.uniform(0.85,1.15)
                self.data.append(newExample)
                countOfNewData += 1
                if countOfNewData >= neededNewCount:
                    break
        print(len(self.data))