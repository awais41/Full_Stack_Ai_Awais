import pandas as pd 
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div" , class_ = "quote")
print(len(quotes))

data = []

for quote in quotes:
    text = quote.find("span" , class_="text")
    print(text.text)

    Author = quote.find("small", class_= "author")
    print(Author.text)
    data.append({"quote": text.text, "author": Author.text})


print(data)

df = pd.DataFrame(data)
df.to_csv("quotes.csv" , index = False)

