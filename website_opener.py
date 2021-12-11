from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()
browser.get('https://techwithtim.net')

search = browser.find_element(By.NAME,"s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(10)

try:
    main = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements(By.TAG_NAME, "article") 
    for article in articles:
       header = article.find_element(By.CLASS_NAME, "entry-summary")
       print(header.text)

finally:
    browser.quit()

