from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data, "html.parser")

print(soup)

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all("tbody")[2].find_all("tr"):
    col = row.find_all("td")
    if col:
        name = col[1].text
        market_cap = float(col[2].text)

data = data.append(
    {"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True
)

print(data)

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=ENTER_YOUR_KEY_HERE"
reponse = requests.get(url)
