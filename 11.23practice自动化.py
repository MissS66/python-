from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
el=driver.find_element(By.ID,'kw')
el.send_keys('淘宝')
em=driver.find_element(By.ID,'su').click()
sleep(2)
driver.switch_to.window(driver.window_handles[-1]) # 转移到选项卡为-1窗口
#em.get('driver.current_url')
er=driver.find_element(By.ID,'kw')
er.send_keys('评价')
en=driver.find_element(By.ID,'su').click()
sleep(2)
driver.back()
#title=bt.titleurl=bt.current_url
#print(title.url)
#ul=driver.find_element(By.CLASS,'wbrjf67').click()
#bt.find_element(BY.CLASS,'wbrjf67').click
#bt.find_element(BY.TAG_NAME,'a href').click()
#bt.find_element(BY.)
sleep(2)
ul=driver.find_element(By.XPATH,'//*[@id="3001"]').click()
sleep(8)
driver.switch_to.window(driver.window_handles[-1]) # 转移到选项卡为-1窗口
ed=driver.find_element(By.NAME,'key')
ed.send_keys('牛奶')
ea=driver.find_element(By.XPATH,'//*[@id="J_searchForm"]/input').click()
sleep(8)
driver.quit()