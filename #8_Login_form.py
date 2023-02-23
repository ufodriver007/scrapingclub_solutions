from bs4 import BeautifulSoup
from requests import Session

work = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari 537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "x-requested-with": "XMLHttpRequest",
    'origin': 'https://scrapingclub.com',
    'referer': 'https://scrapingclub.com/exercise/basic_login/',
}

url = 'https://scrapingclub.com/exercise/basic_login/'
resp = work.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')
token = soup.find('form').find('input').get('value')

data = {'csrfmiddlewaretoken': token, "name": "Existor", "password": "12345"}
result = work.post(f"https://scrapingclub.com/exercise/basic_login/", headers=headers, data=data)
print(result)
