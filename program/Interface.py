class Interface:

    def go(self):
        print("Program start")
        isValueInput = False
        while not isValueInput:
            inputValue = input("What do you want to do? 0 - upload data to database\n")
            if inputValue == "0":
                print("upload data")
                isValueInput = True
            else:
                print("error")