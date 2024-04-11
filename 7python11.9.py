'''import requests
from bs4 import BeautifulSoup
r = requests.head('http://httpbin.org/get')
print(r.headers)
print(r.text)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data = payload)
print(r.text)'''

'''
r=requests.get("https://item.jd.com/100009177424.html",headers={"user-agent":"Mozilla/5.0"})
r.encoding=r.apparent_encoding
print(r.text[:1000])'''

'''
import requests
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000'
}   #自定义一个请求头，使用字典的形式。

url="http://www.baidu.com/s?wd={}"

keywords = input("请输入要搜索的关键字：")

r = requests.get(url.format(keywords),headers=headers)    #在这里调用自定义的请求头
print(r.status_code)    #输出状态码
r.encoding="utf-8"
print(r.text)'''

import requests

url="http://www.baidu.com/s?"   #记得要把wd去掉

keywords = input("请输入要搜索的关键字：")

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36 Maxthon/5.3.8.2000'
}   #自定义一个请求头，使用字典的形式。

params = {"wd":keywords}

r = requests.get(url,headers=headers,params=params)    #在这里调用自定义的请求头

#print(r.status_code)    #输出状态码
r.encoding="utf-8"

print(r.request.url)

#print(r.text)

