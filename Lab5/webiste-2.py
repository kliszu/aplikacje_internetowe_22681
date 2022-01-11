import requests
from bs4 import BeautifulSoup

search_link = 'https://pypi.org/search/?q={}'
link = 'https://pypi.org/{}'

def package_search(query):
    response = requests.get(search_link.format(query))
    response_soup = BeautifulSoup(response.content, 'html.parser')
    names = response_soup.find_all('span', attrs={'class':'package-snippet__name'}, limit=5)
    versions = response_soup.find_all('span', attrs={'class' : 'package-snippet__version'}, limit=5)
    links = response_soup.find_all('a', attrs={'class':'package-snippet'}, limit=5)
    result = list()
    for i in range(0,5):
        element = [
            names[i].contents[0],
            versions[i].contents[0],
            link.format(links[i]['href'])
        ]
        result.append(element)
    return result
    

def package_detail(package_url):
    link_get = requests.get(package_url)
    link_soup = BeautifulSoup(link_get.content, 'html.parser')
    banner = link_soup.find('h1', attrs={'class':'package-header__name'}).contents[0]
    installation_commnad = link_soup.find('span', attrs={'id' : 'pip-command'}).contents[0]
    description = link_soup.find('div', attrs= { 'class' : 'project-description'}).contents
    return [banner, installation_commnad, description]

def main():
    print("This program returns search result from pypi.org and shows package details")
    query = input("Enter name of the package: ")
    if(isinstance(query, str)):
        res = package_search(query)
        print("Shows 5 best results:\n")
        for el in res:
            print('{}. {} {} \n'.format(res.index(el)+1, el[0], el[1]))
        pick = int(input("Enter number of package: "))
        if pick in range(1,6):
            details = package_detail(res[pick-1][2])
            print("Name: {}\npip command: {}\ndescription: {} \n".format(details[0],details[1], details[2]))


if __name__== '__main__':
    main()