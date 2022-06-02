import requests
from bs4 import BeautifulSoup

url = "https://myfin.by/currency/minsk"

headers = {
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
req = requests.get(url, headers=headers)
src = req.text
with open("parsed_currency.html", "w") as file:
    file.write(src)

with open("parsed_currency.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

dollar_search = soup.find("span", "bl_usd_ex")
euro_search = soup.find("span", "bl_eur_ex")
dollar = dollar_search.text
euro = euro_search.text
