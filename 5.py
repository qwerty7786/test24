from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://ya.ru/')

element = driver.find_element(By.CLASS_NAME,'informers3__item-icon')

element.click()

