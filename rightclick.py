import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys, ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(5)

button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver) # create object for actionchains ,which is important

act.context_click(button).perform() #  context click is used for right click

time.sleep(3)