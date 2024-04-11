#要求包含排名、电影名、主演、上映时间。
import requests
import re
from bs4 import BeautifulSoup
import csv
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
'cookie': 'HMACCOUNT_BFESS=D0A5F257A347911A; H_WISE_SIDS_BFESS=39996_40038; ZFY=p56zgLMLbwBvlC5DISGrxlssE0cVO5vvd4PVaKwqlbk:C; BAIDUID_BFESS=4D381287C7391F4DE34947A916D39D0A:FG=1; BDUSS_BFESS=Fo5QnJQRkhuQUc4TWZQMHgtUXhBa3dNQ3JycTY1ckVjbzhZM290Y2JoQXA4Q2htRVFBQUFBJCQAAAAAAQAAAAEAAAB4~ZuFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACljAWYpYwFma'}

urls = ["https://www.maoyan.com/board/4?offset={}".format(i) for i in range(0,100,10)]
pattern = re.compile('<i class="board-index board-index-\d+">(.*?)</i>.*?'
                        '<div class="movie-item-info".*?<p class="name">.*?<a href="/films/\d+".*?title="(.*?)".*?data-act="boarditem-click"'
                        '<a href="/films/(.*?)" title=".*?" class="image-link".*?>.*?</a>'
                        '<p class="star">(.*?)</p>.*?'
                        '<p class="releasetime">(.*?)</p>', re.S)
for url in urls:
    content = requests.get(url, headers=headers).text

    #pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?</dd>', re.S)
    #pattern = re.compile('<dd>.*?name.*?a.*?href="(.*?)".*?title="(.*?)".*?</a>.*?star">(.*?).*?releasetime">(.*?).*?</dd>')
    
    rank_matchs=re.findall('<i class="board-index board-index-\d+">(.*?)</i>',content,re.S)
    name_matchs=re.findall('<div class="movie-item-info".*?<p class="name">.*?<a href="/films/\d+".*?title="(.*?)".*?data-act="boarditem-click"',content,re.S)
    link_matchs = re.findall('<a href="/films/(.*?)" title=".*?" class="image-link".*?>.*?</a>', content, re.S)
    star_matchs=re.findall('<p class="star">(.*?)</p>',content,re.S)
    releasetime_matchs=re.findall('<p class="releasetime">(.*?)</p>',content,re.S)
    #print(len(rank_matchs),len(name_matchs),len(link_matchs),len(star_matchs),len(releasetime_matchs))

    for r in range(len(rank_matchs)):
        if r >= len(name_matchs):
        # 电影名列表长度不足，跳过当前迭代或使用默认值
            continue
        rank=rank_matchs[r]
        name=name_matchs[r]
        star=star_matchs[r].strip()[3:]
        releasetime=releasetime_matchs[r].strip()[5:]
        link = 'https://www.maoyan.com/films/' + link_matchs[r]
        print(rank, name,link, star, releasetime)
        listt = [rank, name, link, star, releasetime]
        name = re.sub('\s', '', name)
        star = re.sub('\s', '', star)
        releasetime = re.sub('\s', '', releasetime)
    
        with open('result2.csv', 'a', encoding='utf-8-sig') as f:

            write=csv.writer(f)
            write.writerow(listt)
            time.sleep(2)
'''matches = re.findall(pattern, content)
for match in matches:
        rank, name, star, releasetime = match
        name = re.sub('\s', '', name)
        star = re.sub('\s', '', star)
        releasetime = re.sub('\s', '', releasetime)
        list = [rank, name, star, releasetime]
        print(rank, name, star, releasetime)
        with open('result.csv', 'w', encoding='utf-8') as f:
            write=csv.writer(f)
            write.writerow(list)
            time.sleep(2)
'''