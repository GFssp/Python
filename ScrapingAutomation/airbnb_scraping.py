import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
## Para não abrir
#options.add_argument('--headless')
options.add_argument('window-size=800,800')
browser = webdriver.Firefox(options=options)

browser.get("https://www.airbnb.com")

sleep(2)

site = BeautifulSoup(browser.page_source, 'html.parser')

print(site.prettify())