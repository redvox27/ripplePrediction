from scraper import Scraper
from tkinter import *
from plotter import Plotter
import time
from dataInserter import DataInserter

class GraphicalInterface:

    def __init__(self):
        self.height = 80
        self.width = 150

        self.root = Tk()
        self.root.title('crypto_coin_plotter')

        self.main_frame = Frame(self.root, width=self.width, height=self.width)
        self.main_frame.grid_propagate(False)
        self.main_frame.pack()

        self.checkbox_frame = Frame(self.main_frame, width=1280, height=800)
        self.checkbox_frame.grid(row=0, column=0)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=0, column=1)

        #checkbuttons
        self.ripple_var = IntVar()
        self.bitcoin_var = IntVar()
        self.ripple_check_button = Checkbutton(self.checkbox_frame, text="Ripple", variable=self.ripple_var)
        self.ripple_check_button.grid(row=0, column =0)
        self.bitcoin_check_button = Checkbutton(self.checkbox_frame, text="Bitcoin", variable=self.bitcoin_var)
        self.bitcoin_check_button.grid(row=1, column=0)

        #submitbuttons
        self.plot_button = Button(self.button_frame, text="Plot", command=self.plot)
        self.plot_button.grid(row=0, column=0)
        self.extract_info_button = Button(self.button_frame, text='Extract Data', command=self.insert_into_database)
        self.extract_info_button.grid(row=1, column=0)

        self.ws = self.root.winfo_screenwidth()  # width of the screen
        self.hs = self.root.winfo_screenheight()  # height of the screen

        self.x = (self.ws / 2) - (self.width / 2)
        self.y = (self.hs / 2) - (self.width / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))

        self.root.mainloop()

    def get_ripple_checkbox_value(self):
        return self.ripple_var.get()

    def get_bitcoin_checkbox_value(self):
        return self.bitcoin_var.get()

    def plot(self):

        try:
            self.root.after(100, self.root.destroy())
            if self.get_ripple_checkbox_value() == 1:
                plotter = Plotter("ripple")
                plotter.plot_graph()
            elif self.get_bitcoin_checkbox_value() == 1:
                plotter = Plotter("bitcoin")
                plotter.plot_graph()

        except Exception as e:
            print(e)

    def insert_into_database(self):
        try:
            self.root.after(100, self.root.destroy())

            if self.get_ripple_checkbox_value() == 1:
                data_inserter = DataInserter('ripple')
                data_inserter.insert_data_into_database()

            elif self.get_bitcoin_checkbox_value() ==1:
                data_inserter = DataInserter('bitcoin')
                data_inserter.insert_data_into_database()

        except Exception as e:
            print(e)