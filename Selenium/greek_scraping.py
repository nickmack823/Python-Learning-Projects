from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")


with open('greek_characters.txt') as file:
    entities = file.readlines()

symbols = {}
for entity in entities:
    to_search = entity.replace('\n', '')
    print(to_search)
    # Searching
    search = driver.find_element(by=By.NAME, value='search')
    search.send_keys(to_search)
    search.send_keys(Keys.ENTER)
    result = driver.find_element(by=By.LINK_TEXT, value=to_search)
    result.click()

    labels = driver.find_elements(by=By.CLASS_NAME, value='infobox-label')
    info = driver.find_elements(by=By.CLASS_NAME, value='infobox-data')
    if len(labels) == 0:
        continue
    for n in range(len(labels)):
        label = labels[n].text
        if label == 'Symbol':
            symbols[to_search] = info[n].text
            break

print(symbols)
driver.quit()
