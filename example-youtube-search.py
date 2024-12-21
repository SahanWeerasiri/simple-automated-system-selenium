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
# driver.get("https://www.youtube.com")


# # <div class="ytSearchboxComponentInputBox ytSearchboxComponentInputBoxDark"><form action="/results" class="ytSearchboxComponentSearchForm"><input name="search_query" type="text" autocomplete="off" autocorrect="off" aria-autocomplete="list" role="combobox" class="ytSearchboxComponentInput yt-searchbox-input title" placeholder="Search"></form></div>

# # Find the search input box by its class name and enter search term
# input_box = driver.find_element(By.CLASS_NAME, "ytSearchboxComponentInput")
# input_box.send_keys("Ben 10", Keys.ENTER)

# # Wait for search results to load
# time.sleep(2)

# # Find and click the first search result

# first_result = driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer a#video-title")
# url = first_result.get_attribute("href")
url = "https://youtu.be/EgYiFB94a8I"
print(f"Video URL: {url}")

# # Wait to see the result page
# time.sleep(10)

# # Close the browser
# driver.quit()

driver.get("https://www.subeasy.ai/youtube-to-mp4")

# <form data-v-0f75678b="" data-gtm-form-interact-id="0">
#     <div class="mt-14 flex items-center max-w-[800px] mx-auto" data-v-0f75678b="">
#         <div class="relative flex-1 text-lg" data-v-0f75678b="">
#             <input type="text" required="" placeholder="Paste YouTube link here" class="relative block w-full disabled:cursor-not-allowed disabled:opacity-75 focus:outline-none border-0 form-input rounded-md placeholder-gray-400 dark:placeholder-gray-500 text-base p-4 dark:focus:ring-primary-400 shadow-sm bg-[#f7f7f8] dark:bg-gray-900 text-gray-900 dark:text-white ring-0 ring-inset ring-gray-200 dark:ring-gray-700 focus:ring-1 focus:ring-primary" value="https://youtu.be/EgYiFB94a8I" data-gtm-form-interact-field-id="0">
#             <!--[--><!--]--><!----><!---->
#         </div>
#         <button type="submit" class="focus:outline-none focus-visible:outline-0 disabled:cursor-not-allowed disabled:opacity-75 aria-disabled:cursor-not-allowed aria-disabled:opacity-75 flex-shrink-0 font-medium rounded-md text-base gap-x-2.5 px-3.5 shadow-sm text-white dark:text-gray-900 bg-gray-900 hover:bg-gray-800 disabled:bg-gray-900 aria-disabled:bg-gray-900 dark:bg-white dark:hover:bg-gray-100 dark:disabled:bg-white dark:aria-disabled:bg-white focus-visible:ring-inset focus-visible:ring-2 focus-visible:ring-primary-500 dark:focus-visible:ring-primary-400 inline-flex items-center ml-2.5 md:ml-5 justify-center md:min-w-36 py-4" data-v-0f75678b="">
#         <!--[--><!--[--><!----><!--]--><!--[-->Convert <!--]--><!--[--><!----><!--]--><!--]-->
#         </button>
#     </div>
# </form>

input_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Paste YouTube link here']")
input_box.clear()  # Clear any existing text first
input_box.send_keys(url)
btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # More reliable selector
btn.click()
time.sleep(10)

# <div data-v-0f75678b="" class="p-3 bg-white rounded-lg cursor-pointer flex-1 text-center flex items-center justify-center min-w-24 max-w-32 mr-2.5 mb-2.5"><!----><span data-v-0f75678b="">360P</span><!----></div>

# quality = driver.find_elements(By.CSS_SELECTOR, "p-3 bg-white rounded-lg cursor-pointer flex-1 text-center flex items-center justify-center min-w-24 max-w-32 mr-2.5 mb-2.5")
# quality[0].click()

# print("Quality selected")

# try:
#     # Find the quality selector div that contains "360P" text
#     quality = driver.find_elements(By.CSS_SELECTOR, "div.rounded-lg span")
#     quality = [q.find_element(By.XPATH, "..") for q in quality if q.text == "360P"]
# except:
#     try:
#         # Alternative XPATH approach
#         quality = driver.find_elements(By.XPATH, "//div[contains(@class, 'rounded-lg')]//span[text()='360P']/parent::div")
#     except:
#         print("Could not find quality selector")
#         quality = []
# print(len(quality))
# quality[0].click()


# time.sleep(10)

driver.quit()
