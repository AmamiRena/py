# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

sample = 200
x = np.arange(sample)
y = 1.02 ** x
plt.plot(x, y)
plt.xlabel('n')
plt.ylabel('Money($)')
z = 1 + 0.02 * x
plt.plot(x, z)
plt.show()

def HowMuchMoney(starting_amount, earn_percent, day):
    day_multiplier = 1 + (earn_percent / 100.0)
    return starting_amount * (day_multiplier ** (day - 1))
    
def PrintExample(starting_amount, earn_percent, day):
    print("If you start with $%d and earn %d%% each day, you will have more than $%.0f on day %d!" % 
          (starting_amount, earn_percent, HowMuchMoney(starting_amount, earn_percent, day), day))

PrintExample(1000, 2, 350)

def DayToReachTarget(starting_amount, earn_percent, target_amount):
    day = 1
    amount = starting_amount
    day_multiplier = (1 + (earn_percent) / 100.0)
    while amount < target_amount:
        day += 1
        amount = amount * day_multiplier
    return day

def PrintFirstDay(starting_amount, earn_percent, target_amount):
    print("If you start with $%d and earn %d%% each day, you will have more than $%d on day %d for the first time!" %
          (starting_amount, earn_percent, target_amount, DayToReachTarget(starting_amount, earn_percent, target_amount)))

PrintFirstDay(1000, 2, 1000000)