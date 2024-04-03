import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# capture the cookies from the browser

# cookies = driver.get_cookies()
# print(len(cookies))

# print the details of all cookies

#for c in cookies:
#   print(c)
#    print(c.get('name'),":",c.get('value'))

# Add new cokkie to the browser

# driver.add_cookie({"name":"mycookie","value":"123456"})
# cookies = driver.get_cookies()
# print("size of cookies after adding new one:",len(cookies))

# delete specific cookie from the browser
# driver.delete_cookie("mycookie")
# cookies = driver.get_cookies()
# print(len(cookies))

# delete all the cookies
driver.delete_all_cookies()