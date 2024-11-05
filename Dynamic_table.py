import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

user_name = driver.find_element(By.NAME,'username')
user_name.send_keys("Admin")

pass_word = driver.find_element(By.NAME,'password')
pass_word.send_keys("admin123")

log_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(7)

driver.find_element(By.LINK_TEXT,'Admin').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,'oxd-topbar-body-nav-tab-item').click()
time.sleep(3)
driver.find_element(By.CLASS_NAME,'oxd-topbar-body-nav-tab-link').click()
time.sleep(5)

rows = len(driver.find_elements(By.XPATH,"table[@id='resultTable']//tbody/tr"))
print("total number of rows in a table:",rows)

count=0
for r in range(1,rows+1):
    status=driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[5]").text
    if status =="Enabled":
        count = count+1

print("Total Number of users:",rows)
print("Number of enabled users:",count)
print("Number of disabled users:",(rows-count))

driver.close()
