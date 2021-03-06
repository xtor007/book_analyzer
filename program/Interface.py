from DBWorker import DBWorker
from FileWorker import MainFile, BookFile
from Book import Book
from DataWorker import DataWorker
from LogisticRegresion import LogisticRegresion
from TestWorkerLogistic import TestWorkerLogistic
from DecisionTree import DecisionTree
from knn import NearestNeighbors
from LinearRegression import LinearRegression


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
                data.saveMaxMinData()
            elif inputValue == "1":
                loadedData = db.fetch_all_data()
                normalizedData = data.loadData(loadedData)
                linReg = LinearRegression(normalizedData)
                linReg.clearNotImportant()
                linReg.start()
                '''
                logReg = LogisticRegresion(normalizedData)
                logReg.go()
                logReg.saveResult()
                decisionTree = DecisionTree(normalizedData)
                decisionTree.saveData()
                '''
                isValueInput = True
            elif inputValue == "2":
                loadedData = db.fetch_all_data()
                normalizedData = data.loadData(loadedData)
                print("Uploading test data...")
                fileWorker = MainFile('test.bp')
                testData = []
                testNames = []
                testResults = []
                testDataForKnn = []
                for bookNameFile in fileWorker.getFilesNames():
                    bookFile = BookFile(bookNameFile)
                    book = Book(bookFile.getBookData())
                    testNames.append(book.name)
                    testResults.append(book.isDark)
                    testData.append([
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
                    ])
                    testDataForKnn.append([
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
                        book.isDark,
                        book.count
                    ])
                linReg = LinearRegression(normalizedData)
                linReg.getParameters()
                linReg.compare(normalizedData, linReg.evaluate(normalizedData))
                knn = NearestNeighbors(normalizedData)
                knn.start(testDataForKnn)
                logTest = TestWorkerLogistic(testData,testNames,testResults)
                logTest.goTesting()
                #logTest.printTree()
                isValueInput = True
            else:
                print("error")