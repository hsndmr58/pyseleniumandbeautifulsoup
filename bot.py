from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
import random
senin_ben_yolunu="D:\chromedriver\chromedriver.exe"
kitle="Happiness İst."
browser = webdriver.Chrome(executable_path=senin_ben_yolunu)
browser.maximize_window()
browser.get('https://www.trendyol.com/butik/liste/kadin?pi=29')
sleep(2)
soup=BeautifulSoup(browser.page_source, 'html.parser')
veri=[td.text for td in soup.findAll('span', class_='name')]
deneme=str(soup)
ths=open("veri.txt","w",encoding="utf-8")
ths.write(deneme)
ths.close()
anu=0
yakala=""
say=0
virüs=0
print(veri)
# '//*[@id="browsing-gw-homepage"]/div/div[2]/div[2]/article[605]/a/span/img'
# '//*[@id="browsing-gw-homepage"]/div/div[2]/div[2]/article[602]/a/span/img'
# '//*[@id="browsing-gw-homepage"]/div/div[2]/div[2]/article[1]/a/span/img'
while anu<len(veri):
    if(veri[anu]==kitle):
        say=anu+1
    if(say<=19):
        yakala='//*[@id="browsing-gw-homepage"]/div/div[2]/div[1]/div[1]/article['+str(say)+']/a/span/img'
    if(say>19):
        yakalasay=say-20
        yakala='//*[@id="browsing-gw-homepage"]/div/div[2]/div[2]/article['+str(yakalasay)+']/a/span/img'
    anu+=1
sleep(2)
while virüs<50:
    
    # if(virüs!=0 and virüs%5==0):
    #     sleep(2)
    #     browser.get("http://192.168.1.1/login.html")
    #     sleep(2)
    #     browser.find_element_by_id('login-username').send_keys('admin')
    #     sleep(2)
    #     browser.find_element_by_id('login-password').send_keys('admin')
    #     sleep(2)
    #     browser.find_element_by_id('submit').click()
    #     sleep(2)
    #     browser.get("http://192.168.1.1/resetroute.html")
    #     sleep(1)
    #     browser.find_element_by_id('btnReboot').click()
    #     sleep(150)
    #     try:
    #         browser.get("https://www.trendyol.com/butik/liste/kadin?pi=29")
    #         sleep(4)
    #     except:
    #         sleep(10)
    #         browser.get("https://www.trendyol.com/butik/liste/kadin?pi=29")


    browser.get('https://www.trendyol.com/butik/liste/kadin?pi=29')
    sleep(2)
    bnrbtn= browser.find_element_by_xpath(yakala).click()
    sleep(4)
    degisken=random.randint(1,20)
    print(degisken)
    
    
    sleep(3)
    try:
        bnrbtn= browser.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div['+str(degisken)+']/div[1]/a/div[1]/div/img').click()
    except:
        sleep(2)
        bnrbtn= browser.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]').click()
        sleep(2)
        bnrbtn= browser.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div['+str(degisken)+']/div[1]/a/div[1]/div/img').click()
    sleep(2)
    virüs+=1
