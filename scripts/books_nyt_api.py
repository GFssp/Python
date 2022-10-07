import requests
import json
from time import sleep
from termcolor import colored


print('--------------------------------------------')
print('BEST SELLERS OF NEW YORK TIMES')
print('--------------------------------------------')


def execute():
  requestUrl = "https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=vukkIyZIQNgdIZAQQ1GWnsVafjzdDHoy"
  requestHeaders = {
    "Accept": "application/json"
  }

  response = requests.get(requestUrl, headers=requestHeaders).text
  data = json.loads(response)
  results = data['results']
  
  for book in results:

    title = book['title']
    title = title.replace("'", "")
    print('->', title)

    for key, value in book.items():

        print(f'{key}: {value}')

    print('----------------')

  end = input('Type enter to exit >')
  print(colored('Bye :)', 'red'))
  sleep(1)


if __name__ == "__main__":
    execute()
    sleep(10)
