# -*- coding: utf-8 -*-
"""
Created on Tue May 28 20:11:10 2024

@author: USER
"""

def student(school,**personal):
    print(school,"依學生姓名排序")
    
    for key in sorted(personal):
        print('%-10s%d' % (key,personal[key]))
    
    
    
    print("-" * 30)
    
    
    print("及格資訊如下")
    up60 = {k:v for k,v in personal.items() if v >= 60}
    c = len(up60)
    
    print('人數：',c,'人')
    print(up60)
    
    print("不及格資訊如下:")
    low60 = {k:v for k,v in personal.items() if v <= 60}
    c = len(low60)

    print('人數:',c,'人')
    print(low60)
    
    
student('中一中',Mary=90,Sue=81,Bill=39,John=61,Eric=42,Tom=72)    