from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Clicking an element
# article_count = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
# article_count.click()

# Finding a link by its text
# all_portals = driver.find_element(by=By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Searching
search = driver.find_element(by=By.NAME, value='search')
search.send_keys('Hercules')
search.send_keys(Keys.ENTER)

result = driver.find_element(by=By.LINK_TEXT, value='Hercules')
result.click()

labels = driver.find_elements(by=By.CLASS_NAME, value='infobox-label')
info = driver.find_elements(by=By.CLASS_NAME, value='infobox-data')

driver.quit()
