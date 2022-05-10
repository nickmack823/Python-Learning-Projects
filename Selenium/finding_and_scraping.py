from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Opens Amazon page and gets item price
# driver.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=pd_lpo_2?pd_rd_i=B07588SJHN&psc=1")
# price = driver.find_element(by=By.CLASS_NAME, value='a-price')
# print(price.text)

driver.get('https://python.org')
search_bar = driver.find_element(by=By.NAME, value='q')
print(search_bar.tag_name)

# Get anchor tag within item with this css selector
doc_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
print(doc_link.text)

# Using XPath (inspect --> copy --> copy XPath)
bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# Getting multiple elements in a list
event_dates = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')
events = {}
for n in range(len(event_names)):
    events[n] = {
        'name': event_names[n].text,
        'time': event_dates[n].text,
    }
print(events)


# Closes active tab
# driver.close()
# Closes entire browser
driver.quit()


