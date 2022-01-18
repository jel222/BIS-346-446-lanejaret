#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 5.20
Jan 17th 2022

"""

def display_table(twoDlist):
    for i in range(len(twoDlist[0])):
        print('\t',i+1,end='')
    print()
    for j in range(len(twoDlist)):
        print(j+1,'\t',end='')
        for k in range(len(twoDlist[j])):
            print(twoDlist[j][k],'\t',end='')
        print()

