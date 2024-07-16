# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:14:51 2024

@author: USER
"""

a,b,c = 10,20,30
print(a)
print(b)
print(c)

d = 10,20,30

print(d)

student = ('John','Man',100,95,67)

name,sex,*score = student

print('姓名：',name)
print('性別：',sex)
print('分數：',score)