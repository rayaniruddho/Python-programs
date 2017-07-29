# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:06:49 2016

@author: User
"""
print("Please think of a number between 0 and 100!")
low=0
high=100
ans=(int)(high+low)/2
i=''
while i!='c':
    print("Is your secret number "+str(ans)+"?")
    i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if i=='c':
        print("Game over. Your secret number was: "+str(ans))
        break
    elif i=='l':
        high=ans
        ans=int((high+low)/2)
        #print("Is your secret number "+str(ans)+"?")
      #  i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif i=='h':
        low=ans
        ans=int((high+low)/2)
      #  print("Is your secret number "+str(ans)+"?")
      #  i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print("Please enter a valid input")
       # i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
