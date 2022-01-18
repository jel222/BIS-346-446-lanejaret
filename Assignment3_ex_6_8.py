#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
Exercise 6.8
Jan 17th 2022

"""

num_dictionary={1:'one', 2:'two', 3:'three',4:'four',
                5:'five',6:'six',7:'seven',8:'eight',
                9:'nine',10:'ten',11:'eleven',12:'twelve',
                13:'thirteen',14:'fourteen',15:'fifteen',
                16:'sixteen',17:'seventeen',18:'eighteen',
                19:'ninteen',20:'twenty',30:'thirty',40:'forty',
                50:'fifty',60:'sixty',70:'seventy',80:'eighty',
                90:'ninety',100:'hundred'}

value=input('Enter check value< (<1000):\t')


string_num=''

number=value.split('.')



hundreds=int(int(number[0])/100)
tens=int((int(number[0])%100)/10)
ones=int((int(number[0])%10))

if hundreds>0:
    string_num=string_num+num_dictionary[hundreds]+' '+num_dictionary[100]+' '
if tens>0:
    if tens==1:
        string_num=string_num+ num_dictionary[int((int(number[0])%100))]+' '
    else:
        string_num=string_num+ num_dictionary[int(10)*tens]+' '+num_dictionary[ones]+' '
        
else:
    if ones>0:
        string_num=string_num+num_dictionary[ones]+' '
    

   
string_num=string_num+ f'and {number[1]}/100'

print(string_num)