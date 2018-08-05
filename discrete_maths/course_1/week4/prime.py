# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
for n in range(2,1000):
    found=False
    test_num=n**2+n+41
    for i in range(2,test_num):
        if test_num%i==0:
            found=True
            break
    if found==True:
        break
print('n is',n)
print('divisor is',i)
print('minimum num is',test_num)
