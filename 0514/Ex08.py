# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:58:08 2024

@author: USER
"""

number = list()

while len(number) < 6:
    num = int(input('請輸入1~49之間的數字：'))
    if 0 < num < 50:
        if number.count(num) == 0:
            number.append(num)
            
print(number)           

"""
課後練習
1-1黑名單：10,15,39 不可以被新增進去




1-2 請使用 random 的方式來自動新增這六個數字




1-3 白名單： 17,41 一定要有
""" 