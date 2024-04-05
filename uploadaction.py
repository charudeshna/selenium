import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()              # important statement  add Chrome options for popup's
ops.add_argument("--disable-notifications")   # add argument this is are the two important statements
driver = webdriver.Chrome(options=ops)

driver.get("https://www.dia-pen.hr/orbicon/3rdParty/rad-plus/test.html")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='userfile[0]']").send_keys("C:\selenium\sample.py")

time.sleep(5)