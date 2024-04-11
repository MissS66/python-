#将收集到的电影信息保存到csv文件中
import requests
import json
import csv

#写入csv函数
def save_data_to_csv(data, filename='movies_data.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Score', 'URL'])
        for movie in data:
            writer.writerow([movie['title'], movie['score'], movie['url']])
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
    all_movies_data = []  # 初始化列表以收集所有电影数据
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movies_data = response.json()
            for movie in movies_data:
                title, url, score = parse_movie_data(movie)
                all_movies_data.append({'title': title, 'url': url, 'score': score})
        else:
            print(f"请求失败，状态码：{response.status_code}")
    
    # 在完成所有请求后，将数据保存到CSV文件
    save_data_to_csv(all_movies_data)

#运行程序
urls = generate_douban_urls(0, 60, 20)  
fetch_data_from_urls(urls)