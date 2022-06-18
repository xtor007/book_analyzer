from DecisionCell import  DecisionCell
import random

class DecisionTree:

    root = None
    data = []
    yColumnIndex = 15
    meaningfulParameters = [0, 1, 3, 4, 11, 12, 13]
    percentOfDark = 0.31

    def __init__(self, data):
        print("--------------------------------------------")
        print("Decision tree start")
        self.data = data
        self.overSamplingData()
        root = DecisionCell(self.data,0)

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