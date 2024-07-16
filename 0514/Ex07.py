# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:03:07 2024

@author: USER
"""

words = ['a','b','c','d','a','c','f','a','c','a','c']

#計次
a = words.count('a')
f = words.count('f')
g = words.count('g')


print(a)
print(f)
print(g)

# index 找尋目標物的所在index

ind = words.index('d')
print(ind)

# ind = words.index('z')
# print(ind)

ind = words.index('c')
print('c的位置：',ind)

start = 0
for i in range(words.count('c')):
    ind = words.index('c',start)
    print('C的索引：',ind)
    start = ind + 1
    
    



