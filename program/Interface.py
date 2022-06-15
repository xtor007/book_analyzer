from DBWorker import  DBWorker
from FileWorker import MainFile, BookFile
from Book import Book

class Interface:

    def go(self):
        print("Program start")
        isValueInput = False
        db = DBWorker()
        db.connect()
        while not isValueInput:
            inputValue = input("What do you want to do? 0 - upload data to database\n")
            if inputValue == "0":
                print("Uploading data...")
                fileWorker = MainFile('books.bp')
                for bookNameFile in  fileWorker.getFilesNames():
                    bookFile = BookFile(bookNameFile)
                    book = Book(bookFile.getBookData())
                isValueInput = True
            else:
                print("error")