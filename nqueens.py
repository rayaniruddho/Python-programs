# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:43:23 2017

@author: Aniruddho
"""

def nQueenProblem( n ):
  queens = [0] * n
  addQueen( 0, queens, n )
  return queens;

def addQueen( x, queens, n ):
  i = 0
  while i < n and 0 == queens[n - 1]:
    if safeToAdd( x, i, queens ):
      queens[x] = i
      addQueen( x + 1, queens, n )
    i += 1

def safeToAdd( x, y, queens ):
  for i in range( x ):
    if y == queens[i] or ( x - y ) == ( i - queens[i] ) or ( x + y )== ( i + queens[i] ):
      return False
  return True
  
