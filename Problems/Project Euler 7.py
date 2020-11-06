# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:37:58 2019

@author: Dhiaz Rafilianza"""

n = 2**1000


p =str(n)
f =0
c = 0
for i in p:
    print(p[c])
    f = f + int(p[c])
    c = c + 1
    
print("The Sum of The Digits is : "+str(f))
