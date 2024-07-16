# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:59:02 2024

@author: USER
"""
# 不定長度的引數
def student(name,*score,subject=5):
    if subject >= 1 :
        print('姓名：',name)
        print('共有',subject,'科，分數：',score)
    total = sum(score)    # 加總分數
    print('總分：',total,'平均：%.3f'%(total/subject))
    
    
student('Mary',77,66,88,99,100)    
student('John',88,77,66,subject=3)
        