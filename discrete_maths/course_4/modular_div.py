# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    global d
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def divide(a, b, n):
  assert n>1 and a>0
  Para_=extended_gcd(n,a)[2]
  assert d == 1
  return Para_*b%n

print(divide(7,5,9))
