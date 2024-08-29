# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:30:15 2024

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

opt = webdriver.ChromeOptions()
opt.add_argument("--user-agent=%s" % user_agent)



url = "https://www.kkday.com/zh-tw/city/tokyo"

driver = webdriver.Chrome(options=opt)

driver.get(url)


topData = driver.find_element(By.ID,'splide04')
print(topData.text)