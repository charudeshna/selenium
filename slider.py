import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(5)


min_slider = driver.find_element(By.XPATH,"//body//div//span[1]")
max_slider = driver.find_element(By.XPATH,"//body//div//span[2]")


print("location before moving ") # before moving {'x': 59, 'y': 250} ,{'x': 59, 'y': 250}
print (min_slider.location)
print(max_slider.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,20,0).perform()
act.drag_and_drop_by_offset(max_slider,-40,0).perform()


time.sleep(4)

print("location After moving ") #location After moving 'x': 82, 'y': 250},{'x': 469, 'y': 250}

print (min_slider.location)
print(max_slider.location)
