import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# using switching commands

# driver.get("https://demo.nopcommerce.com")
# driver.maximize_window()
# reglink = Keys.CONTROL + Keys.RETURN # switcing commamnds
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# time.sleep(5)

# using selenium 4 new tab

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")


# using selenium 4 new window

driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")

