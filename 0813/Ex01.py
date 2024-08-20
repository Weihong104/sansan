# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:02:52 2024

@author: USER
"""
import requests
from bs4 import BeautifulSoup

url  = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation"
header={
        'Cookie':
'_ga=GA1.1.1742597053.1723546412; T4TIPSESSIONID=SAdLaIdp6EoMbSRf-c4jaxe1LxxfMlpcQ6W14GEd_iFZsHx4wdGc!-1481708575; _ga_9P3LQ5F3SZ=GS1.1.1723546412.1.1.1723547471.0.0.0',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
    
    
    
parms={
        '_csrf': '89ef8071-5b9d-4cdd-b855-58a03bf4e0e4',
'rideDate': '2024/08/13',
'station': '3300-臺中'
        
        
        }
    
    
data=requests.post(url.headers=header.data.params)
data.encoding="utf-8"
data=data.text
print(data)


soup=BeautifulSoup(data,'html.params')
tab1=soup.find(id='tab1')
tab2=soup.find(id='tab2')
tabltr=soup.find('id=tab2')
for row in tab1tr:
    tds=row.find_all('tr')
    if len(tds>0):
        print(tds[0].text.strip().replace('/n',""))
        print(tds[1].text.strip
        print(tds[2].text.strip
        print(tds[3].text.strip
        print()
    