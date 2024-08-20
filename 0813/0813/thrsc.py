# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:57:52 2024

@author: USER
"""

import requests
import json

url =  "https://www.thsrc.com.tw/TimeTable/Search"

header = {
    'cookie':
'_gcl_au=1.1.1357243546.1723550294; _td_cid=1791218857.1723550293; _ga=GA1.3.1580186032.1723550293; _gid=GA1.3.1037528922.1723550294; _fbp=fb.2.1723550294063.336127861619041268; AcceptThsrcCookiePolicyTime=Tue%20Aug%2013%202024%2019:58:14%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); _ga_1FDVRGS3MR=GS1.1.1723550293.1.1.1723550320.33.0.0; _ga_6M07CCJT7N=GS1.1.1723550293.1.1.1723550561.60.0.0',


'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    
    }
    
    
params  = {
   'SearchType': 'S',
'Lang': 'TW',
'StartStation': 'TaiZhong',
'EndStation': 'ZuoYing',
'OutWardSearchDate': '2024/08/13',
'OutWardSearchTime': '20:00',
'ReturnSearchDate': '2024/08/13',
'ReturnSearchTime': '20:00' 
    }    


data = requests.post(url,headers=header,data=params).text

thsrc = json.loads(data)

thsrc = thsrc['data']['DepartureTable']['TrainItem']

for row in thsrc:
    print('車次：',row['TrainNumber'])
    print('出發時間：',row['DepartureTime'])
    print('旅行時間：',row['Duration'])
    print('抵達時間：',row['DestinationTime'])
    station = []
    for s in row['StationInfo']:
        
        if s['Show']:
            station.append(s['StationName'])
    print('停靠站：',station)    
    print()
    




















