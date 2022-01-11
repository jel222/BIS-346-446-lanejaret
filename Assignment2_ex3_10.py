#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 3.10
January 10th 2022

"""

p=1000
r=.07

print('principal\tyear\t\tvalue')
for n in range(31):
    a=p*(1+r)**n
    print(p,'\t\t',n,'\t\t',a)