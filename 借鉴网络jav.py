import requests  # 数据请求 第三方模块 pip install requests
import re  # 正则表达式模块
import json  # 序列化与反序列化
import pprint  # 格式化输出模块
import csv  # 保存csv数据
f = open('python招聘数据1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '标题',
    '公司名字',
    '城市',
    '薪资',
    '招聘信息',
    '公司属性',
    '公司规模',
    '企业性质',
    '招聘发布日期',
    '公司详情页',
    '招聘详情页',
])
csv_writer.writeheader() # 写入表头数据
for page in range(1, 11):
    #  1. 发送请求, 对于url地址发送请求
    url = f'https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C090200,000000,0000,00,9,99,python,2,{page}.html'
    # 把python代码进行伪装, 伪装浏览器对服务器发送请求
    # User-Agent 浏览器的基本信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)  # 调用 requests这个模块里面get方法对于 url发送请求
    #  2. 获取数据, 获取服务器发给我们返回的数据响应数据
    # <Response [200]> <> 表示response响应对象 200 状态码 表示请求成功
    # response.text 获取响应体的文本数据(网页源代码)
    # print(response.text)
    # 3. 解析数据, 提取我们想要的数据内容 (比如 招聘标题, 招聘薪资...)
    # 解析方法: re正则表达式, css选择器 xpath  根据服务器返回的数据内容, 选择最适合的解析方式
    # 遇事不决 .*? 元字符 . 可以匹配任意字符串除了换行符以外 * 匹配前一个字符串 0个或者多个 ? 非贪婪匹配模式
    # [] 表示列表
    # {} 可能想到的是字典数据类型
    # .*? 可以匹配任意字符串 除了 换行符\n
    # 通过re模块调用 findall 方法 'window.__SEARCH_RESULT__ = (.*?)</script>' 要匹配的数据内容  response.text从哪里匹配数据 [0] 列表索引取第一个元素
    # 正则表达式详细内容讲解 在VIP课程里面 要讲三个小时左右
    html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text, re.S).split("")[0]
    # print(html_data)
    # print(type(html_data))
    # 把这个字符串数据类型 转成 字典数据类型 通过键值对取值方式提取想要的内容
    json_data = json.loads(html_data)
    # print(type(json_data))
    # 字符串的时候 里面的引号是双引号 字典时候就变成了单引号
    # print(json_data)
    # pprint.pprint(json_data['engine_jds'])
    # 字典取值 根据冒号左边的内容, 提取冒号右边的内容
    # parsel 数据解析
    for index in json_data['engine_jds']:
        # pprint.pprint(index)
        dit = {
            '标题': index['job_name'],
            '公司名字': index['company_name'],
            '城市': index['workarea_text'],
            '薪资': index['providesalary_text'],
            '招聘信息': '|'.join(index['attribute_text']),
            '公司属性': index['companyind_text'],
            '公司规模': index['companysize_text'],
            '企业性质': index['companytype_text'],
            '招聘发布日期': index['issuedate'],
            '公司详情页': index['company_href'],
            '招聘详情页': index['job_href'],
        }
        csv_writer.writerow(dit)
        print(dit)
