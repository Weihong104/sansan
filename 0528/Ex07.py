# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:36:04 2024

@author: USER
"""

print(divmod(11, 2))
a,b = divmod(11, 2)
print(a)
print(b)

print(abs(-10))

print(float("1.2345"))

print(pow(2,3))

print(round(100.345,1))

name = ['John','Mary','Bill']

score = [99,86,69]

item = zip(name,score)

#print(list(item))

data = list(item)

print(data[0])

for k,v in zip(name,score):
    print(k)
    print(v)