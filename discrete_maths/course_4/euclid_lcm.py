# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def lcm(a,b):
    assert a>0 and b>0
    Mult_=a*b
    while a>0 and b>0:
        if a>=b:
            a=a%b
        else:
            b=b%a
    return Mult_/max(a,b)
            







