import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)


# 1 ) count  number of rows and columns


noofrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))

noofcolumns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noofrows)
print(noofcolumns)


# 2 ) Read specific row and coloumns

data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
print(data)

# Read all the rows and columns data


#for r in range (2,noofrows+1):
#    for c in range(1,noofcolumns+1):
#        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
#        print(data)
#    print()


# read data based on certain condition  (list books name whose author is mukhesh)


for r in range (2,noofrows+1):
    author_name  = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[2]").text
    if author_name == 'Mukesh':
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        print(book_name,price)



