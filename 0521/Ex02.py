# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:42:55 2024

@author: USER
"""

student = {'John':99,'Peter':88}

student['Bill'] = 66

student.update({'Mary':87,'Sue':92})

print(student)

for k in sorted(student):
    print('%-12s %3d' % (k,student[k]))
    
student.pop('John')    

print(student)

for k in sorted(student,reverse=True):
    print('%-12s %3d' % (k,student[k]))
    

print("清空字典",student.clear())
student.update(Eric=99,George=73)

print(student)












    