from douban_movie_crawler import generate_douban_urls
  
# 生成豆瓣电影网址列表  
urls = generate_douban_urls(0, 60, 20)  
  
print(urls)