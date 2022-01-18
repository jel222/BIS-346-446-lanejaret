#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 5.28
Jan 17th 2022

"""

import numpy as np

list1=[1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

values,frequencies=np.unique(list1,return_counts=True)

print('Value\tFrequency')
for i in range(len(values)):
    print(f'{values[i]}\t\t{frequencies[i]}')
print()
    
print(f'Min:\t\t{min(list1)}')
print(f'Max:\t\t{max(list1)}')
print(f'Range:\t{max(list1)-min(list1)}')
print(f'Mean:\t{np.mean(list1)}')
print(f'Median:\t{np.median(list1)}')
print(f'Mode:\t{values[np.where(frequencies==max(frequencies))]}')
print(f'Variance:\t{np.var(list1)}')
print(f'Standard Deviation:\t{np.std(list1)}')
    