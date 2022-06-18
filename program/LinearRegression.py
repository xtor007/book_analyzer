import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys

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

    yColumnIndex = 16

    percentageScore = 0

    def __init__(self, data):
        self.data = data
        print("--------------------------------------------")
        print("Linear regression starts")

    def start(self):
        self.findEquations()
        print(self.parametrs)

    def findEquations(self):
        matrix = []
        for equation in range(0, len(self.names)):
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

    def addTwoRows(self, row1, row2):
        resultRow = []
        if len(row1) == len(row2):
            for i in (range(0, len(row1))):
                resultRow.append(row1[i]+row2[i])
        return  resultRow
