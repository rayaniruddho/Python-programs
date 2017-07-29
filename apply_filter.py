# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 03:00:38 2016

@author: User
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    M=[]
    for i in L:
        if g(f(i))==True:
            M.append(i)
     
    L[:]=M
    if L==[]:
        return -1
    
    return max(L)
            

def f(i):
    return i+2
def g(i):
    return i>5

L = [1,2,3]
print(applyF_filterG(L, f, g))
print(L)