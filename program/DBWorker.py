import pymysql


class DBWorker:
    __host = ""
    __user = ""
    __port = 3306
    __password = ""
    __db_name = ""
    __connection = None

    def __init__(self, host="localhost", user="root", port="3306", password="password", db_name="BooksMeasurement"):
        self.__host = host
        self.__user = user
        self.__port = int(port)
        self.__password = password
        self.__db_name = db_name

    def connect(self):
        try:
            self.__connection = pymysql.connect(
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

    def create_table(self):
        self.connect()
        try:
            with self.__connection.cursor() as cursor:
                drop_script = "DROP TABLE IF EXISTS Parameters;"
                create_script = "CREATE TABLE Parameters (   `id` DOUBLE NOT NULL AUTO_INCREMENT,   " \
                                "`name` VARCHAR(150) NOT NULL,   `year` DOUBLE NOT NULL,   `pages` DOUBLE NOT NULL,   " \
                                "`ratingLiveLib` DOUBLE NOT NULL, `ratingLitRes` DOUBLE NOT NULL,   `isRealistic` TINYINT NOT NULL,   `charactersNumber` " \
                                "DOUBLE NOT NULL,   `femaleNumber` DOUBLE NOT NULL,   `maleNumber` DOUBLE NOT NULL,   " \
                                "`plotTwists` DOUBLE NOT NULL,   `raceNumber` DOUBLE NOT NULL,   `friendsNumber` " \
                                "DOUBLE " \
                                "NOT NULL,   `lovesNumber` DOUBLE NOT NULL,   `relativesNumber` DOUBLE NOT NULL,   " \
                                "`enemiesNumber` DOUBLE NOT NULL,   `locationsNumber` DOUBLE NOT NULL,   PRIMARY KEY (" \
                                "`id`)) "
                cursor.execute(drop_script)
                cursor.execute(create_script)

        finally:
            self.__connection.close()

    def insert_params(self, name, year, pages, ratingLiveLib, ratingLitRes, is_realistic, characters_number, female_number, male_number,
                      plot_twists, race_number, friends_number, loves_number, relatives_number, enemies_number,
                      locations_number):
        self.connect()
        try:
            with self.__connection.cursor() as cursor:
                insert_script = "INSERT INTO `Parameters`(`name`, `year`, `pages`, `ratingLiveLib`, `ratingLitRes`, `isRealistic`, `charactersNumber`, " \
                                "`femaleNumber`, `maleNumber`, `plotTwists`, `raceNumber`, `friendsNumber`, `lovesNumber`, " \
                                "`relativesNumber`, `enemiesNumber`, `locationsNumber`) VALUES(" + "'{}', {}, {}, {}, {}, {}, " \
                                                                                             "{}, {}, {}, {}, {}, {}," \
                                                                                             " {}, {}, {}, {});".format(
                    name, year, pages, ratingLiveLib, ratingLitRes, is_realistic, characters_number, female_number, male_number,
                    plot_twists, race_number, friends_number, loves_number, relatives_number, enemies_number,
                    locations_number)
                cursor.execute(insert_script)
                self.__connection.commit()
        finally:
            self.__connection.close()

    def fetch_all_data(self):
        self.connect()
        try:
            with self.__connection.cursor() as cursor:
                select_script = "SELECT * FROM Parameters;"
                cursor.execute(select_script)
                rows = cursor.fetchall()
                return rows
        finally:
            self.__connection.close()
