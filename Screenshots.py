import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome()


driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
driver.implicitly_wait(10)

# important commands for screenshots 

# driver.save_screenshot("C:\\Users\\charudeshna.n\\PycharmProjects\\selenium\\homepage.png")
# driver.save_screenshot(os.getcwd()+"\\homepage.png")

# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

# driver.get_screenshot_as_png() or driver.get_screenshot_as_base64()

