from mysql import Database
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib import dates as mdates
from matplotlib.finance import candlestick2_ohlc
from forex_python.converter import CurrencyRates
from decimal import *
class Plotter:

    def __init__(self, crypto_coin):
        db = Database()
        self.crypto_coin = crypto_coin
        self.data = db.getData(self.crypto_coin)
        self.rates = CurrencyRates()
        self.exchange_rate = self.get_exchange_rate()

    def fill_arrays(self):
        array = self.data
        date_array = []
        open_price_array = []
        high_price_array = []
        low_price_array = []
        close_price_array =[]

        for dictionary in array:
            date = dictionary['scrapeDate']
            date_object = datetime.strptime(date, '%Y-%m-%d')
            number_date = date_object.timestamp()
            open_price = float(dictionary['openPrice'])
            high_price = float(dictionary['highPrice'])
            low_price = float(dictionary['lowPrice'])
            close_price = float(dictionary['closePrice'])
            volume = dictionary['volume']
            marketCap = dictionary['marketCap']

            date_array.append(mdates.date2num(date_object))
            open_price_array.append(open_price * self.exchange_rate)
            high_price_array.append(high_price * self.exchange_rate)
            low_price_array.append(low_price *self.exchange_rate)
            close_price_array.append(close_price * self.exchange_rate)

        return date_array, open_price_array, high_price_array, low_price_array, close_price_array

    def plot_graph(self):
        print("fetching data")
        date_array, open_price_array, high_price_array, low_price_array, close_price_array = self.fill_arrays()

        fig, ax = plt.subplots()

        ax.grid(True) #set grid

        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.suptitle(self.crypto_coin + ' price in Euro' + "'" + "s")

        #ax.plot(date_array, open_price_array) #eerst x-as dan Y-as
        #ax.plot(date_array, high_price_array)

        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # formateer de floatdate naar d-m-Y
        ax.xaxis.set_major_locator(mdates.DayLocator())

        candlestick2_ohlc(ax, open_price_array, high_price_array,low_price_array, close_price_array, width=0.75)
        #ax.plot(date_array, open_price_array) #eerst x-as dan Y-as

        ax.xaxis_date()
        #plt.xticks(date_array, rotation=315)  # verandert rotatie van de labels op de x-as
        ax.autoscale_view()

        plt.show()

    def get_exchange_rate(self):
        rates = self.rates.get_rates('USD')
        return float(rates['EUR'])
