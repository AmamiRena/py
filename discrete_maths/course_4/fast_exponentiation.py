# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def FastModularExponentiation1(b, e, m):
  binary = bin(e)[2:]
  count = len(binary)
  x = [1] * count
  for i in binary:
    if i == '1':
      x[count - 1] = (pow(b, pow(2, (count - 1)))) % m
    else:
      x[count - 1] = 1
    count = count - 1
  p = 1
  for j in x:
    p = p * j
  c = p % m
  return c



def FastModularExponentiation2(b,e,m):
    Bin_=bin(e)[2:]
    List_=[int(l_) for l_ in Bin_[::-1]]
    Sum_=0
    for num_ in range(len(List_)):
        if List_[num_]==1: Sum_+=2**num_
    return b**Sum_%m
            
def FastModularExponentiation(b,e,m):
    assert b>0 and e>0 and m>0
    Mult_=1
    while e>0:
        if e%2==0:
            b=(b**2)%m
            e//=2
        else:
            Mult_=b*Mult_%m
            e-=1
    return Mult_
print(FastModularExponentiation(2,953,239))
print(FastModularExponentiation(7,4,11))
print(FastModularExponentiation(7,128,11))
