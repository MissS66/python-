import requests
from bs4 import BeautifulSoup
import csv
import time
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
urls = ["https://movie.douban.com/top250?start={}&filter=".format(i) for i in range(0,250,25)]
for url in urls:
    r = requests.get(url,headers=headers)
    html= r.text
r=requests.get(url,headers=headers)
html=r.text
soup=BeautifulSoup(html,"lxml")
movies=soup.select('ol li')
for movie in movies:
    rank=movie.find(name='em').get_text()
    filmname=movie.find(name="span",class_='title').get_text()
    star=movie.find_all("p")[0].text.strip()
    score=movie.find('span',class_="rating_num").get_text()
    if movie.find('span',class_="inq") != None:
            evaluate = movie.find("span",class_ = "inq").get_text()      #描述
    else:
            evaluate = "none"
    try:
        star_split=star.split("主演:")
        director=star_split[0][4:]
        performer=star_split[1].split("\n")[0][1:]
        times=star_split[1].split("\n")[1].split("/")[0].strip()
        country=star_split[1].split("/")[-2].strip()
        kind=star_split[1].split("/")[-1].strip()
    except: 
        try:   
            star_split=star.split("主")
            director=star_split[0][4:]
            performer=star_split[1].split("\n")[0][1:]
            times=star_split[1].split("\n")[1].split("/")[0].strip()
            country=star_split[1].split("/")[-2].strip()
            kind=star_split[1].split("/")[-1].strip()
        except:  
            pass
    filmUrl=movie.find("a").get("href")
    r2=requests.get(filmUrl,headers=headers)
    soup2=BeautifulSoup(r2.text,"html.parser")#这个地方为什么是parser
    if soup2.find("span",class_="all hidden") != None:
        jianjie=soup2.find("span",class_="all hidden").get_text() .strip()
        print(jianjie)
    else:
        jianjie=soup2.find("span",property="v:summary").get_text() .strip()
        print(jianjie)
    pic=movie.find(name='img').get('src')
    path = filmname+".jpg"
    pic_r = requests.get(pic)
    with open(path,"wb") as f:
        f.write(pic_r.content)
    print(rank,filmname,director,performer,times,country,kind,score,evaluate,jianjie)
    content=[rank,filmname,director,performer,times,country,kind,score,evaluate,jianjie]
    with open("movies.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(content)
    time.sleep(2)
print("爬取完毕！文件写入完毕！")
