import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(5)

# create a object for action chains that is very important
act = ActionChains(driver)

# source element and target element are important in drag and drop actions

rome_ele = driver.find_element(By.XPATH,"//div[@id='box6']")
italy_ele = driver.find_element(By.XPATH,"//div[@id='box106']")

act.drag_and_drop(rome_ele,italy_ele).perform()
time.sleep(3)



