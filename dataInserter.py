from scraper import Scraper
from mysql import Database

class MainClass:

    def __init__(self):
        self.scraper = Scraper()
        self.db = Database()

    def insert_data_into_database(self):
        collected_data = self.scraper.get_data_array()

        for i in range(0, len(collected_data)):
            data_segment = collected_data[i]

            date = data_segment[0]
            open_price = data_segment[1]
            high_price = data_segment[2]
            low_price = data_segment[3]
            close_price = data_segment[4]
            volume = data_segment[5]
            market_cap = data_segment[6]

            if not self.db.check_if_entry_exists(date):
               self.db.insert_data(date, open_price, high_price, low_price, close_price, volume, market_cap)

