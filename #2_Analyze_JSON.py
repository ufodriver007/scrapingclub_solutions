import re
import requests
from bs4 import BeautifulSoup
import json


url = 'https://scrapingclub.com/exercise/detail_json/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
script = soup.find('script', string=re.compile('var obj = '))
json_text = re.search(r'(?<=\{)(.+)(?=\};)', script.text, flags=re.DOTALL + re.MULTILINE)

new_dict = {}
for line in json_text.group(1).split('\n'):
    if line:
        li = re.findall(r'\".*?\"', line)
        new_dict[li[0].replace('\"', '')] = ''.join(li[1:]).replace('\"', '')

with open("example.json", 'w') as f:
    json.dump(new_dict, f, indent=4, ensure_ascii=False)


