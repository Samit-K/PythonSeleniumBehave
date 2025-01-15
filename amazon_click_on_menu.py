from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=serv_obj,options=options)
driver = webdriver.Chrome(options=options)

driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.refresh()
driver.find_element(By.XPATH, "//span[@class='hm-icon-label'][normalize-space()='All']").click()
# driver.find_element(By.XPATH, '//a[@aria-label="See All Categories"]//div[contains(text(),"See all")]').click()
# locator = driver.find_element(By.XPATH, '//a[@aria-label="See All Categories"]//div[contains(text(),"See all")]')
# driver.execute_script("arguments[0].scrollIntoView();", element)
# element.click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
    (By.XPATH, '//a[@aria-label="See All Categories"]//div[contains(text(),"See all")]')))
element.click()
books = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[3]/div[2]/div[2]/ul[1]/ul[1]/li[7]/a[1]')))
books.click()
all_books = driver.find_element(By.XPATH,"//a[normalize-space()='All Books']")
driver.execute_script("arguments[0].click();", all_books)

