# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:19:29 2016

@author: User
"""
import operator
def bubbleSort(L):
    swap=1
    while not swap==0:  
        swap=0
        for k in range(0,len(L)-1):
            if L[k]>L[k+1]:
                temp=L[k]
                L[k]=L[k+1]
                L[k+1]=temp
                swap+=1
                print(L)
    return L

def selectionSort(L):
    for i in range(0,len(L)-1):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
        print(L)
    return L
    
def insertionSort(L):
    for i in range(1,len(L)):
        for j in range(i-1,-1,-1):
            if L[i]<L[j]:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
                i-=1
            else:
                break
        print(L)
    return L
    
def mergeSort(L,compare=operator.lt):
    if len(L)<2:
        return L[:]
    else:
        middle=int(len(L)/2)
        left=mergeSort(L[:middle],compare)
        right=mergeSort(L[middle:],compare)
        print(left,right)
        return merge(left,right,compare)
        
def merge(left,right,compare):
    result=[]
    i,j=0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        print(result)
    while (i < len(left)):
        result.append(left[i])
        i += 1
        print(result)
    while (j < len(right)):
        result.append(right[j])
        j += 1
        print(result)
    return result
    
def quickSort(L):
    if len(L)<2:
        return L[:]
    else:
        pivot=L[0]
        i=1
        for j in range(1,len(L)-1):
            if L[j]<pivot:
                temp=L[i]
                L[i]=L[j]
                L[j]=temp
                i+=1
        for k in range(1,len(L)):
            if pivot<L[k] :
                temp=L[L.index(pivot)]
                L[L.index(pivot)]=L[k-1]
                L[k-1]=temp
                break
            elif pivot>L[len(L)-1]:
                temp=L[L.index(pivot)]
                L[L.index(pivot)]=L[len(L)-1]
                L[len(L)-1]=temp
                break
#        left=quickSort(L[0:L[k-1]])
#        right=quickSort(L[L[k]:len(L)])
        return L
    
def myAlgo(L):
    i=0
    j=len(L)-1
    swaps=0
    while i<j:
        if L[i]>L[j]:
            temp=L[i]
            L[i]=L[j]
            L[j]=temp
            swaps+=1
            print(L)
        i+=1
        j-=1
    a=(L[int(len(L)/2):])
    while len(a)>1:
        return a.append(myAlgo(a))
    return L
    
    
l=[3,5,4,2,1]  
#print("Insertion sort:")
#print(l) 
#insertionSort(l[:])
#
#print("Selection sort:")
#print(l) 
#selectionSort(l[:])
#
#print("Bubble sort:")
#print(l) 
#bubbleSort(l[:])
#
#print("Merge sort:")
#print(l)
#mergeSort(l[:])
#print(quickSort(l[:]))
print(l)
print(myAlgo(l[:]))
