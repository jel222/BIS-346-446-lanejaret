#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 4.12
January 10th 2022

"""

import random

race_end=70

def move_tortoise(t):
    move=random.randrange(1,11)
    
    if move<=5:
        t+=3
    elif move>7:
        t+=1
    else:
        t-=6 
        
    if t <1:
        t=1
    elif t>race_end:
        t=race_end
    return t
    
def move_hare(h):
    move=random.randrange(1,11)
    if move in (3,4):
        h+=9
    elif move==5:
        h-=12
    elif 6<= move<=8:
        h+=1
    elif move>8:
        h-=2
        
    if h <1:
        h=1
    elif h>race_end:
        h=race_end
    return h
    
    
def print_pos(t,h):
    for i in range(1,race_end+1):
        if i==t and i==h:
            print('Ouch!!!', end='')
        elif i==h:
            print('H', end='')
        elif i==t:
            print('T', end='')
        else:
            print('-',end='')
    print()
    
   
hare=1
tortoise=1
timer=0

print('ON YOUR MARK, GET SET')
print('BANG!!!!!')
print('AND THEYRE OFF!!!!!')

while tortoise<race_end and hare<race_end:
    hare=move_hare(hare)
    tortoise=move_tortoise(tortoise)
    print_pos(tortoise, hare)
    timer+=1
    
if tortoise >= hare:
    print('\nTortoise Wins!!! Yay!!!')
else:
    print('\nHare wins. Yuch')
    
print(f'TIME ELAPSED = {timer} seconds')

    