import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = "http://quotes.toscrape.com/page/{}/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

num_pages = int(input("Enter number of pages to scrape: "))

# 👉 Filter input
filter_type = input("Filter by 'author', 'tag', or press Enter for none: ").lower()
filter_value = input("Enter filter value (or leave blank): ").lower()

data = []

for page in range(1, num_pages + 1):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = [tag.text for tag in q.find_all("a", class_="tag")]

        # 👉 Apply filter
        if filter_type == "author" and filter_value:
            if filter_value not in author.lower():
                continue

        if filter_type == "tag" and filter_value:
            if not any(filter_value in tag.lower() for tag in tags):
                continue

        data.append({
            "quote": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    print(f"Page {page} scraped...")

# 👉 Save CSV
with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    writer.writerows(data)

# 👉 Save JSON
with open("quotes.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"✅ Done! {len(data)} filtered quotes saved.")