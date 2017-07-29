# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 00:57:11 2016

@author: User
"""
def f(a,b):
    return a>b
def dict_interdiff(d1,d2):
    d3 ={}
    d4 ={}
    res=()
    for i in d1.keys():
        if i in d2.keys():
            d3[i] = f(d1[i],d2[i])
        else:
            d4[i] = d1[i]
        for i in d2.keys():
            if i not in d1.keys():
                d4[i] = d2[i] 
        res = d3,d4  
    if d1=={} and d2=={}:
        res=d1,d2
    return res
d1={}
d2 = {}
print(dict_interdiff(d1, d2))
