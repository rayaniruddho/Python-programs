# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 21:39:28 2016

@author: User
"""

epsilon=0.01
y=24.0
guess=y/2.0
numGuesses=0
while abs(guess*guess-y)>=epsilon:
    numGuesses+=1
    guess=guess-(((guess**2)-y)/(2*guess))
print("Number of guesses= "+ str(numGuesses))
print("Square root of "+str(y)+" is about "+str(guess))