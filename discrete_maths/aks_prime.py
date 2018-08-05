# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def isprime(n):
    if n==2:
        return True
    if n==3:
        return True
    if n%2==0:
        return False
    if n%3==0:
        return False
    i=5
    w=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=w
        w=6-w
    return True
            
print(isprime(239))

def listprime():
    list_=[2,3]
    for n in range(5,1000):
        if n%2==0:
            continue
        if n%3==0:
            continue
        i=5
        w=2
        while i*i<=n:
            if n%i==0:
                break
            i+=w
            w=6-w
        list_.append(n)
    return list_


