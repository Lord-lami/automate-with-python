from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service(
    service_args=[
        "--profile-root=/home/gamp/firefox-selenium"
    ]
)

browser = webdriver.Firefox(service=service)

browser.get('https://autbor.com/example3.html')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')
print(elems[0].text)
print(elems[0].get_property('innerHTML'))