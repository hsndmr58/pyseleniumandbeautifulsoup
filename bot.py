from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import pyautogui
senin_ben_yolunu="D:\\chromedriver\chromedriver.exe"
kitle="Sağlık Ürünlerinde Kaçmaz Fırsat"
browser = webdriver.Chrome(executable_path=senin_ben_yolunu)
browser.get('https://www.trendyol.com/butik/liste/kadin')
sleep(2)
soup=BeautifulSoup(browser.page_source, 'html.parser')
veri=[td.text for td in soup.findAll('span', class_='name')]
deneme=str(soup)
ths=open("veri.txt","w",encoding="utf-8")
ths.write(deneme)
ths.close()
anu=0
say=0
virüs=0
while anu<19:
    if(veri[anu]==kitle):
        say=anu+1
    anu+=1
sleep(4)
while virüs<50:
    if(virüs!=0 and virüs%5==0):
        sleep(2)
        browser.get("http://192.168.1.1/login.html")
        sleep(2)
        browser.find_element_by_id('login-username').send_keys('admin')
        sleep(2)
        browser.find_element_by_id('login-password').send_keys('admin')
        sleep(2)
        browser.find_element_by_id('submit').click()
        sleep(2)
        browser.get("http://192.168.1.1/resetroute.html")
        sleep(1)
        browser.find_element_by_id('btnReboot').click()
        sleep(150)
        try:
            browser.get("https://www.trendyol.com/butik/liste/kadin")
            sleep(4)
        except:
            sleep(10)
            browser.get("https://www.trendyol.com/butik/liste/kadin")


    browser.get('https://www.trendyol.com/butik/liste/kadin')
    sleep(2)
    bnrbtn= browser.find_element_by_xpath('//*[@id="browsing-gw-homepage"]/div/div[2]/div[1]/div[1]/article['+str(say)+']/a/span/img').click()
    sleep(4)
    virüs+=1