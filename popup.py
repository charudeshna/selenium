import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()              # important statement  add Chrome options for popup's
ops.add_argument("--disable-notifications")   # add argument this is are the two important statements
driver = webdriver.Chrome(options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(5)
