import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://realpython.github.io/fake-jobs/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Filter input
filter_type = input("Filter by 'location', 'company', or press Enter for none: ").lower()
filter_value = input("Enter filter value (or leave blank): ").lower()

response = requests.get(base_url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch data")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

data = []

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    # Apply filters
    if filter_type == "location" and filter_value:
        if filter_value not in location.lower():
            continue

    if filter_type == "company" and filter_value:
        if filter_value not in company.lower():
            continue

    data.append({
        "title": title,
        "company": company,
        "location": location
    })

# Save CSV
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "company", "location"])
    writer.writeheader()
    writer.writerows(data)

print(f"✅ {len(data)} jobs saved after filtering")