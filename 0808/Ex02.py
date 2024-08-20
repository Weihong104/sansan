# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:09:07 2024

@author: USER
"""

from bs4 import BeautifulSoup

import requests

url  = "https://www.setn.com/ViewAll.aspx"

header = {
    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',

'Cookie':
'__htid=1730a2ac-76d3-4303-83cf-239e60713b20; _ht_em=1; AviviD_uuid=994a0592-200d-4a75-a015-13d2de8d1ef3; webuserid=867ec3ee-091f-c567-d3be-4bffe50fbf5d; userKey=f15bd6c7-0033-420c-838b-f20a0b1bf1a9; AviviD_already_exist=0; AviviD_sw_version=1.0.868.210701; ch_tracking_uuid=1; _ga=GA1.1.1762361344.1723118258; _ht_47b240=1; _fbp=fb.1.1723118257992.559480465635270529; AviviD_tid_rmed=1; _cc_id=d666ab8e5595a3823cfd24ef5fb4599f; panoramaId_expiry=1723723059870; panoramaId=8dbd1c96fc2d42cdb221917adbd5185ca02cfd7fc31d8317acefefc50b5a3cf7; panoramaIdType=panoDevice; __gads=ID=e3ae1ed71120aecd:T=1723118259:RT=1723118259:S=ALNI_MZ1JPb6vLdBn6bIK2c4hzp5cee6iw; __gpi=UID=00000eb935107114:T=1723118259:RT=1723118259:S=ALNI_MbshQRsm7PregNNUy-9cH-uerZ3UQ; __eoi=ID=b51f160b76ed70bc:T=1723118259:RT=1723118259:S=AA-AfjYJpyrdNtjL9M-yV21nJmeS; stid=1762361344.1723118258; stid2=1762361344.1723118258; AviviD_token_retake=0; _ht_hi=1; AviviD_refresh_uuid_status=2; show_avivid_native_subscribe=2; _ttd_sync=1; _ga_8NJ3QZRCY6=GS1.1.1723118257.1.1.1723118281.36.0.0; _ga_54ZJR9ZRH0=GS1.1.1723118257.1.1.1723118281.36.0.0; FCNEC=%5B%5B%22AKsRol_uNOtlMp534da7bRVxHlqdULs2fkuv9mzUlPUN5GuO8mVbh-ILnzbAjA1aAw--2_mIZZrtRXJtnWPjdpMGXwPEV1N43tIzPf0Ppc6WQ8C8xXgri9TpABI0UMuho8xU_EPdjqryTW84silP6GZDFK5IINpZrg%3D%3D%22%5D%5D; Privacy=true'    
}
    
    
data = requests.get(url,headers=header)
data.encoding = "utf-8"    
data = data.text

soup = BeautifulSoup(data,'html.parser')

allnews = soup.find(id='NewsList')

times = allnews.find_all('time')
h3s = allnews.find_all('h3')

for i in range(len(times)):
    time = times[i].text
    
    title = h3s[i].text
    link = h3s[i].find('a').get('href')
    
    if not ('https' in link):
        link = 'https://www.setn.com' + link 
        
    
    print(time)
    print(title)
    print(link)
    print()















