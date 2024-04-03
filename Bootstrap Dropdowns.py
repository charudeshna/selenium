import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

time.sleep(10)
country_list = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(country_list))

for country in country_list:
    if country.text == "Iran":
        country.click()
        break

time.sleep(5)
