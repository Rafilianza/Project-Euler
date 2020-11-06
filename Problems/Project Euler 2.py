# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:57:57 2019

@author: Dhiaz Rafilianza
"""
a = 1
b = 2
d=0
counter = 0
my_list = [1,2]
while d <= 4000000:
    d = a+b
    a = b
    b = d
    if d % 2 == 0:
        counter = counter + d
    else:
        continue
    
counter = counter + 2
print (counter)
    
    
    