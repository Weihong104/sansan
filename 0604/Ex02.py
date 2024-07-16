# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:05:19 2024

@author: USER
"""

#求質數　　可被自然數及自己整數的數

for i in range(2,101):
    for x in range(2,i):
        if i % x == 0:
            #print(i,"不是質數")
            break
    else:
        print(i,'是質數')