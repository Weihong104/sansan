# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:26:58 2024

@author: USER
"""

import requests
from bs4 import BeautifulSoup
url='https://rate.bot.com.tw/xrt?Lang=zh-TW'

header={
        'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }



data=requests.get(url,headers=header).text
soup=BeautifulSoup(data,'html.parser')

table=soup.find('table')


rate=table.find('tbody')

trs=rate.find_all('tr')
for row in trs:
    tds=row.find_all('td')
    currency=tds[0].text.strip()#去前後空白
    
    money=currency.split()
    currency=money[0]+money[1]
    
    cashbuy=tds[1].text.strip()
    cashsell=tds[2].text.strip()
    spotbuy=tds[3].text.strip()
    spotsell=tds[4].text.strip()
    print(currency,cashbuy,cashsell,spotbuy,spotsell)
    
    
    