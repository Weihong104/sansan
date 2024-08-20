# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup

import requests

url  = "https://news.cts.com.tw/real/index.html"

header = {
    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',

'Cookie':
'_gid=GA1.3.280707477.1723114263; _fbp=fb.2.1723114262559.588892637769527; AWSALB=DVuwhpI2Rh0aR5UGROgrz3YQPnq6pcNaL24GH+SA2NPuS5793nhKeMOaWD3ht40x+1wO51BalSUAsDEUqw+OfhE2zvV5ajQiTIr35D7ChHwVJhdIxY5Qrli6kyiY; AWSALBCORS=DVuwhpI2Rh0aR5UGROgrz3YQPnq6pcNaL24GH+SA2NPuS5793nhKeMOaWD3ht40x+1wO51BalSUAsDEUqw+OfhE2zvV5ajQiTIr35D7ChHwVJhdIxY5Qrli6kyiY; AviviD_uuid=994a0592-200d-4a75-a015-13d2de8d1ef3; webuserid=2cedd5b0-ec68-e171-9261-686d92d07a49; ch_tracking_uuid=1; __htid=1730a2ac-76d3-4303-83cf-239e60713b20; _ht_em=1; _ht_47b240=1; __gads=ID=fb963c379679e928:T=1723114281:RT=1723114281:S=ALNI_MauK0QB0bS6qo7O5dlL78eY5mIe2g; __gpi=UID=00000eb92c9a9e04:T=1723114281:RT=1723114281:S=ALNI_MamGoS6gtn8tvhZjQSzdfiPqEeyew; __eoi=ID=1f07865392076370:T=1723114281:RT=1723114281:S=AA-AfjYXfr3LnwRf14dKPP2stW4u; ISMD5VERSION=1; CFFPCKUUID=4759-qjExNtw9lNEos8nZD8tKC1ZcbkoS6Z2P; CFFPCKUUIDMAIN=9528-QegWu50gQzSGPXtQwh3DHs11kyMpJoSn; FPUUID=9528-a89fe15316cad69e5bcf91a94dc58f17; _ht_hi=1; _ht_50ef57=1; AviviD_refresh_uuid_status=2; _ss_pp_id=48d31a2753c114dcafc1723085592232; dable_uid=14991885.1715674563456; _ht_f3244e=1; oid=%257B%2522oid%2522%253A%25226b25cc58-5574-11ef-bdb2-0242ac130002%2522%252C%2522ts%2522%253A-62135596800%252C%2522v%2522%253A%252220201117%2522%257D; _tg_IM=1; _td=733ecc9d-42fd-4a55-a7a5-9a2d43fd308d; _ga=GA1.3.1124006614.1723114262; _ga_F6LZM62QYC=GS1.3.1723114271.1.1.1723114402.52.0.0; _ga_FWQF4JLMB1=GS1.3.1723114262.1.1.1723114402.52.0.0; FCNEC=%5B%5B%22AKsRol8CyN7WjJPiHbdYuKP2OaPjAHzHBsWPVjtkektFXnKH9xFh3hnw1NR8lpoojtQIGZToc6Wc7cBqsmNEat-Mo77W-e5q564Mle0seIkGngVHfMaXbBtZ_3EAQqoYlp7XUOF1ymOmFIxsyZiEiyzfRJvpWAoJRA%3D%3D%22%5D%5D; _ga_B5S0TX9D32=GS1.1.1723114262.1.1.1723114576.60.0.1517142844'
    
    }
    
    
data = requests.get(url,headers=header)
data.encoding = "utf-8"    
data = data.text

soup = BeautifulSoup(data,'html.parser')

allnews = soup.find(id='newslist-top')

news = allnews.find_all('a')

for row in news:
    link = row.get('href')
    title = row.get('title')
    #h3 = row.find('h3').text.strip()
    img = row.find('img')
    if img != None:
        photo = img.get('data-src')
        if photo == None:
            photo = img.get('src')
    else:
        photo = ''
        
        
    print(link)
    print(title)
    #print(h3)    
    print(photo)
    
    print()








