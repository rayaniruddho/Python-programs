# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:10:47 2016

@author: User
"""

def printMove(fr,to):
    print('move from '+str(fr)+' to '+str(to) )
    
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
        
print(Towers(10,'P1','P2','P3'))