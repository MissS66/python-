from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import csv
from bs4 import BeautifulSoup
#虎扑咨询标题，时间，正文
start_url="https://www.hupu.com/"
driver=webdriver.Edge()
driver.get(start_url)
time.sleep(40)

content=driver.page_source
#print(content)
soup=BeautifulSoup(content,'lxml')
#print(soup)
alist=soup.find(class_="test-img-list-model infinite-container")
#print(alist)
#newpcnews=driver.find_element(By.XPATH,'//*[@id="newpcnews-1"]')
#el=driver.find_element(By.ID,'kw')
#print(newcpnews)
for i in range(1,299):
    newpcnews=alist.find(id="newpcnews-{}".format(i))
    i=i+1
    #print(newpcnews)
    newurl=newpcnews.find(class_="list-item-title").get("href")
    #print(newurl)
    driver.get(newurl)
    time.sleep(1)
    content2=driver.page_source
    #print(content2)
    soup2=BeautifulSoup(content2,'lxml')
    #print(soup2)
    title=soup2.find(class_="index_name__M5qqs").get_text()
    print(title)
    date=soup2.find(class_="post-user_post-user-comp-info-top-time__k9K2U").get_text()
    print(date)
    passage=soup2.find(class_="thread-content-detail").get_text()
    print(passage)
    print("第{}个爬取完成！".format(i-1))
    listt=[title,date,passage]
    with open("hupu.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(listt)