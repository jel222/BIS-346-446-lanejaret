#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 5.11
Jan 17th 2022

"""

response=input('Enter string: ')




def summarize_letters(string):
    alpha='abcdefghijklmnopqrstuvwxyz'
    cap_alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(string)):
        letter=string[i]
        for j in range(len(alpha)):
            if letter == cap_alpha[j]:
                if i == len(string)-1:
                    string= string[:i]+alpha[j]
                else:
                    string= string[:i]+alpha[j]+string[i+1:]
    tuple_list=[]
    for k in range(26):
        count= string.count(alpha[k])
        letter_tuple= (alpha[k], count)
        tuple_list.append(letter_tuple)
    return tuple_list


list= summarize_letters(response)
has_letters=True
for m in range(len(list)):
    print(list[m])
    if list[m][1]==0:
        has_letters=False
        
if has_letters:
    print('Contrains all letters')
else: 
    print('Does not contain all letters')