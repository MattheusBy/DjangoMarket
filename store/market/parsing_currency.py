"""
This module gets the current exchange rate
"""

import requests
from bs4 import BeautifulSoup

# url for currency values
url_usd = "https://myfin.by/bank/kursy_valjut_nbrb/usd"
url_eur = "https://myfin.by/bank/kursy_valjut_nbrb/eur"

headers = {
     "Accept": "text/html,application/xhtml+xml,"
               "application/xml;q=0.9,image/avif,"
               "image/webp,*/*;q=0.8",
     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; "
                   "Linux x86_64; rv:95.0) "
                   "Gecko/20100101 Firefox/95.0"
}
# create request instance
req = requests.get(url_usd, headers=headers)
# src-variable store request data
src = req.text

# BS4 instance
soup = BeautifulSoup(src, "lxml")

dollar_search = soup.find("div", "cur-rate__value")

req = requests.get(url_eur, headers=headers)
src = req.text

euro_search = soup.find("div", "cur-rate__value")
# final value dollar and euro
dollar = dollar_search.text
euro = euro_search.text
