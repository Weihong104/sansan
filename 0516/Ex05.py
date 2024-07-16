# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:19:48 2024

@author: USER
"""

import copy

n2 = [1,2,3,4,5,6,7]

n3 = copy.copy(n2)  # 淺複製  用於一維串列

print(n3)

n2[0] = 699

print(n3)

print(n2)

d = [10,20,[1,2,3]]

e = copy.copy(d)

print(e)

d[2][0] = 199

print(d)
print(e)

print()

f = copy.deepcopy(d)
d[2][1] = 699

print(d)

print(f)