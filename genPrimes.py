# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:35:53 2016

@author: User
"""

def genPrimes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1
        
        
    
