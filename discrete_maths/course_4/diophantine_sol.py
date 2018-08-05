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

def diophantine(a, b, c):
  if a>=b:
    d,x,y=extended_gcd(a,b)
  else:
    d,x,y=extended_gcd(b,a)
  assert c%d==0
  Mult_=c//d
  if a>=b:
    Result1=Mult_*x
    Result2=Mult_*y
  else:
    Result1=Mult_*y
    Result2=Mult_*x
  return (Result1,Result2)

print(extended_gcd(9,7))

