import requests
from bs4 import BeautifulSoup

# Set scrape function
def scrape_heds():
    url = 'https://www.avclub.com/tag/game-of-thrones'

    # Get the html from a request to the url
    response = requests.get(url)

    html = response.text

    # Convert the html into a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')

    # Get all info from the specified .find_all() location
    info = soup.find_all('div', class_='sqekv3-5 hVuiJw')

    # Create empty list for the info to be pulled
    links = []

    # Get headline text and hrefs using a for loop and 
    # append as dictionaries to the empty links list
    for x in range(len(info)):
        hed = info[x].h1.text
        href = info[x].a['href']
        links_dict = {'hed' : hed, 'href' : href}
        links.append(links_dict)
    
    # Return the links list as a dictionary value
    return {
        'links' : links
    }