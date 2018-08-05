# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
import collections
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    test_group,test_result,lose_record=[],[],[]
    for i1,i2 in itertools.combinations(range(len(dices)),2):
        test_group.append((i1,i2))
    for i in range(len(test_group)):
        num_dice1_wins,num_dice2_wins = 0,0
        for _ in dices[test_group[i][0]]:
            for n in dices[test_group[i][1]]:
                if _ > n:
                    num_dice1_wins += 1
                elif n > _:
                    num_dice2_wins += 1
        if num_dice1_wins>num_dice2_wins:
            test_result.append(test_group[i][0])
            lose_record.append(test_group[i][1])
        elif num_dice2_wins>num_dice1_wins:
            test_result.append(test_group[i][1])
            lose_record.append(test_group[i][0])
    test_count=collections.Counter(test_result).most_common(2)
    if len(test_count)==1:
        return test_count[0][0]
    elif test_count[0][1]==test_count[1][1]:
        return -1
    else:
        return test_count[0][0]

dices=[[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
print(find_the_best_dice(dices))

