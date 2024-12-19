# Import required modules from selenium and time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome webdriver service using local chromedriver.exe
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search input box by its class name and enter search term
input_box = driver.find_element(By.CLASS_NAME, "gLFyf")
input_box.send_keys("Ben 10", Keys.ENTER) 

# Wait for 10 seconds to see the results
time.sleep(10)

# Close the browser
driver.quit()
