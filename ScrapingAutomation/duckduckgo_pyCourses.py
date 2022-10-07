from selenium import webdriver
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox()
driver.get("https://duckduckgo.com/")

search = driver.find_element(by='id', value="search_form_input_homepage")
search.send_keys('python courses')

button = driver.find_element(by='id',value="search_button_homepage")
button.click()