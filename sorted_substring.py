# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'abcdefghijklmnopqrstuvwxyz'
result = []
final = []
for letters in s:
    result = result + [letters]        
    if result == sorted(result) and len(result) > len(final):
        final=result            
    elif result != sorted(result):
        result = [result[len(result)-1]]        

print("Longest substring in alphabetical order is:" +''.join(final))