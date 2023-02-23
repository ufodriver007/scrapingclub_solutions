from bs4 import BeautifulSoup
from requests import Session

work = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari 537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "x-requested-with": "XMLHttpRequest",
}

url = 'https://scrapingclub.com/exercise/basic_captcha/'
resp = work.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')
token = soup.find('form').find('input').get('value')
captcha_0 = soup.find('input', id="id_captcha_0").get('value')
captcha_1 = ''  # TODO write an algorithm to solve captcha

data = {
    'csrfmiddlewaretoken': token,
    "name": "scrapingclub",
    "password": "scrapingclub",
    "captcha_0": captcha_0,
    "captcha_1": captcha_1
}

result = work.post(url, headers=headers, data=data)
print(result)
