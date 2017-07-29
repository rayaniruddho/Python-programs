# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:37:18 2016

@author: User
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp=0
    ans=[]
    i=0
    power=base**exp
    ans.append(abs(power-num))
    exp+=1
    power=base**exp
    ans.append(abs(power-num))
    exp+=1
    while ans[i+1]<ans[i]:
        i+=1
        power=base**exp
        ans.append(abs(power-num))
        exp+=1
    return exp-2
print(closest_power(2,3))

    
    