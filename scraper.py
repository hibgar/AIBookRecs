from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import bs4

driver = webdriver.Firefox()

driver.get('https://www.goodreads.com/review/list/99850740-hiba?ref=nav_mybooks&shelf=favorites') #open GR site with the list
print(driver.title)

booksTable = driver.find_element(By.ID, "booksBody")
#for item in booksTable.find_elements(By.CSS_SELECTOR,'tr'):
    #print(item.text)
    #if item.get_attribute("class") == "field title":
        #print(item.text)
        #value = item.find_element(By.CLASS_NAME, "value")
        #innerTitleItem = value.find_element(By.CSS_SELECTOR, "a")
        #print(innerTitleItem)

rows = booksTable.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
for row in rows:
    # Get the book names (all the 4th column = index 3)
    col = row.find_elements(By.TAG_NAME, "td")[3]
    print(col.text) #prints text from the element

driver.close() # close the browser