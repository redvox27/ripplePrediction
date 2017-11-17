import pymysql
class Database:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Vtl54711', db='mydb')
        self.cursor = self.db.cursor()

    def insert_data(self, date, open_price, high_price, low_price, close_price, volume, market_cap):
        query = "INSERT INTO mydb.ripple (scrapeDate, openPrice, highPrice, lowPrice, closePrice, volume, marketCap)"\
                "VALUES(%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (date, open_price, high_price, low_price, close_price, volume, market_cap))

        self.db.commit()

    def getData(self):
        dictCursor = self.db.cursor(pymysql.cursors.DictCursor)
        query = "SELECT * FROM mydb.ripple"
        dictCursor.execute(query)
        data = dictCursor.fetchall()
        print(data)
        return data

    def check_if_entry_exists(self, date):
        query = "SELECT * FROM mydb.ripple where scrapeDate = %s"


        result = self.cursor.execute(query, date)
        if result > 0:
            return True
        else:
            return False

