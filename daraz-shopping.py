# Import required modules from selenium and time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Product:
    name = ""
    description = ""
    price = ""
    link = ""
    rate = ""
    image = ""

# Set up the Chrome webdriver service using local chromedriver.exe
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

link = "https://www.daraz.lk/catalog/?spm=a2a0e.tm80335410.search.d_go&q="

obj = "Watch"

driver.get(link+obj)

# root(turnning point)                 /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]
# child(image)                         /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img
# price                                 /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span
# link , name                           /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a

item1 = Product()
item2 = Product()


item1.image = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img')
item2.image = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/a/div/img')

ele1 = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a')
ele2 = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a')

item1.name = ele1
item2.name = ele2

item1.link = ele1.get_attribute('href')
item2.link = ele2.get_attribute('href')

item1.price = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span')
item2.price = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span')

print("--------------------------------Item 1--------------------------------")
print(item1.image.get_attribute('src'))
print(item1.name.text)
print(item1.price.text)
print(item1.link)
print("--------------------------------Item 2--------------------------------")
print(item2.image.get_attribute('src'))
print(item2.name.text)
print(item2.price.text)
print(item2.link)

driver.quit()
