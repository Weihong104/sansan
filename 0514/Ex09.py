# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:23:21 2024

@author: USER
"""



print('學生成績查詢系統')

students = list()
score = list()

while True:
    q = input('請輸入學生姓名查詢成績(q離開)：')
    if q == 'q':
        break
    
    if students.count(q) == 1:
        ind = students.index(q) # 找出索引值
        print('學生：',students[ind],'分數：',score[ind],'分')
        
    else:
        ans = input('是否要加入此學生(y/n):')
        if ans.lower() == 'y':  # lower() 轉小寫
            s = int(input('請輸入分數：'))
            students.append(q)
            score.append(s)
            


print(students)            
print(score)
        

