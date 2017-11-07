import time
import urllib.request
import requests
from bs4 import BeautifulSoup

class Scraper:

    dataList = []

    def __init__(self):
        self.currentTime = int(round(time.time()))
        self.pastTime = self.currentTime - 2592000
        self.url = "https://coinmarketcap.com/currencies/ripple/historical-data/?start=%d&end=%d" % (self.pastTime, self.currentTime)

    def get_url(self):
        return self.url

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
            print(columnList)
            self.dataList.append(columnList)


s = Scraper()
s.spider()