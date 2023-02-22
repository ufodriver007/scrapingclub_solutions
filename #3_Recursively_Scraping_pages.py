import requests
from bs4 import BeautifulSoup
import re
import csv


def get_paths() -> list:
    page = 1
    path_list = []
    while True:
        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        search = re.search(r'.*(?=\n)', soup.find('li', class_='page-item active').find('span', class_="page-link").text.strip())
        current_page = int(search.group())

        if current_page == page:

            cards_list = soup.findAll('div', class_='col-lg-4 col-md-6 mb-4')
            for card in cards_list:
                path = card.find('a').get('href')
                path_list.append("https://scrapingclub.com" + path)
            page += 1
        else:
            return path_list


def get_data(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    card = soup.find('div', class_="card-body")
    title = card.find('h3').text
    price = card.find('h4').text
    description = card.find('p').text
    with open('example.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([title, price, description])


for path in get_paths():
    get_data(path)
