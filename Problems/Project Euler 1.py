# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:50:02 2019

@author: Dhiaz Rafilianza
"""
p = 0
n = 0
for n in range (0,1000):
    if n%3 == 0:
        m = n
        p += m
        n =+ 1
        
    elif n%5 == 0:
        m = n
        p += m
        n =+ 1
        
    else :
     n =+ 1
     
     
print (p)
    
# Project Euler 1 Solved