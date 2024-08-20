# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:24:21 2024

@author: USER
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import time


driver = webdriver.Chrome()

driver.implicitly_wait(3)

driver.get('https://tw.buy.yahoo.com/search/product?p=%E8%A1%9B%E7%94%9F%E7%B4%99')

time.sleep(2)

soup = BeautifulSoup(driver.page_source,'html.parser')

items = soup.find_all('a',class_='sc-1drl28c-1 cnHJYW')

for row in items:
    link = row.get('href')
    title = row.find('span',class_='sc-dlyefy sc-gKcDdr sc-1drl28c-5 jHwfYO ikfoIQ jZWZIY').text
    price = row.find('span',class_='sc-dlyefy sc-gKcDdr dfRcqf hFXgfs').text
    price = price.replace('$','').replace(',','')
    
    print(link)
    print(title)
    print(price)
    print()
