# Import required modules from selenium and time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Product:
    name = ""
    price = ""
    link = ""
    image = ""

# Set up the Chrome webdriver service using local chromedriver.exe
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

link = "https://www.daraz.lk/catalog/?spm=a2a0e.tm80335410.search.d_go&q="

obj = "Benz car"

no_of_items = 4

driver.get(link+obj)

# root(turnning point)                 /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]
# child(image)                         /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img
# price                                 /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span
# link , name                           /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a

items = []

for i in range(no_of_items):
    item = Product()
    item.image = (driver.find_element(By.XPATH,f'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i+1}]/div/div/div[1]/div/a/div/img')).get_attribute('src')
    item.name = (driver.find_element(By.XPATH,f'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i+1}]/div/div/div[2]/div[2]/a')).text
    item.price = (driver.find_element(By.XPATH,f'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i+1}]/div/div/div[2]/div[3]/span')).text
    item.link = (driver.find_element(By.XPATH,f'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[{i+1}]/div/div/div[2]/div[2]/a')).get_attribute('href')
    items.append(item)

for item in items:
    print("--------------------------------Item--------------------------------")
    print(item.image)
    print(item.name)
    print(item.price)
    print(item.link)
    print("----------------------------------------------------------------")

driver.quit()
