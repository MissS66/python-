import requests
from bs4 import BeautifulSoup
import csv
import time
url="https://www.maoyan.com/board/4"
#要求爬取：排名，电影名，主演，上映时间，评分，剧情简介以及封面图。
#注意：剧情简介是难点，自己先思考尝试。
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
r=requests.get(url,headers=headers)
html=r.text
soup=BeautifulSoup(html,"lxml")
movies=soup.select()