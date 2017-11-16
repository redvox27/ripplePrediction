import time
from datetime import datetime
import urllib.request
import requests
from bs4 import BeautifulSoup

class Scraper:

    data_list = []

    def __init__(self):
        self.currentTime = int(round(time.time()))
        self.pastTime = self.currentTime - 2592000
        self.url = "https://coinmarketcap.com/currencies/ripple/historical-data/?start=%d&end=%d" % (self.pastTime, self.currentTime)

    def get_url(self):
        return self.url

    def get_data_list(self):
        return self.data_list

    def spider(self):
        url = self.get_url()
        headers = {
            "User-Agent":
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
        }

        req = requests.get(url, headers)
        plain_text = req.text
        soup = BeautifulSoup(plain_text, "html.parser")

        tableTag = soup.find("div", attrs={"class": "table-responsive"})

        tableBody = tableTag.find("tbody")

        rows = tableBody.find_all("tr")
        for row in rows:
            column = row.find_all("td")
            columnList = [element.text for element in column]
            #print(columnList)
            self.data_list.append(columnList)

    def correctDate(self):
        for i in range(0, len(self.data_list)):
            singe_data_list = self.data_list[i]
            date = singe_data_list[0]
            date = date.replace(",", "")
            date = str((datetime.strptime(date, '%b %d %Y')))
            date = date[:10]
            #date = datetime.strptime(date, "%Y-%m-%d").strftime("%m-%d-%Y")
            singe_data_list[0] = str(date)
            singe_data_list[5] = singe_data_list[5].replace(",", "")
            singe_data_list[6] = singe_data_list[6].replace(",", "")
            print(singe_data_list)

    def get_data_array(self):
        self.spider()
        self.correctDate()
        return self.data_list
