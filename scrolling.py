import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

# very very important note that that scrolling cannot be done with the help of action
#  chains,  so with the help of JAVASCRIPT we will automate scrolling action

# scrolling using pixel

driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print("The number of pixels moved:",value)

# scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
value = driver.execute_script("return window.pageYOffset;")
print("The number of pixels moved:",value)

# scroll up position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)", "")
value = driver.execute_script("return window.pageYOffset;")
print("The number of pixels moved:",value)


