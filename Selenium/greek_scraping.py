from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

with open('greek_characters.txt') as file:
    entities = file.readlines()
reversed_entities = entities[::-1]

symbols = {}


def scrape_symbols(entities):
    for entity in entities:
        to_search = entity.replace('\n', '')
        print(to_search)
        if to_search in symbols.keys():
            print('continuing')
            continue
        symbols[to_search] = ''
        # Searching
        driver.get(f"https://en.wikipedia.org/wiki/{to_search}")

        labels = driver.find_elements(by=By.CLASS_NAME, value='infobox-label')
        info = driver.find_elements(by=By.CLASS_NAME, value='infobox-data')
        if len(labels) == 0:
            continue
        for n in range(len(labels)):
            label = labels[n].text
            if label == 'Symbol':
                symbols[to_search] = info[n].text
                break


def record_symbols(symbols):
    with open('greek_god_symbols.txt', 'w') as f:
        for god in symbols:
            if symbols[god] != '':
                f.write(f"{god}: {symbols[god]}\n")


scrape_symbols(entities)
record_symbols(symbols)
driver.quit()

