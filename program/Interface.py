from DBWorker import DBWorker
from FileWorker import MainFile, BookFile
from Book import Book


class Interface:

    def go(self):
        print("Program start")
        isValueInput = False
        db = DBWorker()
        db.create_table()
        while not isValueInput:
            inputValue = input("What do you want to do? 0 - upload data to database\n")
            if inputValue == "0":
                print("Uploading data...")
                fileWorker = MainFile('books.bp')
                for bookNameFile in fileWorker.getFilesNames():
                    bookFile = BookFile(bookNameFile)
                    book = Book(bookFile.getBookData())
                    db.insert_params(
                        book.name,
                        book.year,
                        book.pages,
                        book.ratingLiveLib,
                        book.ratingLitRes,
                        book.isReal,
                        book.analyzeResult['count'],
                        book.analyzeResult['woman_count'],
                        book.analyzeResult['man_count'],
                        book.analyzeResult['twist_count'],
                        book.analyzeResult['race_count'],
                        book.analyzeResult['friends_count'],
                        book.analyzeResult['lovers_count'],
                        book.analyzeResult['families_count'],
                        book.analyzeResult['enemies_count'],
                        book.analyzeResult['location_count']
                    )
                isValueInput = True
            else:
                print("error")
