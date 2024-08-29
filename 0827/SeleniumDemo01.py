# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:02:43 2024

@author: USER
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

url = "https://www.kkday.com/zh-tw/city/tokyo"

driver = webdriver.Chrome()

driver.get(url)

topTen = driver.find_element(By.CSS_SELECTOR,'.splide__slider')

li_elements = topTen.find_elements(By.TAG_NAME,'li')

for li in li_elements:
    price = li.find_element(By.CSS_SELECTOR,'.kk-price-local__normal').text
    title = li.find_element(By.TAG_NAME,'h3').text
    a_element = li.find_element(By.TAG_NAME,'a')
    link = a_element.get_attribute('href')
    
    img_element = li.find_element(By.CSS_SELECTOR,'.product-card__image')
    
    img = img_element.get_attribute('data-src')
    
    
    
    print('價格：',price)
    print('主題：',title)
    print('連結：',link)
    print('圖片：',img)
    print()
    
