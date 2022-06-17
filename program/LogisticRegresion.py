import numpy as np
import matplotlib.pyplot as plt
import random
import math

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

    alpha = 0.005
    parametrs = []
    oldParametrs = []

    percentOfDark = 0

    isFinish = False

    def __init__(self, data):
        self.data = data
        print("--------------------------------------------")
        print("Logistic regresion start")

    def go(self):
        self.checkData()
        self.overSamplingData()
        self.parametrs = [1]*(len(self.meaningfulParameters)+1)
        self.trainData()
        print(self.parametrs)

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
        print("Data is ready to analyze")

    def costFunction(self):
        result = 0
        for example in self.data:
            p = self.expon(example)
            if p == 0 or p == 1:
                self.isFinish = True
            else:
                result += example[self.yColumnIndex]*math.log(p)
                result += (1-example[self.yColumnIndex])*math.log(1-p)
        return -result/len(self.data)

    def expon(self, example):
        z = 0
        for i in range(len(self.oldParametrs)):
            if i == len(self.oldParametrs) - 1:
                z += self.oldParametrs[i]
            else:
                z += self.oldParametrs[i] * example[self.meaningfulParameters[i]]
        return(1 / (1 + (math.e ** (-z))))

    def trainData(self):
        print("Training is start")
        self.isFinish = False
        count = 0
        self.oldParametrs = self.parametrs
        prevValue = self.costFunction()
        while not self.isFinish:
            self.oldParametrs = self.parametrs
            if count % 100 == 0:
                print(count)
                print(self.parametrs)
            count += 1
            for j in range(len(self.parametrs)):
                sum = 0
                for i in range(len(self.data)):
                    subsum = self.expon(self.data[j])-self.data[i][self.yColumnIndex]
                    mn = 1
                    if j != len(self.parametrs)-1:
                        mn = self.data[i][self.meaningfulParameters[j]]
                    sum += subsum*mn
                sum /= len(self.data)
                self.parametrs[j] -= sum*self.alpha
            nowValue = self.costFunction()
            if abs(nowValue-prevValue) < 0.00001:
                self.isFinish = True