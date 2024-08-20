# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:30:17 2024

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import urllib.request


url = "https://www.ptt.cc/bbs/Beauty/index.html"

header = {
    'cookie':'over18=1',
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    }
    
t = 1

for i in range(1):
    
    data = requests.get(url,headers=header)
        
    data.encoding = 'utf-8'    
        
    data = data.text
    
    soup = BeautifulSoup(data,'html.parser')   
    
    
    names = soup.find_all(class_='r-ent')
    for row in names:
        if row.find('a') != None:
            link = 'https://www.ptt.cc' + row.find('a').get('href')
            title = row.find('a').text
            
            
            
            data2 = requests.get(link,headers=header)                
            data2.encoding = 'utf-8'    
            data2 = data2.text            
            soup2 = BeautifulSoup(data2,'html.parser')   
            richcontent = soup2.find_all(class_='richcontent')
            for item in richcontent:
                if item.find('img') != None:
                    img = item.find('img').get('src')
                    print(img)
                    if 'imgur' in img:
                        try:
                            urllib.request.urlretrieve(img,str(t)+'.jpg')
                        except Exception as e:
                            pass
                        finally:
                            t+=1
                    
            
    
    page = soup.find_all(class_='btn wide')
    upPage = page[1].get('href')
    url = 'https://www.ptt.cc' + upPage








    
