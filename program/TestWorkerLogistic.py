from FileWorker import MaxMinFile, ParamFile, CellFile
import math
import matplotlib.pyplot as plt

class TestWorkerLogistic:

    data = []
    names = []
    results = []

    x = []
    y = []

    paramNames = [
        "year", "pages",
        "ratingLiveLib", "ratingLitRes",
        "isRealistic",
        "characters", "female", "male",
        "twists", "race",
        "friends", "loves", "family", "enemy",
        "locations",
        "isDark",
        "countOfRate"
    ]

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

    def printCell(self, fileName):
        path = "solution/tree/"
        file = CellFile(path + fileName + ".bp")
        cellData = file.getCellValues()
        if cellData[0] == "1":
            print(f'res - {cellData[1]}')
            return
        if fileName == "root":
            self.printCell("l")
        else:
            self.printCell(fileName+"l")
        parametr = int(cellData[1])
        value = float(cellData[2])
        print(f'{self.paramNames[parametr]} - {value}')
        if fileName == "root":
            self.printCell("r")
        else:
            self.printCell(fileName+"r")

    def printTree(self):
        self.printCell("root")

    def goTesting(self):
        self.testLogisticReg()
        plt.scatter(self.x, self.y)
        #plt.scatter(self.x, self.results)
        plt.show()
        self.testTree()

    def testTree(self):
        resultNames = ["Light", "Dark"]
        print("----------------------------------")
        print("Start testing tree")
        rss = 0
        tss = 0
        avarageY = 0
        for i in range(len(self.data)):
            avarageY += self.results[i]
        avarageY /= len(self.data)
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
            rss += (self.results[i] - avarageY) ** 2
            tss += (self.results[i] - predict) ** 2
            if self.results[i] == predict:
                rightAnswers += 1
        print(f'Correctness of predictions - {rightAnswers / len(self.data)}')
        print(f'RSS = {rss}, TSS = {tss}, R2 = {1 - rss / tss}')

    def testLogisticReg(self):
        rozp = [0]*21
        xInGisto = []
        xValInGisto = -1
        for _ in range(21):
            xInGisto.append(xValInGisto)
            xValInGisto += 0.1
        rss = 0
        tss = 0
        avarageY = 0
        for i in range(len(self.data)):
            avarageY += self.results[i]
        avarageY /= len(self.data)
        resultNames = ["Light", "Dark"]
        print("----------------------------------")
        print("Start testing logistic regresion")
        paramFile = ParamFile("solution/LogResParams.bp")
        parametrs = paramFile.getParams()
        rightAnswers = 0
        for i in range(len(self.data)):
            predictionVal = self.expon(parametrs,self.data[i])
            rozp[int((predictionVal-self.results[i])*10) + 10] += 1
            if predictionVal>0.5:
                prediction = 1
            else:
                prediction = 0
            print(f'{self.names[i]} is {resultNames[self.results[i]]}; Prediction is {resultNames[prediction]}')
            rss += (self.results[i] - avarageY) ** 2
            tss += (self.results[i] - predictionVal) ** 2
            if self.results[i] == prediction:
                rightAnswers += 1
        plt.bar(xInGisto,rozp,0.4)
        plt.show()
        print(f'Correctness of predictions - {rightAnswers/len(self.data)}')
        print (f'RSS = {rss}, TSS = {tss}, R2 = {1 - rss/tss}')

    def expon(self, parametrs, example):
        z = 0
        for i in range(len(parametrs)):
            if i == len(parametrs) - 1:
                z += parametrs[i]
            else:
                z += parametrs[i] * example[i]
        self.x.append(z)
        self.y.append((1 / (1 + (math.e ** (-z)))))
        return (1 / (1 + (math.e ** (-z))))