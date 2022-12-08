from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Collect data
url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data = requests.get(url).text

# Parse data
soup = BeautifulSoup(html_data, "html.parser")

# Put it in a empty dataframe
data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

# Loop through soup and add to data frame
for row in soup.find_all("tbody")[2].find_all("tr"):
    col = row.find_all("td")
    if col:
        name = col[1].text
        market_cap = float(col[2].text)
        data = data.append(
            {"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True
            )

# Re-afirm inside dataframe
data = pd.DataFrame(data)

# API Website with key on end
url3 = "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=EUR&apikey=API_KEY"

# Check if file exists to avoid hitting the API again
if os.path.exists('file_name.csv')==False:
    # GET
    response = requests.get(url3)

    # Store in dataframe
    df = pd.DataFrame(response.json())

    # Write to csv
    df.to_csv('file_name.csv')
else:
    # Continue to execute
    pass

# Read from csv
rates = pd.read_csv('file_name.csv')
rates.head()

# Set first row rates column as variable
eur_rate = rates.loc[0, 'rates']

# Display
print('The EUR rate is = ' + str(eur_rate))

# Create new col and multiply USD column with EUR rate
data["Market Cap (EUR$ Billion)"] = data["Market Cap (US$ Billion)"] * eur_rate

# Display
print(data)
