# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:09:08 2024

@author: USER
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

url = "https://www.kkday.com/zh-tw/city/tokyo"

driver = webdriver.Chrome()

driver.get(url)

time.sleep(2)
x=0
y=400
for i in range(1):
    driver.execute_script('window.scrollTo({},{})'.format(x,y))
    time.sleep(2)    
    y+=1000


topData = driver.find_element(By.ID,'splide04')
print(topData.text)

driver.close()

# for row in topData:
#     print(row.text)
    
#     print('-'* 30)


