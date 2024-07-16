# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:24:44 2024

@author: USER
"""

# 預設值參數
def circle(r=10):
    area = r * r * 3.14
    circleLen = 2 * r  * 3.14
    return area,circleLen


a,c = circle()
ac = circle(5)

print(a)
print(c)
print(ac)