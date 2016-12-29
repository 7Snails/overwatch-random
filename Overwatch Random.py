# Random Overwatch Character Picker --- Made by 7Snails
# Version 0.0.1 -- Last updated: December 29, 2016

import os
import random

heroes = [
'Genji',
'McCree',
'Pharah',
'Reaper',
'Soldier 76',
'Tracer',
'Bastion',
'Hanzo',
'Junkrat',
'Mei',
'Törbjorn',
'Widowmaker',
'D.va',
'Reinhardt',
'Roadhog',
'Winston',
'Zarya',
'Lucio',
'Mercy',
'Symmetra',
'Zenyatta',
]

p = eval(input('How many people are participating?: '))
c = ''

while c == '':   
    for r in range(0,p):
        print(random.choice(heroes))
    c = input('Press [Enter] to continue')
os._exit(0)
