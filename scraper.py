from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
userFavoriteGenres = {"Fiction" : 1}
bookScores = {}

def findBookGenres(bookDriver, dict):
    genres = bookDriver.find_elements(By.CLASS_NAME, "BookPageMetadataSection__genreButton")
    for genre in genres:
        a = genre.find_element(By.TAG_NAME, "a")
        nameOfGenre = a.find_element(By.TAG_NAME, "span").text
        if nameOfGenre in dict:
            dict[nameOfGenre] = 1
        else:
            dict[nameOfGenre] += 1
        print(nameOfGenre)
    return 1

def analyzeUserList():
    # insert link to YOUR OWN list of books you want to find a similar one to
    driver.get('https://www.goodreads.com/review/list/99850740-hiba?ref=nav_mybooks&shelf=favorites')  # open GR site with the list
    print(driver.title)

    booksTable = driver.find_element(By.ID, "booksBody")
    rows = booksTable.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
    for row in rows:
        # Get the book names (all the 4th column = index 3)
        col = row.find_elements(By.TAG_NAME, "td")[3]
        print(col.text)  # prints title of each book

        book_title_element = col.find_element(By.TAG_NAME, "a")
        # Extract the book title text
        book_title = book_title_element.text

        # Get the href attribute of the link
        book_link = book_title_element.get_attribute('href')

        print(f"Title: {book_title}")

        # New browser to loop thru the books so that the for loop of the initial page is preserved
        driver2 = webdriver.Firefox()
        # Navigate to a new URL in the newly opened window or tab
        driver2.get(book_link)
        # find all the most common genres and save it into listGenres
        listGenres = findBookGenres(driver2, userFavoriteGenres)
        driver2.close()  # to go back to the prev page

    print(userFavoriteGenres)

def analyzePublicList():
    #driver.get('https://www.goodreads.com/list/show/63.Favorite_Books')
    driver.get('https://www.goodreads.com/list/show/154685.TOP_YA_Dystopian_Books_of_ALL_TIME')

    booksTable = driver.find_element(By.ID, "all_votes")

    rows = booksTable.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
    for row in rows:

        bookClass = row.find_element(By.CLASS_NAME, "bookTitle")
        book_title = bookClass.find_element(By.TAG_NAME, 'span').text
        print(book_title)
        book_link = bookClass.get_attribute('href')

        # New browser to loop thru the books so that the for loop of the initial page is preserved
        driver2 = webdriver.Firefox()
        # Navigate to a new URL in the newly opened window or tab
        driver2.get(book_link)
        score = 0

        genres = driver2.find_elements(By.CLASS_NAME, "BookPageMetadataSection__genreButton")
        for genre in genres:
            a = genre.find_element(By.TAG_NAME, "a")
            nameOfGenre = a.find_element(By.TAG_NAME, "span").text
            if nameOfGenre in userFavoriteGenres:
                score += 1

        if score > 0:
            bookScores[book_title] = score

        driver2.close()  # to go back to the prev page

    print("Based on your favorite genres, you would enjoy: ")
    for rec in bookScores:
        print(rec)

#analyzeUserList()
analyzePublicList()
driver.close()  # close the browser
