**import requests**

**from bs4 import BeautifulSoup**

**import csv**



**base\_url = "http://quotes.toscrape.com/page/{}/"**



**with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:**

&#x20;   **writer = csv.writer(file)**

&#x20;   **writer.writerow(\["Quote", "Author"])**



&#x20;   **page = 1**



&#x20;   **while True:**

&#x20;       **url = base\_url.format(page)**

&#x20;       **response = requests.get(url)**

&#x20;       **response.encoding = 'utf-8'**



&#x20;       **soup = BeautifulSoup(response.text, "html.parser")**

&#x20;       **quotes = soup.find\_all("div", class\_="quote")**



&#x20;       **# Stop when no quotes found**

&#x20;       **if not quotes:**

&#x20;           **break**



&#x20;       **for q in quotes:**

&#x20;           **text = q.find("span", class\_="text").text**

&#x20;           **author = q.find("small", class\_="author").text**

&#x20;           **writer.writerow(\[text, author])**



&#x20;       **print(f"Page {page} scraped...")**

&#x20;       **page += 1**



**print("✅ Data saved to quotes.csv")**

