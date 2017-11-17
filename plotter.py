from mysql import Database
import datetime
import numpy as np
from matplotlib import pyplot
from matplotlib import ticker
from matplotlib import dates
class Plotter:

    def __init__(self):
        db = Database()
        self.data = db.getData()


    def graphData(self):
        array = self.data
        for dictionary in array:
            date = dictionary['scrapeDate']
            open_price = dictionary['openPrice']
            high_price = dictionary['highPrice']
            low_price = dictionary['lowPrice']
            close_price = dictionary['closePrice']
            volume = dictionary['volume']
            marketCap = dictionary['marketCap']


p = Plotter()
p.graphData()