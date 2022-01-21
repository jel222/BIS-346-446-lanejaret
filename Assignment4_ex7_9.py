# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 7.9
January 21st 2022
"""

import numpy as np

x=np.arange(1,16,1).reshape(3,5)

print(f'Original:\n{x}')
print()

print(f'a)\n{x[2]}')
print()

print(f'b)\n{x[:,4]}')
print()

print(f'c)\n{x[0:2,]}')
print()

print(f'd)\n{x[:,2:5]}')
print()

print(f'e)\n{x[1,4]}')
print()

print(f'f)\n{x[1:3,[0,2,4]]}')
print()
