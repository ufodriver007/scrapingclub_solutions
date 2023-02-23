from requests import Session
import hashlib
import json


work = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari 537.36",
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "x-requested-with": "XMLHttpRequest"
}

url = 'https://scrapingclub.com/exercise/detail_sign/'
resp = work.get(url, headers=headers)
cookie = work.cookies.get_dict()

token = cookie['token']
sign = hashlib.md5(token.encode())

result = work.get(f"https://scrapingclub.com/exercise/ajaxdetail_sign/?sign={sign.hexdigest()}", headers=headers)
with open("example.json", "w") as f:
    json.dump(json.loads(result.text), f, indent=4, ensure_ascii=False)
