import pymysql
class Database:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Vtl54711', db='mydb')
        self.cursor = self.db.cursor()

    def insert_data(self, date, open_price, high_price, low_price, close_price, volume, market_cap, crypto_coin):
        query = "INSERT INTO " + crypto_coin +" (scrapeDate, openPrice, highPrice, lowPrice, closePrice, volume, marketCap)"\
                "VALUES(%s, %s, %s, %s, %s, %s, %s)"

        self.cursor.execute(query, (date, open_price, high_price, low_price, close_price, volume, market_cap))

        self.db.commit()

    def getData(self, crypto_coin):

        dictCursor = self.db.cursor(pymysql.cursors.DictCursor)
        query = "SELECT * FROM " + crypto_coin + " ORDER BY scrapeDate"
        dictCursor.execute(query)
        data = dictCursor.fetchall()
        return data

    def check_if_entry_exists(self, date, crypto_coin):
        query = "SELECT * FROM " + crypto_coin + " where scrapeDate = %s"


        result = self.cursor.execute(query, date)
        if result > 0:
            return True
        else:
            return False

