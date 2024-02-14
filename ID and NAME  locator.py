from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
sleep(5)
driver.maximize_window() # maximize the browser window


#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
driver.find_element(By.NAME,"q").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
sleep(5)