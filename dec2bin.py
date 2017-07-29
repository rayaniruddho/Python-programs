# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:06:49 2016

@author: User
"""

x=-19
if x<0:
    isNeg=True
    x=abs(x)
else:
    isNeg=False
result=''
if x==0:
    result='0'
while x>0:
    result=str(x%2)+result
    x=x//2
if isNeg:
    result='-'+result
print(result)