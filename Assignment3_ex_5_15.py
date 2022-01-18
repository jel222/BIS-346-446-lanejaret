#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 5.15
Jan 17th 2022

"""
from operator import itemgetter


items = [(83, 'Electric sander',7,57.98),(24,'Power saw',18,99.99),(7, 'Sledge hammer',11,21.5),(77,'Hammer',76,11.99),(39,'Jig saw',3,79.5)]


#part a
a_sort=sorted(items, key=itemgetter(1))
print('a)')
for i in range(5):
    print(a_sort[i])
print()

#part b
b_sort = sorted(items, key= itemgetter(3))
print('b)')
for i in range(5):
    print(b_sort[i])
print()

#part c
part_quantity=[]
for i in range(len(items)):
    this_tuple=(items[i][1], items[i][2])
    part_quantity.append(this_tuple) 
c_sort=sorted(part_quantity,key=itemgetter(1))
print('c)')
for i in range(5):
    print(c_sort[i])
print()

#part d
part_value=[]
for i in range(len(items)):
    this_tuple=(items[i][1], items[i][2]*items[i][3])
    part_value.append(this_tuple) 
d_sort=sorted(part_value,key=itemgetter(1))
print('d)')
for i in range(5):
    print(d_sort[i])
print()

#part e
filtered=[]
for i in range(len(d_sort)):
    if 200< d_sort[i][1] < 500:
        filtered.append(d_sort[i])
print('e)')
for i in range(len(filtered)):
    print(filtered[i])
print()

#part f
total=0
for i in range(len(d_sort)):
    total+=d_sort[i][1]
print('f)\tTotal: ',total)


