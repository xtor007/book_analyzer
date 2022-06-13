from Book import Book

class FileWorker:

    __rootPath = "data/"
    fileData = ""

    def __init__ (self, fileName):
        file = open(self.__rootPath+fileName, 'r')
        self.fileData = file.read()

class MainFile(FileWorker):
    def getFilesNames(self):
        return self.fileData.splitlines()

class BookFile(FileWorker):
    def getBookData(self):
        return Book(self.fileData.splitlines())