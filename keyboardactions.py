import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)



driver.get("https://gotranscript.com/text-compare")
driver.maximize_window()
time.sleep(5)


input1 = driver.find_element(By.XPATH,"//textarea[@placeholder='Paste one version of the text here.']")
input2 = driver.find_element(By.XPATH,"//textarea[@placeholder='Paste another version of the text here.']")

input1.send_keys("welcome to selenium")
input2.send_keys("welcome to selenium")

act = ActionChains(driver)

# input 1 Ctrl + A , select text

# act.key_down(keys.CONTROL)
# act.send_keys("a")
# act.key_up(keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

time.sleep(4)


# input 1 Ctrl + C ,copy text

# act.key_down(keys.CONTROL)
# act.send_keys("c")
# act.key_up(keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(4)


# select tab to navigate to next input

act.send_keys(Keys.TAB).perform()


# input 2 Ctrl + v ,paste text
# act.key_down(keys.CONTROL)
# act.send_keys("v")
# act.key_up(keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(7)



