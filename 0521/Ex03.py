# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:29:21 2024

@author: USER
"""

student = {'周子瑜':77,'IU':100}

name = input('input Name:')

if name in student:
    print(name,'成績：',student[name])
else:
    score = int(input('input Score:'))    
    
    student[name] = score
    
print(student)  

keys = student.keys()

values = student.values()

print(keys)
print(values)

listkeys = list(keys)

print(listkeys)

items = student.items()
it = list(items)

print(it[0])
print(it[0][0])
print(it[0][1])


  
    