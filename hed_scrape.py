import requests
from bs4 import BeautifulSoup

def scrape_heds():
    url = 'https://www.avclub.com/tag/game-of-thrones'

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    info = soup.find_all('div', class_='item__content item__content--thumb')

    links = []

    for x in range(len(info)):
        hed = info[x].h1.div.text
        href = info[x].h1.a['href']
        links_dict = {'hed' : hed, 'href' : href}
        links.append(links_dict)
    
    return {
        'links' : links
    }