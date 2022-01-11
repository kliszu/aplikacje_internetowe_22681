import requests
from bs4 import BeautifulSoup

webpage = requests.get("http://www.ufo-ski.pl/")
soup = BeautifulSoup(webpage.content, "lxml")
title = soup.title.text

print(soup)
print(title)