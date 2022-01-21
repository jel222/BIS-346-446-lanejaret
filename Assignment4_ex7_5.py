#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 7.5
Jan 20th 2022

"""

import numpy as np

x=[]

for i in range(6):
    x.append(2**i)
    
y=np.array(x).reshape(2,3)



flattened=y.flatten()
print(f'Flattened:\t{flattened}')

raveled=y.ravel()
print(f'Raveled:\t{raveled}')

print(f'Original:\n{y}')