import requests
from bs4 import BeautifulSoup
import csv
import time
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
urls= ["https://www.chinanews.com.cn/scroll-news/news{}.html".format(i) for i in range(1,11)]
for url in urls:
 r = requests.get(url,headers=headers)
 r.encoding='utf-8'
 html= r.text
 r = requests.get(url,headers=headers)
 soup=BeautifulSoup(html,"lxml")
 response = requests.get(url)  
 print(response.encoding)
 news=soup.find(class_="content_list").find("ul").select("li:not([class_='nocontent'])")#"li:not([class_='nocontent'])"#"div",class_="dd_bt"
#print(soup)
#print(news)
 for new in news:
     try:
         name=new.find("div",class_="dd_bt").get_text()
         #此处因为没有缩进导致一直输出none，然后尝试了很多不同的find内容，很费时间！！！！
         time1=new.find('div',class_="dd_time").get_text()
    #print(time)
         newUrl=new.find_all("a")[1].get("href")
    #print("https://www.chinanews.com.cn/"+newUrl)
    #content=new.find('div',class_="left_zw")
         url2="https://www.chinanews.com.cn/"+newUrl
         r2=requests.get(url2,headers=headers)
         r2.encoding='utf-8'
         soup2=BeautifulSoup(r2.text,"html.parser")#这个地方为什么是parser
    #if content.find('div',class_="left_zw") != None:
         content=soup2.find('div',class_="left_zw").get_text() .strip()
    #print(content)
     except:
         pass
     print(name,time1,url2,content)
     listt=[name,time1,url2,content]
     with open("news2.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(listt)
     time.sleep(5)
     #print(name,time1,url2,content)
     
print("ok了爬取完毕！文件写入完毕！")


