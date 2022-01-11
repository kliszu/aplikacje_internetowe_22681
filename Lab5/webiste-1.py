import requests
from bs4 import BeautifulSoup
import csv

site = requests.get("https://partnerzy.pl/zespol")
site_new = BeautifulSoup(site.content, 'html.parser')

workers = list()

rows  = site_new.find_all('div', attrs={'class':'offer-type-information clearfix'})


for item in rows:
    if len(item.p.contents) == 0:
        description = None
    else:
        description = item.p.contents[0]
    employe = {
        "Name": item.h1.contents[0],
        "Job title": item.span.contents[1].contents[0],
        "profile link": "https://partnerzy.pl"+item.a['href'],
        "description": description,
    }
    workers.append(employe)


with open('workers.csv','a', newline='') as file:
    dict_writer = csv.DictWriter(file, workers[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(workers)
