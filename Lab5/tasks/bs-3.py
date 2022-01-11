import requests
from bs4 import BeautifulSoup

webpage = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(webpage.content, 'html.parser')

tags_h1 = []

for item in soup.select('h1'):
    tags_h1.append(item.text)


p_element = soup.select('p')[6].text

print(tags_h1, p_element)

