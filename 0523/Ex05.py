# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:38:36 2024

@author: USER
"""

students = {'John':55,'Mary':100,'Eric':43,'Bill':12}

low60 = { k:v for k,v in students.items() if v < 60}

print('不及格人數為：',len(low60))

for k,v in low60.items():
    print("%-10s%3d" % (k,v))
    