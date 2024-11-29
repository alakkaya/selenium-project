from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/Users/ali/Desktop/PYTHON/selenium project/chromedriver"

driver = webdriver.Chrome(service=Service(chromedriver_path))

driver.get("https://google.com")

# waits until the elements exists
WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf") )
)

# put the input
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("selenium docs" + Keys.ENTER)

WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Selenium with Python - Read the Docs") )
)

# clicking links & navigating pages
link = driver.find_element(By.PARTIAL_LINK_TEXT,"Selenium with Python - Read the Docs") #LINK_TEXT
link.click()

time.sleep(10);

driver.quit()