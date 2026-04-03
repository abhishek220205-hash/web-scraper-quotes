import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        text = text.encode('utf-8').decode('utf-8')

        author = q.find("small", class_="author").get_text(strip=True)

        writer.writerow([text, author])

print("Data saved to quotes.csv")