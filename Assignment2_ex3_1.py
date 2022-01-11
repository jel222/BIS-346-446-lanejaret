#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Jaret Lane
Exercise 3.1
January 9th 2022

"""

passes=0
failures=0
student=0
while student<10:
    result=int(input('enter result (1-pass, 2-fail):'))
    if result ==1:
        passes=passes+1
    elif result==2:
        failures=failures+1
    else:
        print('Please input valid response')
        student=student-1
    student=student+1
    
print('Passes: ',passes)
print('failures: ',failures)