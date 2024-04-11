from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import csv
import undetected_chromedriver as uc
driver = uc.Chrome(use_subprocess=True)
driver=webdriver.Chrome()
driver.get('https://www.51job.com/')
driver.maximize_window()
blk=driver.find_element(By.XPATH,'//*[@id="kwdselectid"]')
blk.send_keys("大数据")
so=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/button').click()
sleep(15)
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
jobs=driver.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div')#'/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]')
for i in range(1,11):
 jobNames = [driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[{i}]/div[2]').format(i) for i in range(1,21)].text.strip()
 for jobname in jobNames:
  try:
    jobname=jobName.split(" ")#.strip()
    #print(jobname)
    jname=jobname[0].split("\n")[0]
    gname=jobname[0].split("\n")[4]
    prize=jobname[0].split("\n")[2]
    sleep(1)#print(jname)#print(gname)#print(prize)
    cent=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]').click()
    driver.switch_to.window(driver.window_handles[-1])
    sleep(5)
    jobcontent=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[1]/div').text.strip()#print(jobcontent)
    sleep(2)
    driver.close()
  except:
    pass
  print(jname,gname,prize,jobcontent)
  listt=[jname,gname,prize,jobcontent]
  with open("人才网大数据岗位11/30.csv","a+",newline='',encoding="utf-8-sig") as f:
        write=csv.writer(f)
        write.writerow(listt)
 driver.switch_to.window(driver.window_handles[0])#可有可无
 try:
    next=driver.find_element(By.CLASS_NAME,'btn-next')
    next.click()
 except:
    next=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[3]')
    next.click()#driver.switch_to.window(driver.window_handles[-1])
sleep(2)
driver.quit()
