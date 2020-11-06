# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:02:40 2020

@author: Dhiaz Rafilianza
Problem 30




NOT DONEE
"""
total = 0

for a in range (1,5):
    for b in range (1,5):
        for c in range (1,5):
            for d in range (1,5):
                my_list=[a,b,c,d]
                x = int("".join(map(str, my_list)))
                if a**4 + b**4 + c**4+d**4 == x:
                    total = total + x
                    continue
                else:
                    continue
                
print(total)
                