# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:11:07 2016
@author: AR
coding done in python 3.5
"""
"""
i= Starting point, should be between 0 and (n-1)
j= Destination, should be between 0 and (n-1)
n= number of terminals, should be a power of 2
Output= path from source to destination
"""
import math 

i=int(input("Enter starting point:"))
j=int(input("Enter destination:"))
n=int(input("Enter the number of terminals:"))

if i<0 or i>=n or j<0 or j>=n:
    raise ValueError("Invalid source or destination")
    
    
if not math.log(n,2)==int(math.log(n,2)):
    raise ValueError("Number of terminals should be a power of 2")
    
    
numOfStages=int(math.log(n,2))
numOfSwitches=n/2
tag=int(i)^int(j)

def shuffle(val,r_bits,max_bits):
    """
    Input= A number with no. of bits ==max_bit
    Output= Input no. left rotated by r_bits
    """
#    rol = lambda val, r_bits, max_bits: \
    newval=(val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
#    max_bits =numOfStages  
#    value = int(a)
#    newval = rol(value, 1, max_bits)
    return newval
    
def exchange(x):
    """
    Input= tag
    Output= Whether exchange is needed or not
    """
    t=2**(numOfStages-1)
    if x&t==0:
        return False
    elif x&t==t:
        return True
        

node=i  
for k in range(0,numOfStages):
    print("\nStage "+str(k)+"\n")    
    inp=shuffle(node,1,numOfStages)
    switchnum=int(inp/2)
    print("Switch number= "+str(switchnum))
    print("Input= "+str(inp))
    res=exchange(tag)
    tag<<=1
    if res==True:
        if inp%2==0:
            outp=inp+1
        else:
            outp=inp-1
    else:
        outp=inp
    print("Output= "+str(outp))
    node=int(outp)
    

    