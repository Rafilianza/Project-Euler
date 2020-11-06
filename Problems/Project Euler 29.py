# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 02:20:05 2020

@author: Dhiaz Rafilianza

This Is Project Euler no 52

Find the smallest postive integer , x, such that 
2x, 3x, 4x, 6x contain the same digits
"""
myset = set()


for a in range (2,101):
    for b in range (2,101):
        myset.add(a**b)
        
print(len(myset))
        