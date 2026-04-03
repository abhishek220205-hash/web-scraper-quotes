import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://quotes.toscrape.com/page/{}/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    page = 1

    while True:
        url = base_url.format(page)

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            print(f"❌ Error on page {page}: {e}")
            break

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            break

        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            tags = [tag.text for tag in q.find_all("a", class_="tag")]
            writer.writerow([text, author, ", ".join(tags)])

        print(f"Page {page} scraped...")

        time.sleep(1)
        page += 1

print("✅ Data saved to quotes.csv")