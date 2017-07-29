# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:53:34 2017

@author: Aniruddho
"""
"""
Assumption: Number of attributes are known
"""
import openpyxl,math
from collections import Counter
#print('Opening workbook...')

wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.get_sheet_by_name('Input')

s=0
age_values,income_values,student_values,credit_values,label_values=[],[],[],[],[]
a1,a2,a3,a4 = [],[],[],[]
i_cl = 0

e_age = 0
e_income = 0
e_student = 0
e_credit = 0
#print('Reading rows...')
   
for row in range(2, sheet.max_row + 1):
       # Each row in the spreadsheet has data for one type of customer.
       s+=1
       
       age  = sheet['B' + str(row)].value
       age_values.append(age)         
           
       income = sheet['C' + str(row)].value
       income_values.append(income)
                 
       student = sheet['D' + str(row)].value
       student_values.append(student)
                     
       credit = sheet['E' + str(row)].value
       credit_values.append(credit)
                    
       label = sheet['F' + str(row)].value
       label_values.append(label)
       
       s_age1 = (label,age)
       a1.append(s_age1)
       
       s_income1 = (label,income)
       a2.append(s_income1)
       
       s_student1 = (label,student)
       a3.append(s_student1)
       
       s_credit1 = (label,credit)
       a4.append(s_credit1)
           
s_cl = Counter(label_values)

s_age = Counter(age_values)
s_cl_age = Counter(a1)

s_income = Counter(income_values)
s_cl_income = Counter(a2)

s_student = Counter(student_values)
s_cl_student = Counter(a3)

s_credit = Counter(credit_values)
s_cl_credit = Counter(a4)

for k in s_cl:
    p_cl = s_cl[k]/s
    i_cl += p_cl*math.log(p_cl,2)*-1
    
print('I(s1,s2) = '+'%.3f'%i_cl+'\n')

for i in s_age:
    i_age = 0
    for j in s_cl:
        p_age = (s_cl_age.get((i,j),0)/s_age[i])
        if p_age>0:
            i_age += (p_age * math.log(p_age,2) * -1)
    e_age += (s_age[i]/s) * i_age
gain_age = i_cl - e_age

print('E(Age) = '+'%.3f'%e_age)

for i in s_income:
    i_income = 0
    for j in s_cl:
        p_income = (s_cl_income.get((i,j),0)/s_income[i])
        if p_income>0:
            i_income += (p_income * math.log(p_income,2) * -1)
    e_income += (s_income[i]/s) * i_income
gain_income = i_cl - e_income

print('E(Income) = '+'%.3f'%e_income)

for i in s_student:
    i_student = 0
    for j in s_cl:
        p_student = (s_cl_student.get((i,j),0)/s_student[i])
        if p_student>0:
            i_student += (p_student * math.log(p_student,2) * -1)
    e_student += (s_student[i]/s) * i_student
gain_student = i_cl - e_student

print('E(Student) = '+'%.3f'%e_student)

for i in s_credit:
    i_credit = 0
    for j in s_cl:
        p_credit = (s_cl_credit.get((i,j),0)/s_credit[i])
        if p_credit>0:
            i_credit += (p_credit * math.log(p_credit,2) * -1)
    e_credit += (s_credit[i]/s) * i_credit
gain_credit = i_cl - e_credit

print('E(Credit Rating) = '+'%.3f'%e_credit+'\n')

print('Gain(Age) = '+'%.3f'%gain_age)
print('Gain(Income) = '+'%.3f'%gain_income)
print('Gain(Student) = '+'%.3f'%gain_student)
print('Gain(Credit Rating) = '+'%.3f'%gain_credit)

control = max(gain_age,gain_income,gain_student,gain_credit)

if control == gain_age:
    print('\nThe controlling attribute is Age')
    
elif control == gain_income:
    print('\nThe controlling attribute is Income')
    
elif control == gain_student:
    print('\nThe controlling attribute is Student')
    
elif control == gain_credit:
    print('\nThe controlling attribute is Credit Rating')