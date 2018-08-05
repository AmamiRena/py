# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print('combinations_with_replacement(i1,i2)')
print('i1>>>number of options, or areas/divisions')
print('i2>>>number of slots')
x=int(input('i1: '))
y=int(input('i2: '))
count=0
from itertools import combinations_with_replacement
for c in combinations_with_replacement(range(x), y):
    count+=1
    #print("".join(c))
print(count)
