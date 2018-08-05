# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
    print('x')
  else:
    print('y')
    (d, p, q) = extended_gcd(b, a % b)
    print((d,p,q),(b,a%b))
    x = q
    y = p - q * (a // b)
    print('x,y',x,y)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

print(extended_gcd(47,30))
print(extended_gcd(10,6))
print(extended_gcd(7,5))
print(extended_gcd(391,299))
print(extended_gcd(239,201))








