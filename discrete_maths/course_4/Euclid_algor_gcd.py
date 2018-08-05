# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  if a == 0 or b == 0:
    return max(a, b)

  for d in range(min(a, b), 0, -1):
    if a % d == 0 and b % d == 0:
      return d

  return 1

print(gcd(0, 1))
print(gcd(24, 16))
print()

def gcd1(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a - b
    else:
      b = b - a

  return max(a, b)

print(gcd1(24, 16))
print(gcd1(790933790547, 1849639579327))
print()

def gcd2(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  return max(a, b)


print(gcd2(24, 16))
print(gcd2(790933790547, 1849639579327))
print(gcd2(790933790548, 2))





