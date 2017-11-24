from mysql import Database
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib import dates as mdates

class Plotter:

    def __init__(self, crypto_coin):
        db = Database()
        self.crypto_coin = crypto_coin
        self.data = db.getData(self.crypto_coin)


    def fill_arrays(self):
        array = self.data
        date_array = []
        open_price_array = []
        high_price_array = []

        for dictionary in array:
            date = dictionary['scrapeDate']
            date_object = datetime.strptime(date, '%Y-%m-%d')
            number_date = date_object.timestamp()
            open_price = dictionary['openPrice']
            high_price = dictionary['highPrice']
            low_price = dictionary['lowPrice']
            close_price = dictionary['closePrice']
            volume = dictionary['volume']
            marketCap = dictionary['marketCap']

            date_array.append(mdates.date2num(date_object))
            open_price_array.append(open_price)
            high_price_array.append(high_price)

        return date_array, open_price_array, high_price_array

    def plot_graph(self):
        print("fetching data")
        date_array, open_price_array, high_price_array = self.fill_arrays()
        date_array = sorted(date_array, reverse=True)

        fig, ax = plt.subplots()

        ax.grid(True) #set grid

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.suptitle(self.crypto_coin + ' price in Dollars')

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y')) #formateer de floatdate naar d-m-Y
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        plt.xticks(date_array, rotation=315) # verandert rotatie van de labels op de x-as

        ax.plot(date_array, open_price_array) #eerst x-as dan Y-as
        ax.plot(date_array, high_price_array)
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        plt.show()

#p = Plotter("bitcoin")
#p.plot_graph()