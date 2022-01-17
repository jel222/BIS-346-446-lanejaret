#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jaret Lane
January 16th 2022
Exam Question

"""
import random

spaces_list=['Go','Mediterranean Ave','Community Chest','Baltic Ave', 'Income Tax', 'Reading Railroad', 'Oriental Ave', 'Chance', 'Vermont Ave', 'Connecticut Ave', 'Jail/Just Visiting', 'St.Charles Place', 'Electric Company', 'States Ave', 'Virginia Ave', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Ave', 'New York Ave', 'Free Parking', 'Kentucky Ave', 'Chance', 'Indiana Ave', 'Illinois Ave', 'B. & O. Railroad', 'Atlantic Ave', 'Ventnor Ave', 'Water Works', 'Marvin Gardens', 'Go to jail', 'Pacific Ave', 'North Carolina Ave', 'Community Chest', 'Pennsylvania Ave', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']


play = True
turn=1
space=0
while (play==True):
    print('Turn ', turn)
    print('Start on: ', spaces_list[space])
    die1= random.randrange(1,7)
    die2= random.randrange(1,7)
    total= die1+die2
    print('Roll: ', die1,'\t',die2)
    print('Total spaces: ', total)
    space+=total
    if space>len(spaces_list)-1:
        space= space%( len(spaces_list) -1)
    
    print('End on: ', spaces_list[space])
    print()
    turn+=1
    if space==(len(spaces_list)-1):
        print('Game Over')
        play=False
