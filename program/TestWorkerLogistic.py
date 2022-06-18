from FileWorker import MaxMinFile, ParamFile, CellFile
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
        #self.testLogisticReg()
        self.testTree()

    def testTree(self):
        resultNames = ["Light", "Dark"]
        print("----------------------------------")
        print("Start testing tree")
        rightAnswers = 0
        path = "solution/tree/"
        for i in range(len(self.data)):
            fileName = "root"
            predict = 0
            while True:
                file = CellFile(path+fileName+".bp")
                if fileName == "root":
                    fileName = ""
                cellData = file.getCellValues()
                if cellData[0] == "1":
                    predict = int(cellData[1])
                    break
                parametr = int(cellData[1])
                value = float(cellData[2])
                if self.data[i][parametr] > value:
                    fileName += "r"
                else:
                    fileName += "l"
            print(f'{self.names[i]} is {resultNames[self.results[i]]}; Prediction is {resultNames[predict]}')
            if self.results[i] == predict:
                rightAnswers += 1
        print(f'Correctness of predictions - {rightAnswers / len(self.data)}')

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