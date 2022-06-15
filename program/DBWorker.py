import pymysql
class DBWorker:
    __host = ""
    __user = ""
    __port = 3306
    __password = ""
    __db_name = ""

    def __init__ (self, host ="localhost", user ="root", port ="3306", password ="", db_name ="BooksMeasurement"):
        self.__host = host
        self.__user = user
        self.__port = int(port)
        self.__password = password
        self.__db_name = db_name

    def connect(self):
        try:
            connection = pymysql.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                database=self.__db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected!")
        except Exception as ex:
            print("Connection refused...")
            print(ex)