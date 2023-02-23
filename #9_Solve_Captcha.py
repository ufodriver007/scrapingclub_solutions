from bs4 import BeautifulSoup
import requests
from requests import Session
import easyocr


def text_recognition(path: str) -> str:
    reader = easyocr.Reader(["en"])
    res = reader.readtext(path, detail=0, paragraph=True)
    return res[0] if res else ''


work = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari 537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://scrapingclub.com",
    "referer": "https://scrapingclub.com/exercise/basic_captcha/"
}

url = 'https://scrapingclub.com/exercise/basic_captcha/'
resp = work.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')
token = soup.find('form').find('input').get('value')
captcha_0 = soup.find('input', id="id_captcha_0").get('value')

resp = requests.get(f'https://scrapingclub.com/captcha/image/{captcha_0}/', stream=True)
r = open('captcha.png', 'wb')
for value in resp.iter_content(1024 * 1024):
    r.write(value)
r.close()

captcha_1 = text_recognition('captcha.png').lower()

data = {
    'csrfmiddlewaretoken': token,
    "name": "scrapingclub",
    "password": "scrapingclub",
    "captcha_0": captcha_0,
    "captcha_1": captcha_1
}

cookie = work.cookies.get_dict()
result = work.post(url, headers=headers, data=data, cookies=cookie)
