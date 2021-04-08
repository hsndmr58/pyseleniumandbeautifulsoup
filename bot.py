from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import pyautogui
import random
an=datetime.now()
senin_ben_yolunu="D:\chromedriver\chromedriver.exe"
kitle="Happiness İst."
browser = webdriver.Chrome(executable_path=senin_ben_yolunu)
browser.maximize_window()
browser.get('https://www.trendyol.com/butik/liste/kadin?pi=29')
sleep(2)
soup=BeautifulSoup(browser.page_source, 'html.parser')
veri=[td.text for td in soup.findAll('span', class_='name')]
deneme=str(soup)
# ths=open("veri.txt","w",encoding="utf-8")
# ths.write(deneme)
# ths.close()
anu=0
yakala=""
say=0
virüs=0
banner=0

while banner<len(veri):
    print(str(banner)+" "+veri[banner])
    banner+=1
while anu<len(veri):
    if(veri[anu]==kitle):
        say=anu+1  
    if(say<=19):
        yakala='//*[@id="browsing-gw-homepage"]/div/div[2]/div[1]/div[1]/article['+str(say)+']/a/span/img'
        
    if(say>19):
        yakalasay=say-20
        yakala='//*[@id="browsing-gw-homepage"]/div/div[2]/div[2]/article['+str(yakalasay)+']/a/span/img'


    anu+=1
rpr=open("sira.txt","a",encoding="utf-8")
rpr.write(str(an.month)+".Ay "+str(an.day)+".Gün Rakip "+str(say)+". Sırada\n")
rpr.close()
sleep(2)
while virüs<50:
    if(virüs!=0 and virüs%5==0):
        print("Modeme Reset Atılıyor...")
        # sleep(2)
        # browser.get("http://192.168.1.1/login.html")
        # sleep(2)
        # browser.find_element_by_id('login-username').send_keys('admin')
        # sleep(2)
        # browser.find_element_by_id('login-password').send_keys('admin')
        # sleep(2)
        # browser.find_element_by_id('submit').click()
        # sleep(2)
        # browser.get("http://192.168.1.1/resetroute.html")
        # sleep(1)
        # browser.find_element_by_id('btnReboot').click()
        # sleep(150)
        # try:
        #     browser.get("https://www.trendyol.com/butik/liste/kadin?pi=29")
        #     sleep(4)
        # except:
        #     sleep(10)
        #     browser.get("https://www.trendyol.com/butik/liste/kadin?pi=29")


    browser.get('https://www.trendyol.com/butik/liste/kadin?pi=29')
    sleep(2)
    bnrbtn= browser.find_element_by_xpath(yakala).click()
    sleep(4)
    degisken=random.randint(1,20)
    print(degisken)
    sleep(3)
    browser.refresh()
    sleep(2)
    bnrbtn = browser.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div['+str(degisken)+']/div[1]/a/div[1]/div/img').click()
    sleep(2)
    virüs+=1
