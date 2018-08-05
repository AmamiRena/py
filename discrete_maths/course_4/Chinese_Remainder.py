# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def ChineseRemainderTheorem(n1, r1, n2, r2):
  Num_=r1
  while Num_%n2!=r2:
    Num_+=n1
  return Num_
#print(ChineseRemainderTheorem(3,2,5,3))
#print(ChineseRemainderTheorem(5,1,3,2))
#print(ChineseRemainderTheorem(686579304,295310485,26855093,8217207))
from functools import reduce


def egcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q


def chinese_remainder(pairs):
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

print(egcd(31,7))


print(chinese_remainder([(1,5),(2,3)]))
#print(chinese_remainder([(2,3),(3,5)]))
#print(chinese_remainder([(1,3),(1,4),(1,5),(0,7)]))
#print(chinese_remainder([(2,3),(3,5),(2,7)]))