from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

input_box = driver.find_element(By.CLASS_NAME, "gLFyf")
input_box.send_keys("Ben 10", Keys.ENTER) 

time.sleep(10)

driver.quit()
