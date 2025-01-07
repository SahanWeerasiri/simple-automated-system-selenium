# Import required modules from selenium and time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests


# Set up the download directory
download_dir = "C:/Users/SAHAN/Downloads"  # Change to your desired path

# Set up the Chrome webdriver service using local chromedriver.exe
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Navigate to Google's homepage
driver.get("https://www.youtube.com")

# Find the search input box by its class name and enter search term
input_box = driver.find_element(By.CLASS_NAME, "ytSearchboxComponentInput")
input_box.send_keys("Bat man", Keys.ENTER)

# Wait for search results to load
time.sleep(2)

first_result = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer a#video-title")
url = first_result[3].get_attribute("href")
print(f"Video URL: {url}")

driver.get("https://turboscribe.ai/downloader/youtube/mp4")

input_box = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div[2]/form/div/input")
input_box.clear()  # Clear any existing text first
input_box.send_keys(url)
btn = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div[2]/form/div/button")
btn.click()

time.sleep(3)

# turnning point    /html/body/div[2]/main/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div
# sample            /html/body/div[2]/main/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/a[1]

video_box = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/a[1]")

url = video_box.get_attribute("href")


response = requests.get(url, stream=True)
with open(download_dir+"/video.mp4", "wb") as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
print("Downloading...")
time.sleep(5)
print("Terminate Downloading process manually - This is a demo")

driver.quit()
