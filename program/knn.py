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

    yColumnIndex = 16

    k = 5

    percentageScore = 0

    def __init__(self, data):
        self.data = data
        print("--------------------------------------------")
        print("K-Nearest Neighbors starts")

    def start(self, selection):
        print(selection)
        evaluations = []
        for pack in selection:
            print(f'Pack: {pack}')
            evaluations.append(self.findNeighbors(pack))
        for i in range(len(evaluations)):
            print(f'For {selection[i]} is predicted rate up to {evaluations[i]} | Convergence = {100 * (1 - math.fabs(selection[i][self.yColumnIndex] - evaluations[i]))}')

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
