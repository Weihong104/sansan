# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

score = [99,77,55,100,98,66,95]

data = sorted(score)

print('Old Data:',score)
print('sort Data:',data)

print(sorted(score,reverse=True))

for i in sorted(score,reverse=True):
    print(i)