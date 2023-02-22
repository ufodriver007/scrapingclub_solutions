import requests
import json

url = 'https://scrapingclub.com/exercise/ajaxdetail/'
response = requests.get(url)

data_dict = json.loads(response.text)
with open('data.json', 'w') as f:
    json.dump(data_dict, f, indent=4, ensure_ascii=False)


