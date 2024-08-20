# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:26:07 2024

@author: USER
"""
import requests
import json
url="https://www.thsrc.com.tw/TimeTable/Search"

header={
   'Cookie':
'_gcl_au=1.1.696463694.1723551121; _td_cid=1515914785.1723551121; _gid=GA1.3.233189513.1723551122; _fbp=fb.2.1723551121692.156873995776201979; AcceptThsrcCookiePolicyTime=Tue%20Aug%2013%202024%2020:12:02%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93); _ga_1FDVRGS3MR=GS1.1.1723551120.1.1.1723552730.60.0.0; _ga=GA1.3.339135898.1723551121; _ga_6M07CCJT7N=GS1.1.1723551121.1.1.1723552793.60.0.0',
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'       
        
        }
    
params={

'SearchType':'S',
'Lang':'TW',
'StartStation':'NanGang',
'EndStation':'ZuoYing',
'OutWardSearchDate':'2024/08/13',
'OutWardSearchTime':'20:30',
'ReturnSearchDate':'2024/08/13',
'ReturnSearchTime':'20:30',
'DiscountType': ''
       
       
       }    

    

data=requests.post(url,headers=header.data.params).text
thsrc=json.loads(data)
thsrc=thsrc['data']['DepartureTable']['TrainItrm']
for row in tharc:
    print("車站"='StartStationName')
    print("出發時間"='DepartureDate')
    print("抵達時間"='DestinationTime')
    station=[]
    for s in row ['statioInfo']:
        if s['show']:
            station.appendcs['StatioName'])
        print('停靠站='.station)
        print()