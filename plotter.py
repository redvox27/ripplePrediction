from mysql import Database
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib import dates as mdates
class Plotter:

    def __init__(self):
        db = Database()
        self.data = db.getData()


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

            date_array.append(number_date)
            open_price_array.append(open_price)
            high_price_array.append(high_price)

        return date_array, open_price_array, high_price_array

    def plot_graph(self):
        date_array, open_price_array, high_price_array = self.fill_arrays()

        plt.plot(date_array, open_price_array) #eerst x-as dan Y-as
        plt.plot(date_array, high_price_array)
        plt.show()

p = Plotter()
p.fill_arrays()
p.plot_graph()