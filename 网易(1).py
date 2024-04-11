from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import csv
from bs4 import BeautifulSoup
#网易新闻标题，时间，正文
driver=webdriver.Chrome()
driver.get("https://news.163.com")
time.sleep(4)
driver.maximize_window()
js='window.scrollTo(0, 10000);'
# 使用execute_script方法执行JavaScript代码来实现鼠标滚动
driver.execute_script(js) # 向下滚动 10000 像素
time.sleep(5)
content=driver.page_source
#print(content)
soup=BeautifulSoup(content,'lxml')
#print(soup)
alist=soup.find('li',class_="newsdata_item current")
#print(alist)
newss=alist.find(class_="hidden")
news=newss.find_all('div','a')
for new in news:
    newurl=new.find('a').get("href")
    print(newurl)
    '''driver.get(newurl)
    time.sleep(1)
    content2=driver.page_source
    #print(content2)
    soup2=BeautifulSoup(content2,'lxml')
    #print(soup2)
    title=soup2.find(class_="post_title").get_text()
    print(title)
    date=soup2.find(class_="post_info").get_text()
    print(date)
    passage=soup2.find(class_="post_body").get_text()
    print(passage)
    listt=[title,date,passage]
    with open("wangyi.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(listt)'''
driver.quit()