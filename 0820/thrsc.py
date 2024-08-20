# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:57:52 2024

@author: USER
"""

import requests
import json


station = {
    '南港':'NanGang',
    '台北':'TaiPei',
    '板橋':'BanQiao',
    '桃園':'TaoYuan',
    '新竹':'XinZhu',
    '苗栗':'MiaoLi',
    '台中':'TaiZhong',
    '彰化':'ZhangHua',
    '雲林':'YunLin',
    '嘉義':'JiaYi',
    '台南':'TaiNan',
    '左營':'ZuoYing'

    }


s = input('請輸入出發站：')
sStation = station.get(s,'NanGang')

e = input('請輸入到達站：')
eStation = station.get(e,'ZuoYing')





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
'StartStation': sStation,
'EndStation': eStation,
'OutWardSearchDate': '2024/08/20',
'OutWardSearchTime': '20:00',
'ReturnSearchDate': '2024/08/20',
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
    
    c=0
    for st in row['StationInfo']:
        
        if st['Show']:
            
            if s == st['StationName'] or e == st['StationName']:
                c += 1
            
            if 1 <= c <= 2 :                
                station.append(st['StationName'])
                if e == st['StationName']:
                    break
                
                
                
    print('停靠站：',station)    
    print()
    




















