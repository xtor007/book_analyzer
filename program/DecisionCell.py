class DecisionCell:

    meaningfulParameters = [0, 1, 3, 4, 11, 12, 13]
    yColumnIndex = 15

    parametrIndex = 0
    avarageParam = 0
    values = []
    leftCell = None
    rightCell = None
    isLast = False
    prediction = None

    def __init__(self,data,index):
        if index == None or len(data) == 1:
            self.isLast = True
            avarage = 0
            for example in data:
                avarage += example[self.yColumnIndex]
            if avarage>0.5:
                self.prediction = 1
            else:
                self.prediction = 0
        else:
            self.parametrIndex = index
            avarage = 0
            for example in data:
                avarage += example[index]
            avarage /= len(data)
            self.avarageParam = avarage
            rightData = []
            leftData = []
            for example in data:
                if example[index] > avarage:
                    rightData.append(example)
                else:
                    leftData.append(example)
            if len(leftData) == 0:
                leftData = rightData
            if len(rightData) == 0:
                rightData = leftData
            indexInParams = self.meaningfulParameters.index(index)
            newIndex = None
            if indexInParams < len(self.meaningfulParameters)-1:
                newIndex = self.meaningfulParameters[indexInParams+1]
            self.leftCell = DecisionCell(leftData,newIndex)
            self.rightCell = DecisionCell(rightData,newIndex)