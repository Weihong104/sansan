# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:38:10 2024

@author: USER
"""

score = (10,20,30,40)

print(type(score))  # only read

print(score[0])

print(score[3])

number = 1,2,3,4

print(number)

item = list(score)

item.append(66)

newScore = tuple(item)

print(newScore)