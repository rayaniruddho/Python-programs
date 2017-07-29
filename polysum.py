from math import *
def polysum(n,s):
    """
    Input= no. of sides(n), length of each side(s)
    Output= sum of (area of polygon and square of perimeter)
            correct upto 4 decimal places
    """
    area=(0.25*n*s*s)/tan(pi/n)#calculates area of polygon
    peri=n*s#calculates perimeter
    sum=area+peri**2#calculates required output
    return float('%.4f'%(sum))#returns output in correct format