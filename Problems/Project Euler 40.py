# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:47:56 2020

@author: Dhiaz Rafilianza
Project Euler 40

DONE ! BUT IT TAKES A LONG TIME
NEEDED OPTIMIZATION!

"""
my_list=[9]
for i in range (1,1000000):
    my_list.append(i)
    
#   print(my_list) 
x = int("".join(map(str, my_list)))
#print(x)
res = list(map(int, str(x)))
#print(res)
#print(res[15])
Result = res[1]*res[10]*res[100]*res[1000]*res[10000]*res[100000]*res[1000000]

print (Result)

# 0.1234567
#[1,2,3,4]