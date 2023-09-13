from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bs4

PATH = "/home/geckodriver"
driver = webdriver.Firefox()

driver.get('https://www.goodreads.com/review/list/99850740-hiba?ref=nav_mybooks&shelf=favorites')
print(driver.title)

table = driver.find_element(By.ID, "books")

print(table)
#time.sleep(3)
driver.close()