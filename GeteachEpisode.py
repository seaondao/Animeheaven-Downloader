from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



user_input = input("GIve me the Anime url")
Animename = str(input("Name you want to save as: "))
chrome_option = Options()

chrome_option.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_option)

#Use default wile testing
# default = "https://animeheaven.me/anime.php?22bkm"

driver.get(str(user_input)) #This should be in put of the website.

#Get all of the episodes's url 
atags = driver.find_elements(By.CSS_SELECTOR,".linetitle2 a")
episodes =[]
for a in atags:
    episodes.append(a.get_attribute("href"))
episodes.reverse()

# print(episodes)

videos = []
for epi in episodes:
    driver.get(epi)
    h1element = driver.find_element(By.CSS_SELECTOR,"h1")#Original h1 to use later
    fullname = h1element.text

    dic= {
    "src":driver.find_element(By.CSS_SELECTOR,"video source").get_attribute('src'),
    "fullname": h1element.text,
    "episodeNum":fullname.replace(h1element.find_element(By.TAG_NAME,"a").text,"").strip()
    }
    videos.append(dic)

driver.quit()

with open("test.txt","w") as file:
    file.write(str(videos))

# filename = "test2.csv"
# with open(filename,'w') as file:
#     file.write(str(videos))
