#将收集到的电影信息保存到Excel文件中
import pandas as pd
import requests
import json

#将爬取的数据保存到Excel文件中
def save_data_to_excel(data, filename='movies_data.xlsx'):
    """
    :param data: 要保存的数据列表，每个元素是一个包含电影信息的字典。
    :param filename: Excel文件的名称。
    """
    # 将数据转换为DataFrame
    df = pd.DataFrame(data)
    # 保存DataFrame到Excel，确保安装了openpyxl
    df.to_excel(filename, index=False, engine='openpyxl')
    print(f"数据已保存到{filename}")

# 生成豆瓣电影网址列表。
def generate_douban_urls(start, end, step):
    """
    :param start: 起始值
    :param end: 终止值
    :param step: 每次递增的步长
    :return: 生成的网址列表
    """
    base_url = "https://movie.douban.com/j/chart/top_list?type=18&interval_id=100%3A90&action=&start={}&limit=20"
    urls = [base_url.format(i) for i in range(start, end, step)]
    return urls

## 解析获取到的json数据
def parse_movie_data(movie_data):
    """
    从电影数据中解析title、url和score。
    
    :param movie_data: 单部电影的数据
    :return: 解析后的数据
    """
    title = movie_data.get('title')
    url = movie_data.get('url')
    score = movie_data.get('score')
    return title, url, score

#从给定的URL列表中爬取数据。
def fetch_data_from_urls(urls):
    movies_data = []  # 初始化空列表以收集电影数据
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movies_json = response.json()
            for movie in movies_json:
                # 使用parse_movie_data函数解析数据
                title, url, score = parse_movie_data(movie)
                movies_data.append({'title': title, 'url': url, 'score': score})
        else:
            print(f"请求失败，状态码：{response.status_code}")
            
    # 在完成所有请求后保存数据到Excel
    save_data_to_excel(movies_data)

#运行程序
urls = generate_douban_urls(0, 60, 20)  
fetch_data_from_urls(urls)