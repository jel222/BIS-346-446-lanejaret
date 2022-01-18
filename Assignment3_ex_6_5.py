#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 6.5
Jan 17th 2022

"""

from collections import Counter as ct

text=input('Enter text here:\t')

counter=ct(text.split())


dup_words=0
for word, count in sorted(counter.items()):
    if count>1:
        print(f'{word}\t{count}')
        dup_words+=1
print(f'Duplicate words:\t{dup_words}')
