# Code to login
# Code to extract description
# Code to sort description using length

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=serv_obj,options=options)
driver = webdriver.Chrome(options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

product_desc = driver.find_elements(By.CLASS_NAME, 'inventory_item_desc')


prod_desc = []

for desc in product_desc:
    prod_desc.append(desc.text)
    #print(len(desc.text))
print(sorted(prod_desc, key=len))


driver.quit()

