import requests
from bs4 import BeautifulSoup

webpage =requests.get( "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(webpage.content, 'lxml')

title = soup.title
body = soup.body
head = soup.head

print(title, head)