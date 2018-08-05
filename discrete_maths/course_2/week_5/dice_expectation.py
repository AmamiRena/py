# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint, seed
from datetime import datetime

seed(datetime.now())

num_rounds = 10**5
sum_of_values = 0

for _ in range(num_rounds):
    sum_of_values += randint(1, 6)
    
print("The average is {}".format(sum_of_values/(num_rounds*1.0)))


from random import randint, seed
from datetime import datetime

seed(datetime.now())

dice1=[2, 2, 2, 2, 3, 3]
dice2=[1, 1, 1, 1, 6, 6]

num_rounds = 10**5

assert len(dice1) == 6 and len(dice2) == 6

num_dice1_wins = 0
num_dice2_wins = 0

for _ in range(num_rounds):
    dice1_result = dice1[randint(0, 5)]
    dice2_result = dice2[randint(0, 5)]

    if dice1_result > dice2_result:
            num_dice1_wins += 1
    elif dice2_result > dice1_result:
            num_dice2_wins += 1

if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice1, dice2, num_rounds, num_dice1_wins-num_dice2_wins))
elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice2, dice1, num_rounds, num_dice2_wins-num_dice1_wins))
else:
        print("A tie")
