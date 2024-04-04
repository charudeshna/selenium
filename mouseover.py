import time


from selenium import webdriver
from selenium.webdriver import ActionChains
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

# make a variable
admin = driver.find_element(By.LINK_TEXT,'Admin').click()
time.sleep(3)
usermanagement = driver.find_element(By.CLASS_NAME,'oxd-topbar-body-nav-tab-item').click()
time.sleep(3)
user = driver.find_element(By.CLASS_NAME,'oxd-topbar-body-nav-tab-link').click()
time.sleep(5)

# mouse over actions

act = ActionChains(driver)  # create object for action chains which is important
act.move_to_element(admin).move_to_element(usermanagement).move_to_element(user).click().perform() # move to element command is important for mouse over actions.
