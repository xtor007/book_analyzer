class FileWorker:

    __rootPath = "data/"
    fileData = ""
    file = None

    def __init__ (self, fileName, format = 'r'):
        self.file = open(self.__rootPath+fileName, format)
        if format == 'r':
            self.fileData = self.file.read()

class MainFile(FileWorker):
    def getFilesNames(self):
        return self.fileData.splitlines()

class BookFile(FileWorker):
    def getBookData(self):
        return self.fileData.splitlines()

class ControlFile(FileWorker):
    def getControlWords(self):
        return self.fileData.splitlines()

class MaxMinFile(FileWorker):

    def writeToFile(self, arr):
        for i in arr:
            self.file.write(f'{i} ')
        self.file.write("\n")

    def getMaxArray(self):
        result = []
        for i in self.fileData.splitlines()[0].split(" "):
            if i != '':
                result.append(float(i))
        return result

    def getMinArray(self):
        result = []
        for i in self.fileData.splitlines()[1].split(" "):
            if i != '':
                result.append(float(i))
        return result

class ParamFile(FileWorker):

    def writeToFile(self, param):
        for p in param:
            self.file.write(f'{p} ')

    def getParams(self):
        result = []
        for param in self.fileData.split(" "):
            result.append(float(param))
        return result