from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import csv
from bs4 import BeautifulSoup
#标题、发布时间、点赞量、收藏量（前500个）
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
start_url="https://www.bilibili.com/v/popular/all/"
driver=webdriver.Chrome()
driver.get(start_url)
driver.encoding='utf-8'
time.sleep(4)  
driver.maximize_window()
for x in range(25):
    js=f'window.scrollTo({10000*x}, {10000*(x+1)});'
# 使用execute_script方法执行JavaScript代码来实现鼠标滚动
    driver.execute_script(js) # 向下滚动 10000 像素
    time.sleep(2)
content=driver.page_source
#print(content)
soup=BeautifulSoup(content,'lxml')
#print(soup)
alist=soup.find(class_="flow-loader")
news=alist.find_all(class_='video-card')
#print(news)
for new in news:
  try:
    newurl=new.find('a',target="_blank").get("href")
    #print(newurl)
    url2="https:"+newurl
    r2=requests.get(url2,headers=headers)
    r2.encoding='utf-8'
    soup2=BeautifulSoup(r2.text,"html.parser")
    title=soup2.find('h1',class_="video-title").get_text() .strip()
    #print(title)
    atime=soup2.find('span',class_="pubdate-text").get_text().strip()
    #print(time)
    agree=soup2.find('span',class_="video-like-info video-toolbar-item-text").get_text().strip()
    shoucang=soup2.find('span',class_="video-fav-info video-toolbar-item-text").get_text().strip()
    time.sleep(1)
  except:
    pass
  print(title,atime,agree,shoucang)
  listt=[title,atime,agree,shoucang]
  with open("Bzhano2~.csv","a+",newline='',encoding="utf-8-sig") as f:
    write=csv.writer(f)
    write.writerow(listt)
print("爬取完毕！")
driver.quit()