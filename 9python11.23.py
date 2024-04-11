# 导入selenium模块
#webdrive是selenium模块中的一个个子模块，其取代了嵌入到
# 被测试Web应用中的JavaScript，与浏览器的紧密集成支持创建更高级的测试，
# 避免了JavaScript安全模型导致的限制。
# Webdriver接收到代码后，经过处理来发送给浏览器，
# 浏览器根据处理后的代码执行对应的操作，浏览器执行后完把执行结果返回
# 给Webdriver，Webdriver将执行结果处理并返回给代码展示出来。

from selenium import webdriver
from time import sleep
#记住头文件的导入格式
from selenium.webdriver.common.by import By
# 启动浏览器驱动，浏览器名首字母需要大写且后面加括号。
driver=webdriver.Chrome()
# 访问url
driver.get('https://www.baidu.com')
# 定位元素，我们有八种元素定位的方法：id、name、class、tag_name、
# xpath、css_selector、link_text、partial_link_text。
el=driver.find_element(By.ID,'kw')#ctrl+f查找，看所选元素是否唯一
#在一般情况下，页面源码中的id都是唯一的，所以只要知道页面元素中的id，
# 就可以定位到该元素，但name、class值可以有重复，所以要注意页面元素中的
#name、class值有没有重复，假如有的话，selenium默认会返回第一个name或class的元素，假设有如下页面元素标签：
#示例页面元素标签：<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
#from selenium.webdriver.common.by import By
#driver.find_element(By.TAG_NAME,"input")
# 或
#driver.find_element('tag name',"input")
#这样就可以定位到input标签了。
#xpath定位:1.nodename-获取该节点的所有子节点。2./-从当前节点获取直接子节点
#3.//-从当前节点获取子孙节点。4.*-获取当前节点。5.**-获取当前节点的父节点
#5.@-选取属性。6.[]-添加筛选条件。eg://title[@lang='eng']其表示选择所有名称为title，同时属性lang的值为eng的节点。
#语法格式：driver.find_element('xpath',"xpath规则")
#网页的检查复制中可以复制xpath
# 执行自动化操作
el.send_keys('淘宝')
bt=driver.find_element(By.ID,'su').click()
# 休眠5秒
sleep(5)
# 关闭浏览器并释放进程资源
driver.quit()
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/zh-cn/documentation/webdriver/interactions/alerts/")
driver.find_element('link text','查看样例警告框').click()
sleep(5)
alert = driver.switch_to.alert
alert.accept()
sleep(5)
driver.find_element('link text','查看样例警告框').click()
