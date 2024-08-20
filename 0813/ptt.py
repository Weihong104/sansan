# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:30:17 2024

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Beauty/index.html"

header = {
    'cookie':'over18=1',
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    }
    


for i in range(10):
    
    data = requests.get(url,headers=header)
    
    data.encoding = 'utf-8'    
    
    data = data.text
    
    
