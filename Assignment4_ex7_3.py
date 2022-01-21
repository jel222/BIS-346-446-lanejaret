#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 7.3
Jan 20th 2022

"""

import numpy as np

x=np.arange(2,20,2).reshape(3,3)

print(x)

y=np.arange(9,0,-1).reshape(3,3)

print(y)

z=np.multiply(x,y)

print(z)