# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:48:40 2016

@author: User
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)>1 and char==aStr[int((len(aStr)-1)/2)]:
        return True
    elif len(aStr)==1 and char==aStr[0]:
        return True
    elif aStr=='':
        return False
    elif char<aStr[int((len(aStr)-1)/2)]:
        return isIn(char,aStr[:int((len(aStr)-1)/2)])
    elif char>aStr[int((len(aStr)-1)/2)]:
        return isIn(char,aStr[int((len(aStr)-1)/2)+1:])
        
print(isIn('p','aniruddho'))
        