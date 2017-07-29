# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 23:39:48 2016

@author: User
"""

'''def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    length=len(L)
    M=L[:]
    L=[]
    j=0
    while j<length:
       i=0
       N=[]
       while i<len(M[length-1-j]):
          N.append(M[length-1-j][len(M[length-1-j])-1-i])
          i+=1          
       L.append(N)
       j+=1
    print(L)
L=[[0], [1], [2], [3], [-1]]
deep_reverse(L)
print(L)'''
def is_list(p):
    return isinstance(p, list)

def deep_reverse(a):
    a.reverse()
    for i in a:
        if is_list(i):
            deep_reverse(i)  # <=== This is what changed
            
a=[[0], [1], [2], [3], [-1]]
deep_reverse(a)
print(a)

 