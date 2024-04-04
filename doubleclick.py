import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame("iframeResult") # switch to frame

button = driver.find_element(By.XPATH,"//p[@ondblclick='myFunction()']")

act = ActionChains(driver) # create a object for action chains very important 
act.double_click(button).perform() # important command for double click

time.sleep(4)


