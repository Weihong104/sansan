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

driver.get('https://24h.pchome.com.tw/search/?q=iphone')

time.sleep(2)

soup = BeautifulSoup(driver.page_source,'html.parser')

print(soup)