from FileWorker import MaxMinFile, ParamFile
import math

class TestWorkerLogistic:

    data = []
    names = []
    results = []

    def __init__(self, data, names, results):
        self.data = data
        self.names = names
        self.results = results
        maxMinFile = MaxMinFile("solution/MaxMin.bp")
        maxValues = maxMinFile.getMaxArray()
        minValues = maxMinFile.getMinArray()
        print(maxValues)
        print(minValues)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                data[i][j] = (data[i][j] - minValues[j])/(maxValues[j] - minValues[j])

    def goTesting(self):
        self.testLogisticReg()

    def testLogisticReg(self):
        resultNames = ["Light", "Dark"]
        print("----------------------------------")
        print("Start testing logistic regresion")
        paramFile = ParamFile("solution/LogResParams.bp")
        parametrs = paramFile.getParams()
        rightAnswers = 0
        for i in range(len(self.data)):
            prediction = self.expon(parametrs,self.data[i])
            print(f'{self.names[i]} is {resultNames[self.results[i]]}; Prediction is {resultNames[prediction]}')
            if self.results[i] == prediction:
                rightAnswers += 1
        print(f'Correctness of predictions - {rightAnswers/len(self.data)}')

    def expon(self, parametrs, example):
        z = 0
        for i in range(len(parametrs)):
            if i == len(parametrs) - 1:
                z += parametrs[i]
            else:
                z += parametrs[i] * example[i]
        if (1 / (1 + (math.e ** (-z)))) > 0.5 :
            return 1
        else:
            return 0