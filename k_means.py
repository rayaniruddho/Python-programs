# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 12:41:46 2017

@author: Aniruddho
"""

import openpyxl

wb = openpyxl.load_workbook('k_means.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

n = 0
count = 0
points = []
centers = []
cost = []

for row in range(2, sheet.max_row + 1):
    n += 1
    pt = (sheet['A' + str(row)].value,sheet['B' + str(row)].value)
    
    points.append(pt)
    
k = int(input("Enter the number of clusters: "))

#Needs modification
    
for num in range(0,k):
    centers.append(points[num])
    
while True: 
    mem = []    
    s=0
    print('\n'+'Itertion number '+str(count))
    for i in range(0,n):
        dist = ()
        pt_mem = []
        for j in range(0,k):
            dist += (((points[i][0] - centers[j][0])**2 + (points[i][1] - centers[j][1])**2),)
            pt_mem.append(0)
        pt_mem[dist.index(min(dist))] = 1
        mem.append(pt_mem)
        
    print('\n'+"MEMBERSHIP MATRIX")
    for i in range(1,n+1):
        print('\t'+'p'+str(i),end=' ')
    for i in range(1,k+1):
        print('\n'+'c'+str(i),end='\t')
        for j in range(0,n):
           print(str(mem[j][i-1]),end='\t')
        
    for i in range(0,k):
        for j in range(0,n):
            if mem[j][i] == 1:
                s += (points[j][0] - centers[i][0])**2 + (points[j][1] - centers[i][1])**2    
    
    print('\n'+"Distance = "+str(s))
    cost.append(s)
    
    if count >= 1:
        if s - cost[count-1] <= 0.001:
            print("Centers")
            print(centers)
            break
            
    for i in range(0,k):
        t = 0
        s1 = 0
        s2 = 0
        for j in range(0,n):
            if mem[j][i] == 1:
                t += 1
                s1 += points[j][0]
                s2 += points[j][1]
        
        centers[i] = ((s1/t),(s2/t))
    count += 1
    print("Centers")
    print(centers)
   