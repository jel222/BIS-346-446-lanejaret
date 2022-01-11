#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 3.16
January 10th 2022

"""

n=[14,17,11,20,30,45,37,50,55,1]


max1=0
max2=0
if n[0]>n[1]:
    max1=n[0]
    max2=n[1]
else:
    max1=n[1]
    max2=n[0]
for i in range(2,10):
    if n[i]>max2:
        if n[i]>max1:
            max2=max1
            max1=n[i]
        else:
            max2=n[i]
print('Max Values: ', max1,' ',max2)

