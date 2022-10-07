import requests
import json
import time

response1 = requests.get('https://api.fbi.gov/wanted/v1/list')
data = json.loads(response1.content)
items = data['items']
perfile_counter = 1
characters = ['<p>', '</p>']
detail = items[perfile_counter]['details']
detail = str(detail)

print('FBI MOST WANTED - API 2020')
time.sleep(2)

while perfile_counter < 20:

    name = items[perfile_counter]['title']

    for c in characters:
        detail = detail.replace(c, '')

    print(f'{name} - {detail}')
    time.sleep(1)

    perfile_counter += 1
