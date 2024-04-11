from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import csv
driver=webdriver.Edge()
def load_cookies(driver):
    driver.maximize_window()
    driver.get("https://sc.ecosports.cn/positionList?type_id=26")
    
    with open("cookies.txt", encoding="utf8") as f:
        cookies = json.loads(f.read())
        for cookie in cookies:
            driver.add_cookie(cookie)
    
    driver.refresh()
    time.sleep(5)
load_cookies(driver)
driver.refresh()
sleep(2)
#import undetected_chromedriver as uc
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
#driver = uc.Edge(use_subprocess=True)
driver.get("https://sc.ecosports.cn/positionList?type_id=26")
#driver.get("https://www.baidu.com")
driver.maximize_window()
sleep(5)
'''blk=driver.find_element(By.XPATH,'//*[@id="kwdselectid"]')
blk.send_keys("大数据")
so=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/button').click()
sleep(5)
driver.switch_to.window(driver.window_handles[-1])'''
for i in range(1,13):
    sleep(3)
    content=driver.page_source
    #print(content)
    soup=BeautifulSoup(content,'lxml')
    #print(soup)
    joblist=soup.find(class_='position-list-wrapper')
    print(joblist)
    joblists=joblist.find_all('li',class_="clearfix")
    #print(joblists)
    for joblistt in joblists:
      try:  
        '''jobname=joblistt.find(class_='name').get_text()
        #print(jobname)'''
        gsname=joblistt.find(class_='company-name').get_text()
        #print(gsname)
        '''prize=joblistt.find(class_='sal shrink-0').get_text()
        #print(prize)
        content=joblist.find(class_='d text-cut').get_text()'''
        newUrl=joblistt.find_all("a")[0].get("href")
        r2=requests.get(newUrl,headers=headers)
        r2.encoding='utf-8'
        soup2=BeautifulSoup(r2.text,"html.parser")
        jobname=soup2.find('h1',class_='positioin-name').get_text() .strip()
        prize=soup2.find('div',class_='other clearfix').get_text() .strip()
        content=soup2.find('div',class_='descript-con').get_text() .strip()

      except:
        pass
      print(jobname,gsname,prize,content)
      listt=[jobname,gsname,prize,content]
      with open("shangcang.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(listt)
    try:
        next=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/button[2]')
        next.click()
    except:
        next=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/button[2]/i')
        next.click()#driver.switch_to.window(driver.window_handles[-1])
    print("第{}页爬取完毕".format(i))

sleep(2)
driver.quit() 