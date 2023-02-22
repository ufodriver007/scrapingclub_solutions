import requests
from bs4 import BeautifulSoup
import csv


url = 'https://scrapingclub.com/exercise/detail_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

img = soup.find('img', class_='card-img-top img-fluid').get('src')
title = soup.find('div', class_='card-body').find('h3').text
price = soup.find('div', class_='card-body').find('h4').text
description = soup.find('div', class_='card-body').find('p').text

with open('result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['https://scrapingclub.com' + img, title, price, description])
