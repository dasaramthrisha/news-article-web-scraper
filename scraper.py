import requests
from bs4 import BeautifulSoup

url = input("Enter Reuters article URL: ")

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Get Title
title = soup.find("h1")
if title:
    print("\nTitle:")
    print(title.text.strip())

# Get Article Content
print("\nArticle Content:\n")

paragraphs = soup.find_all("p")

for p in paragraphs:
    text = p.get_text(strip=True)
    if text:
        print(text)
