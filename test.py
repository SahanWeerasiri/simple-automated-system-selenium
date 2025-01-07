# Import required modules from selenium and time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome webdriver service using local chromedriver.exe
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.eporner.com/")

#print(hrefs)
def download_video(href):
    driver.get(href)

    # <span class="uvmspn7" onclick="EP.video.checkDownloadAV1();" data-menutype="downloaddiv"><i>Download</i></span>
    download_btn = driver.find_element(By.CLASS_NAME, 'uvmspn7')
    # Click the download button using JavaScript since it has an onclick handler
    driver.execute_script("arguments[0].click();", download_btn)

    # Find all download links
    download_links = driver.find_elements(By.CSS_SELECTOR, '.download-h264 a')
    # Get the highest quality download link (last one)
    download_link = download_links[-1] if download_links else None
    print(download_link.get_attribute('href'))

    driver.get(download_link.get_attribute('href'))

# <input type="text" id="srch" name="search" value="" onblur="EP.search.blur()" onkeyup="EP.search.keyUp(event)" autocomplete="off" autofocus="">

input_box = driver.find_element(By.NAME, "search")
input_box.clear()  # Clear any existing text first
input_box.send_keys("Alina lopez", Keys.ENTER)

# <div id="vidresults">
# <div class="ad300px"><div class="ad300px-inner"><div class="homeadiframe" id="homeadiframe1"><span class="adstext">Advertisement</span><iframe width="300" height="250" frameborder="0" marginheight="0" marginwidth="0" scrolling="no" src="//tsyndicate.com/iframes2/c12ce8284fbc43d0a9959abcddfb487c.html?keywords=alina%2Clopez%2CWatch%20Alina%20Lopez%20hd%20porn%20videos%20for%20free%20on%20Eporner.com.%20We%20have%20925%20videos%20with%20Alina%20Lopez%2CAlina%20Lopez%20Anal%2CAlina%20Lopez%20Lesbian%2CAlina%20Lopez%20Pov%2CAlina%20Lopez%20Creampie%2CAlina%20Lopez%20Blowjob%2CAlina%20Lopez%20Threesome%2CAlina%20Lopez%20Hardcore%2CAlina%20Lopez%20Step%2CAlina%20Lopez%20Compilation%2CAlina%20Li%20in%20our%20database%20available%20for%20free.%2CAlina%20Lopez%2CAlina%20Lopez%20Anal%2CAlina%20Lopez%20Lesbian%2CAlina%20Lopez%20Pov%2CAlina%20Lopez%20Creampie%2CAlina%20Lopez%20Blowjob%2CAlina%20Lopez%20Threesome%2CAlina%20Lopez%20Hardcore%2CAlina%20Lopez%20Step%2CAlina%20Lopez%20Compilation%2CAlina%20Li%2CAlina%20Lopez%20Porn%20-%20Alina%20Lopez%20Anal%20%26%20Alina%20Lopez%20Lesbian%20Videos%20-%20EPORNER&amp;adb=0&amp;clientjs=1&amp;w=1920&amp;h=1080&amp;tz=%2D330"></iframe></div></div></div>
# <div class="mb hdy" data-id="2011707" data-vp="2011707|0|2" id="vf2011707"><div class="mbimg"><div class="mbcontent"><a href="/hd-porn/v6wwu8ToBdV/Really-Nice-Pussy-Fucking/"><img src="https://static-sg-cdn.eporner.com/thumbs/static4/2/20/201/2011707/5_240.jpg" data-st="2011707|5|0" alt="Really Nice Pussy Fucking"></a><div class="mvhdico" title="Quality"><span>1080p</span></div></div></div><div class="mbunder"><p class="mbtit"><a href="/hd-porn/v6wwu8ToBdV/Really-Nice-Pussy-Fucking/">Really Nice Pussy Fucking - Alina Lopez</a></p><p class="mbstats"><span class="mbtim" title="Duration">23:45</span><span class="mbrate" title="Rating">88%</span><span class="mbvie" title="Views">139,848</span></p></div></div>
# <div class="mb" data-id="2545668" data-vp="2545668|0|2" id="vf2545668"><div class="mbimg"><div class="mbcontent"><a href="/hd-porn/giocRfREfqU/Outdoor-Sex-With-A-Sex-Mate-Her/"><img src="https://static-sg-cdn.eporner.com/thumbs/static4/2/25/254/2545668/9_240.jpg" data-st="2545668|9|0" alt="Outdoor Sex With A Sex Mate Her"></a><div class="mvhdico" title="Quality"><span>720p</span></div></div></div><div class="mbunder"><p class="mbtit"><a href="/hd-porn/giocRfREfqU/Outdoor-Sex-With-A-Sex-Mate-Her/">Outdoor Sex With A Sex Mate Her</a></p><p class="mbstats"><span class="mbtim" title="Duration">3:04</span><span class="mbrate" title="Rating">85%</span><span class="mbvie" title="Views">121,669</span><span class="mb-uploader"><a href="/profile/z8jp2jeucw/" title="Uploader">z8jp2jeucw</a></span></p></div></div>

# Extract all hrefs from the video links
hrefs = []
video_links = driver.find_elements(By.CSS_SELECTOR, 'div.mbcontent a[href*="/video-"]')
for link in video_links:
    href = link.get_attribute('href')
    hrefs.append(href)

for href in hrefs[:10]:
    download_video(href)

driver.quit()
