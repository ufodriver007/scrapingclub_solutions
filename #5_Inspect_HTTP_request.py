import requests
import json


headers = {
    'x-requested-with': 'XMLHttpRequest'
}
response = requests.get('https://scrapingclub.com/exercise/ajaxdetail_header/', headers=headers)
data_dict = json.loads(response.text)
with open('data.json', 'w') as f:
    json.dump(data_dict, f, indent=4, ensure_ascii=False)
