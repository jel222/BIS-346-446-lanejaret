#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 4.9
January 10th 2022

"""

def Fahrenheit(c):
    return (9/5)*c+32

print('Celsius\tFahrenheit')
for celsius in range(101):
    f=Fahrenheit(celsius)
    print(celsius,'\t\t',f)