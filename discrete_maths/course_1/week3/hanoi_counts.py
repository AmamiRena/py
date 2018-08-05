# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def hanoi(n):
    if n==1:
        return 1
    else:
        counts=2*hanoi(n-1)+1
        return counts

n=int(input('Enter level of hanoi: '))
print('need total times:',end=' ')
print(hanoi(n))
