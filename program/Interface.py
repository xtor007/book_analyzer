from DBWorker import DBWorker
from FileWorker import MainFile, BookFile
from Book import Book
from DataWorker import DataWorker
from LogisticRegresion import LogisticRegresion


class Interface:

    def go(self):
        print("Program start")
        isValueInput = False
        db = DBWorker()
        data = DataWorker()
        while not isValueInput:
            inputValue = input("What do you want to do?\n 0 - upload data to database\n 1 - train the model \n 2 - predict for my book\n")
            if inputValue == "0":
                db.create_table()
                print("Uploading data...")
                fileWorker = MainFile('books.bp')
                for bookNameFile in fileWorker.getFilesNames():
                    bookFile = BookFile(bookNameFile)
                    book = Book(bookFile.getBookData())
                    data.updateData(book)
                    db.insert_params(
                        book.getName(),
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
                        book.analyzeResult['location_count'],
                        book.count,
                        book.isDark
                    )
                isValueInput = True
            elif inputValue == "1":
                loadedData = db.fetch_all_data()
                normalizedData = data.loadData(loadedData)
                logReg = LogisticRegresion(normalizedData)
                logReg.go()
                logReg.saveResult()
                isValueInput = True
            elif inputValue == "2":
                
                isValueInput = True
            else:
                print("error")
        data.saveMaxMinData()