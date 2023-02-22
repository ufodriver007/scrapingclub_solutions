from requests import Session
import json

work = Session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari 537.36",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest"
}

url = 'https://scrapingclub.com/exercise/detail_cookie/'
work.get(url, headers=headers, allow_redirects=True)

cookies = work.cookies.get_dict()
response = work.get(f"https://scrapingclub.com/exercise/ajaxdetail_cookie/?token={cookies['token']}", headers=headers, cookies=cookies, allow_redirects=True)

with open("example.json", "w") as f:
    json.dump(json.loads(response.text), f, indent=4, ensure_ascii=False)
