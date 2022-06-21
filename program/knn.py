import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys


class NearestNeighbors:
    data = None
    names = [
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

    importantParameters = [1, 2, 3, 4, 8, 13, 14, 16]

    yColumnIndex = 7

    k = 5

    percentageScore = 0

    def __init__(self, data):
        self.data = data
        self.clearNotImportant()
        print("--------------------------------------------")
        print("K-Nearest Neighbors starts")

    def start(self, selection):
        print(selection)
        evaluations = []
        for pack in selection:
            print(f'Pack: {pack}')
            evaluations.append(self.findNeighbors(pack))
        for i in range(len(evaluations)):
            print(f'Real Y: {selection[i][self.yColumnIndex]} | Theoretical Y: {evaluations[i]} | Convergence = {100 * (1 - math.fabs(selection[i][self.yColumnIndex] - evaluations[i]))}')

    def clearNotImportant(self):
        newData = []
        for i in range(len(self.data)):
            newExample = []
            for j in range(len(self.data)):
                if j in self.importantParameters:
                    newExample.append(self.data[i][j])
            newData.append(newExample)
        self.data = newData

    def findNeighbors(self, pack):
        distances = []
        for example in self.data:
            euclideaDistance = 0
            for parameter in range(len(example)):
                euclideaDistance += (pack[parameter] - example[parameter]) ** 2
            distances.append(math.sqrt(euclideaDistance))
        distances = self.bubbleSort(distances)
        print(distances)
        return self.evaluate()

    def evaluate(self):
        average = 0
        for i in range(self.k):
            average += self.data[i][self.yColumnIndex] / self.k
        return average

    def bubbleSort(self, array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    tempDist = array[j]
                    tempExmp = self.data[j]
                    array[j] = array[j + 1]
                    array[j + 1] = tempDist
                    self.data[j] = self.data[j + 1]
                    self.data[j + 1] = tempExmp
        return array
