# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:52:30 2016

@author: User
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num=list(aDict.values())
    count=0
    for k in range(len(num)):
        count+=len(num[k])
    return count
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    values=[]
    count=0
    for k in aDict:
        if len(aDict[k])>count:
            values.append(k)
            count=len(aDict[k])
    return values[len(values)-1]
        
    
        
            
    
animals={'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
print(biggest(animals))