import requests
from bs4 import BeautifulSoup
import json
import csv


def get_paths() -> list:
    paths = []
    response = requests.get('https://scrapingclub.com/exercise/list_infinite_scroll/?page=1')
    soup = BeautifulSoup(response.text, 'lxml')
    number_of_pages = len(soup.findAll('li', class_='page-item')) - 1
    for page in range(number_of_pages):
        response = requests.get(f'https://scrapingclub.com/exercise/list_infinite_scroll/?page={page}')
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.findAll('h4', class_='card-title')
        for elem in items:
            paths.append('https://scrapingclub.com' + elem.find_next().get('href'))
    return paths


def get_data(path):
    headers = {
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        'https://scrapingclub.com/exercise/list_detail_ajax_infinite_scroll' + path[61:],
        headers=headers,
    )
    return json.loads(response.text)


for path in get_paths():
    with open('file.csv', 'a') as f:
        data = get_data(path)
        csvout = csv.writer(f)
        csvout.writerow([data['title'], data['price'], data['description']])
