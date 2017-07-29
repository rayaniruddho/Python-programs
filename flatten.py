# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:30:14 2016

@author: User
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    def rec(aList):
                j=0
                
                while j<len(aList):
                    if type(aList[j])==list:
                        rec(aList[j])
                    else:
                        K.append(aList[j])
                    j+=1
                print(K)
                return K
    L=[]
    
    length=len(aList)
    i=0
    while i<length:
        if type(aList[i])==list:
            K=[]           
            rec(aList[i])
            k=0
            while k<len(K):
                L.append(K[k])
                k+=1
        else:
            L.append(aList[i])
        i+=1
    return L
print(flatten(['b',[1,'a',['cat'],2],[[[3]],'dog'],4,5,'a']))
        