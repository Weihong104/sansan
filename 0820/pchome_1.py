# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:34:21 2024

@author: USER
"""

import requests
import json


header = {
    
'cookie':
'_pa=xxx-62af7ca8-e9e8-4b1d-bafd-33957c59c5a8; _pat=J.1724157171139.10; uuid=xxx-c53ea399-87fe-48c3-8aba-a93b1d038c5c; _pafp=efc1aca9a6f623c3bcaca25c5336f067; _pafp_t=1724157174; puuid=P.20240820203254.2; _ga_11PNPDB1Q1=GS1.1.1724157174.1.0.1724157174.60.0.0; _ga_QB624SM9W2=GS1.1.1724157174.1.1.1724157209.25.0.0; U=efa0e907c2db32d4e9069649c0381da6d9548725; ECC=a07ade99817bb6401c4e5d1a27ddde3f68f11311.1724157210; ECWEBSESS=9bbaecd5fd.c589f04096363985bd957f9975ff972614a70227.1724157210; sstSID=e22a06eb-e37c-4470-bc01-252037e47f9b.null; sstDID=d23bb645-0dda-408c-8d0c-96a90701c9ff; _gcl_au=1.1.42158725.1724157210; gsite=24h; _ga_9876543210=GS1.1.1724157209.1.0.1724157209.0.0.903450220; _ga=GA1.3.1482567304.1724157175; _gid=GA1.3.1375248784.1724157210; _fbp=fb.2.1724157210038.714667270362139697; FPID=FPID2.3.AdOK4zyMzxqwA2dqhddF8wR49%2BJ58siFIHfKvwLxi7c%3D.1724157175; FPLC=bTo5nlMTo0em%2FbkKbDxXhJitmXjhiABLO72Gn3O5z%2FD5f3A3G14%2F3Ff9p1ZY0KMeRkARXj2EPwBuHYrjJtyN2J%2BQkG%2Brbhr3Ht5ktRQTXSnr9vTt6%2BTFQnUCIOQcLg%3D%3D; cto_bundle=wdssSF95UTd3bFVUelVNbTd6OXVHa016YUhwVVNVYkR6JTJCUXhTOUQzTjRsR01udGEyYSUyQkNLcXdCZ3JuOGxBaUtFdmslMkZlcUN1YVQ5MiUyQnQwZFBkOGQxRnc3V0xGMERUUldYNXY2bUdBaUpFTlM1JTJGdDQ2MnhZQU5xNW5DcVkxTW9nUXNCVzF1SFBQU3hYbTB2eUthVXhUMzlsbkN6QUQ2c3lOSHlPanhaUFdzR3doR3A0JTNE; venguid=cbe1dd56-b772-4333-9be8-59ad4e11fe58.wgc-3rw520240820; vensession=2fbcc6ae-0f45-4092-a2dc-09a7307a81e2.wgc-s6fz20240820.se; _ga_9CE1X6J1FG=GS1.1.1724157209.1.0.1724157243.26.0.1911935782',
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    
    }
        
  
   
    
url = "https://24h.pchome.com.tw/search/?q=iphone"



data = requests.get(url,headers=header)

data.encoding = 'utf-8'

data = data.text

print(data)












