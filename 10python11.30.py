from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
# 实例化对象
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])# 开启实验性功能
# 去除特征值
option.add_argument("--disable-blink-features=AutomationControlled")
# 实例化谷歌
driver = webdriver.Chrome(options=option)
# 修改get方法
script = '''object.defineProperty(navigator,'webdriver',{undefinedget: () => undefined})'''
#execute_cdp_cmd用来执行chrome开发这个工具命令
driver.execute_cdp_cmd("page.addscriptToEvaluateonNewDocument",{"source": script})
driver.get('https://www.baidu.com')
sleep(5)
driver.quit()