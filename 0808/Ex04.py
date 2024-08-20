# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:21:48 2024

@author: USER
"""

from bs4 import BeautifulSoup

import requests

url  = "https://news.tvbs.com.tw/realtime"

header = {
    
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',

'Cookie':
'AMP_TOKEN=%24NOT_FOUND; _gid=GA1.3.1993636898.1723123064; cho_weather=%E8%87%BA%E5%8C%97%E5%B8%82; _fbp=fb.2.1723123064722.663444438272039303; _clck=6a3qev%7C2%7Cfo5%7C0%7C1681; FPID=FPID2.3.0sM%2Fp2a16c%2FmLcnoViynQuZb8Py6IfDU6FbARYYP5yU%3D.1723123064; FPLC=kuEjtXVs2iMBBJiI2N%2FoK%2F0voSHpnit2Rx787ox0bXV25en5mrerHV%2BU%2Bj0dA6SvWNE6Ut%2BZoohy8L43zDT05IP%2FGheRPQxR1qYun1gEfZVSJYo2G5x66c5hO0Urcg%3D%3D; FPGSID=1.1723123066.1723123066.G-B8E0BLEGRH.W4tI-3-9qjn0BKK-eWxOnA; __gads=ID=b4580ef84b606166:T=1723123066:RT=1723123066:S=ALNI_MbQ69pCIKq-XJJmjRot0ZFlEiHvMw; __gpi=UID=00000eb93f5c0150:T=1723123066:RT=1723123066:S=ALNI_MaP3iZL4YJsj3AnKk1nJrh3NHnszA; __eoi=ID=ccf4b93280fa4e3d:T=1723123066:RT=1723123066:S=AA-AfjbHUnwAKqpanBIBJgNH0Z1c; _ga_PT43NBSMZN=GS1.3.1723123064.1.1.1723123066.58.0.0; _ga_B8E0BLEGRH=GS1.1.1723123064.1.1.1723123067.0.0.1893064291; _ga=GA1.1.320785508.1723123064; _clsk=1mkf127%7C1723123067680%7C2%7C1%7Cz.clarity.ms%2Fcollect; FCNEC=%5B%5B%22AKsRol_kjysg7SvgVbvhvaDjHUbhqA7muDsgHgi0FBaj6xYEIURJtJuTy1NiRWN7X1Q8zFRGuuPw1xVh6jxp-yF10jjKQKc5OpdCun5GXtlj_NbC3vPQM1uWM91tbXvDsqxytDnmcDrcQcypPTHWhZl4eMJNyX_LYA%3D%3D%22%5D%5D; no_web_push=true'


}
    
    
data = requests.get(url,headers=header)
data.encoding = "utf-8"    
data = data.text

soup = BeautifulSoup(data,'html.parser')


allnews = soup.find(class_='news_list')

news = allnews.find(class_='list')

items = news.find_all('li')

for row in items:
    
    if row.find('h2') != None:
    
    
        title = row.find('h2').text
        
        link = row.find('a').get('href')
        time = row.find(class_='time').text
        
        photo = row.find('img').get('data-original')
        
        print(title)
        print(link)
        print(time)
        print(photo)
        
        print()
    













