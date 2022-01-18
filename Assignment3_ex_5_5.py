#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 5.5
Jan 17th 2022

"""


#alphabet string
alphabet='abcdefghijklmnopqrstuvwxyz'


#part a
first_half=alphabet[0:13]


print('a)\t', first_half)


#part b
first_half2=alphabet[:13]
print('b)\t', first_half2)

#part c
second_half=alphabet[13:26]
print('c)\t', second_half)

#part d
second_half2=alphabet[13:]
print('d)\t', second_half2)

#part e
every_other=alphabet[::2]
print('e)\t', every_other)

#part f
reverse=alphabet[::-1]
print('f)\t', reverse)

#part g
every_third_reverse=alphabet[::-3]
print('g)\t', every_third_reverse)