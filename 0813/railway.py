# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystation"

header = {
    
    'cookie':
'_ga=GA1.1.915567813.1723546383; _ga_9P3LQ5F3SZ=GS1.1.1723546382.1.1.1723546678.0.0.0',

'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    
    }
    
    
#參數    
params = {
    
    '_csrf': 'a834c3cb-4561-4d1f-a1d0-b886b4e26165',
'rideDate': '2024/08/13',
'station': '3300-臺中'
    
    
    }    

data = requests.post(url,headers=header,data=params)

data.encoding = "utf-8"

data = data.text

soup = BeautifulSoup(data,'html.parser')

#順行
tab1 = soup.find(id='tab1') 

#逆行
tab2 = soup.find(id='tab2')

tab1tr = tab1.find_all('tr')

for row in tab1tr:
    
    tds = row.find_all('td')
    
    if len(tds)  > 0:
        print('車種車次:',tds[0].text.strip().replace("\n",""))
        print('出發：' ,tds[1].text.strip())
        print('終點站:',tds[2].text.strip())
        print('設施：',tds[3].text.strip())
        print('狀態:',tds[4].text.strip())
        print()
    
        

tab1tr = tab2.find_all('tr')

for row in tab1tr:
    
    tds = row.find_all('td')
    
    if len(tds)  > 0:
        print('車種車次:',tds[0].text.strip().replace("\n",""))
        print('出發：' ,tds[1].text.strip())
        print('終點站:',tds[2].text.strip())
        print('設施：',tds[3].text.strip())
        print('狀態:',tds[4].text.strip())
        print()        
          
        
        
        













    
    
    