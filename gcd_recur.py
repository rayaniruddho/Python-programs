# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:59:46 2016

@author: User
"""

def gcdRecur(a,b):
    
    if a<=b:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                return i
    else:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                return i

print(gcdRecur(12,17))
       