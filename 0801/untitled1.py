# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:28:51 2024

@author: USER
"""

import requests
import json
url='https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=6bc80d3f-9761-4245-b14f-1858749c4283'
data= requests.get(url).text

param={
      'api_key':'6bc80d3f-9761-4245-b14f-1858749c4283'
      }

data=requests.get(url, params=param).text

air=json.loads(data)

allair=air['records']

for item in allair:
    
    print('城市:',item['county'])
    print('地區:',item['sitename'])
    print('AQI:',item['aqi'])
    print('狀態:',item['status'])
    print()