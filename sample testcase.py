from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
sleep(5)
driver.find_element(By.NAME,"password").send_keys("admin123")
sleep(5)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(5)