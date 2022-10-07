import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=800,800')
browser = webdriver.Firefox(options=options)
browser.get("https://www.bravesearch.com")

sleep(2)

search = browser.find_element_by_id('searchbox')
search.send_keys('vagas de emprego python')
button = browser.find_element_by_id('submit-button')
button.click()