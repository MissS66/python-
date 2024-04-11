#将收集到的电影信息保存到csv文件中
import requests
import json
import csv
#链接https://movie.douban.com/chart
#右侧分类排行榜某一分类电影的所有结果,包含电影名称、网址、评分、国别、发布时间等内容。
#rank,title, url, score, regions, release_date, actors
#写入csv
def save_data_to_csv(data, filename='ooaction_movies_data.csv'):
#它的第一个参数是文件名 filename，第二个参数 mode 指定了文件的打开模式。
#在这里，mode='w' 表示以写入模式打开文件，如果文件不存在则创建新文件，如果文件已存在则清空文件内容重新写入。
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank','Title', 'URL','Score','Regions','Release_date','Actors'])
        for movie in data:
            writer.writerow([movie['rank'],movie['title'], movie['url'], movie['score'], movie['regions'], movie['release_date'], movie['actors']])
#f-string 是一种方便的字符串格式化方法，用于在字符串中插入变量的值
    print(f"数据已保存到{filename}")

#生成豆瓣电影网址列表的函数。
def generate_douban_urls(start, end, step):
    """
    :param start: 起始值
    :param end: 终止值
    :param step: 每次递增的步长
    :return: 生成的网址列表
    """
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit=20"
    urls = [base_url.format(i) for i in range(start, end, step)]
    return urls

#解析获取到的json数据的函数
def parse_movie_data(movie_data):
    """
    从电影数据中解析rank、title、url、score、
    regions、release_data、actors。
    :param movie_data: 单部电影的数据
    :return: 解析后的数据
    """
    rank=movie_data.get('rank')
    title = movie_data.get('title')
    try:
        url = movie_data.get('url')
    except:
        pass
    score = movie_data.get('score')
    regions=movie_data.get('regions')
    release_date=movie_data.get('release_date')
    actors=movie_data.get('actors')
    return rank,title, url, score, regions, release_date, actors

#从给定的URL列表中爬取数据函数。
def fetch_data_from_urls(urls):
    all_movies_data = []  # 初始化列表以收集所有电影数据
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movies_data = response.json()
            for movie in movies_data:
                rank,title, url, score,regions,release_date,actors = parse_movie_data(movie)
                all_movies_data.append({'rank':rank,'title': title, 'url': url, 'score': score,'regions':regions,'release_date':release_date,'actors':actors})
        else:
            print(f"请求失败，状态码：{response.status_code}")

#在完成所有请求后，将数据保存到CSV文件
    save_data_to_csv(all_movies_data)

#运行程序
if __name__ == "__main__": 
    urls = generate_douban_urls(0, 20, 20)  
    fetch_data_from_urls(urls)
