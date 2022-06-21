import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
from FileWorker import ParamFile

class LinearRegression:

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

    importantParameters = [1, 2, 3, 4, 8, 13, 14, 16]

    yColumnIndex = 7

    coefficients = []

    percentageScore = 0

    def __init__(self, data):
        self.data = data
        print("--------------------------------------------")
        print("Linear regression starts")

    def start(self):
        matrix = self.findEquations()
        self.coefficients = self.solveMtxGauss(matrix, len(self.importantParameters))
        self.saveParametrs()

    def saveParametrs(self):
        file = ParamFile("solution/linRegParams.bp","w")
        j = 0
        resParams = []
        for i in range(len(self.names) - 2):
            if i in self.importantParameters:
                resParams.append(self.coefficients[j])
                j += 1
            else:
                resParams.append(0)
        resParams.append(self.coefficients[j])
        file.writeToFile(resParams)

    def getParameters(self):
        file = ParamFile("solution/linRegParams.bp")
        coefIn = file.getParams()
        for k in coefIn:
            if k != 0:
                self.coefficients.append(k)


    def getImportanceParam(self):
        parameters = []
        for i in range(len(self.names)):
            print(f'{i})', end=" ")
            self.evaluateImportance(i)

    def evaluateImportance(self, parameter):
        x = []
        y = []
        for i in range(len(self.data)):
            tX = self.data[i][parameter]
            tY = 0.4*tX + random.uniform(0, 0.35)
            # tY = self.data[i][self.yColumnIndex]
            x.append(tX)
            y.append(tY)
            print(f'({tX}; {tY})')
        plt.title(self.names[parameter])
        plt.scatter(x, y, marker="o", c="g")
        plt.show()

    def clearNotImportant(self):
        newData = []
        for i in range(len(self.data)):
            newExample = []
            for j in range(len(self.data)):
                if j in self.importantParameters:
                    newExample.append(self.data[i][j])
            newData.append(newExample)
        self.data = newData

    def checkMulticol(self):
        avaragesValues = [0] * len(self.importantParameters)
        for example in self.data:
            for i in range(len(self.importantParameters)):
                avaragesValues[i] += example[self.importantParameters[i]]
        newData = self.data
        for i in range(len(avaragesValues)):
            avaragesValues[i] /= len(self.data)
        for i in range(len(newData)):
            for j in range(len(self.importantParameters)):
                newData[i][self.importantParameters[j]] -= avaragesValues[j]
        corTable = [None] * len(avaragesValues)
        for i in range(len(corTable)):
            corTable[i] = [0] * len(avaragesValues)
            for j in range(len(corTable[0])):
                xy = 0
                xx = 0
                yy = 0
                for example in newData:
                    xy += example[self.importantParameters[i]] * example[self.importantParameters[j]]
                    xx += example[self.importantParameters[i]] ** 2
                    yy += example[self.importantParameters[j]] ** 2
                corTable[i][j] = xy / ((xx * yy) ** 0.5)
        print(f'CorTable is {corTable}')
        self.importantParameters = [0, 1, 3, 4, 11, 12]

    def findEquations(self):
        matrix = []
        for equation in range(0, len(self.importantParameters)):
            print(equation)
            row = []
            if equation != self.yColumnIndex:
                for argument in range(0, len(self.data[equation]) + 1):
                    parameter_sum = 0
                    for i in range(0, len(self.data)):
                        if argument < self.yColumnIndex:
                            parameter_sum += self.data[i][argument] * self.data[i][equation]
                        elif argument == self.yColumnIndex:
                            parameter_sum += self.data[i][equation]
                        else:
                            parameter_sum += self.data[i][self.yColumnIndex] * self.data[i][equation]
                    row.append(parameter_sum)
            else:
                for argument in range(0, len(self.data[equation]) + 1):
                    parameter_sum = 0
                    for i in range(0, len(self.data)):
                        if argument < self.yColumnIndex:
                            parameter_sum += self.data[i][argument]
                        elif argument == self.yColumnIndex:
                            parameter_sum += 1
                        else:
                            parameter_sum += self.data[i][self.yColumnIndex]
                    row.append(parameter_sum)
            print(f'Size: {len(row)}')
            print(row)
            matrix.append(row)
        return matrix


    def solveMtxGauss(self, mtx, unknowns):
        x = np.zeros(unknowns)
        print(mtx)
        print(f'rows: {len(mtx)}; cols: {len(mtx[1])}')
        for i in range(unknowns):
            if mtx[i][i] == 0.0:
                sys.exit('Divide by zero detected!')
            for j in range(i + 1, unknowns):
                ratio = mtx[j][i] / mtx[i][i]
                for k in range(unknowns + 1):
                    mtx[j][k] = mtx[j][k] - ratio * mtx[i][k]
        # Back Substitution
        x[unknowns - 1] = mtx[unknowns - 1][unknowns] / mtx[unknowns - 1][unknowns - 1]
        for i in range(unknowns - 2, -1, -1):
            x[i] = mtx[i][unknowns]
            for j in range(i + 1, unknowns):
                x[i] = x[i] - mtx[i][j] * x[j]
            x[i] = x[i] / mtx[i][i]
        # Displaying solution
        print('\nRequired solution is: ')
        for i in range(unknowns):
            print(f'X{i} = {x[i]}')
        return x

    def evaluate(self, selection):
        predictedSet = []
        if len(self.coefficients) > 0:
            for i in range(len(selection)):
                predictedY = 0
                print(f'Y =', end=" ")
                for paramNum in range(len(self.importantParameters)):
                    print(f'{selection[i][paramNum]} * {self.coefficients[paramNum]} ({paramNum}) +', end=" ")
                    predictedY += selection[i][paramNum] * self.coefficients[paramNum]
                predictedY += self.coefficients[len(self.coefficients) - 1]
                predictedSet.append(predictedY)
                print("")
        return predictedSet

    def compare(self, basedSet, predictedScore):
        if len(basedSet) == len(predictedScore):
            rozp = [0] * 21
            xInGisto = []
            xValInGisto = -1
            for _ in range(21):
                xInGisto.append(xValInGisto)
                xValInGisto += 0.1
            rss = 0
            tss = 0
            avarageY = 0
            for i in range(len(self.data)):
                avarageY += self.data[i][self.yColumnIndex]
            avarageY /= len(self.data)
            for i in range(len(basedSet)):
                convergence = 100 * (1 - math.fabs(basedSet[i][self.yColumnIndex] - predictedScore[i]))
                rozp[int((predictedScore[i] - self.data[i][self.yColumnIndex]) * 10) + 10] += 1
                print(f'Based set: {basedSet[i]}; Predicted score: {predictedScore[i]} | Convergence = {convergence}')
                rss += (self.data[i][self.yColumnIndex] - avarageY) ** 2
                tss += (self.data[i][self.yColumnIndex] - predictedScore[i]) ** 2
            plt.bar(xInGisto, rozp, 0.4)
            plt.show()
            print(f'RSS = {rss}, TSS = {tss}, R2 = {1 - rss / tss}')