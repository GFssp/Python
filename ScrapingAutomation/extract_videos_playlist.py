from encodings import utf_8
import os
from bs4 import BeautifulSoup as bs
import requests
import json
import time

url = 'https://www.youtube.com/playlist?list=PLBkZ7twk12dfufNbLDn-5LebxviSjLeWX'

data = []
response = requests.get(url)
page = response.text
soup = bs(page, 'html.parser')

new_html_file = open('file.html', 'w', encoding='utf_8')
new_html_file.write(str(soup))

html_file = open('file.html', 'r', encoding='utf_8')
blocks = html_file.readlines()
count = 0

while True:
    try:
        block = blocks[count]
    except:
        print("Finished")
        break

    if '"url":"/watch?v=' in block:
        block = block.split('"url":"')
        block_count = 0

        while True:
            try:
                if "/watch?v=" in block[block_count]:
                    inner_content = block[block_count].split('",')
                    inner_count = 0

                    while True:
                        try:
                            if "/watch?v=" in inner_content[inner_count]:
                                url = "https://www.youtube.com"+inner_content[inner_count]
                                data.append(url)
                        except:

                            break

                        inner_count += 1
                
            except:
                break

            block_count += 1
        
    count += 1

new_html_file.close()
html_file.close()
os.remove("file.html")

with open('links.txt', 'w', encoding='utf_8') as file:
    for link in data:
        file.write(link + '\n')
    file.close()
























