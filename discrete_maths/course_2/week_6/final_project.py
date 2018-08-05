# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    num_dice1_wins,num_dice2_wins = 0,0
    for n in dice1:
        for _ in dice2:
            if n>_:
                num_dice1_wins+=1
            elif _>n:
                num_dice2_wins+=1       
    return (num_dice1_wins,num_dice2_wins)

    
print(count_wins(dice1,dice2))
'''
dices= [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
import itertools
import collections
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    test_group,test_result,lose_record=[],[],[]
    for i1,i2 in itertools.combinations(range(len(dices)),2):
        test_group.append((i1,i2))
#    print(test_group)
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
        else:
            test_result.append('')
            lose_record.append('')
    test_count=collections.Counter(test_result).most_common(2)
#    print(test_result,lose_record,test_count)
#    perfect_one=True >>>>for question2
    if perfect_one==False:
        right_one=test_result[lose_record.index(_n_)]
        return right_one
    elif perfect_one==True:
        if len(test_count)==1 or test_count[0][1]>test_count[1][1] and test_count[0][0] not in lose_record:
            return test_count[0][0]
        return -1



#print(find_the_best_dice(dices))


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    strategy = dict()
    global perfect_one
    perfect_one=True
    if find_the_best_dice(dices)!=-1:
        strategy["choose_first"] = True
        strategy["first_dice"] = find_the_best_dice(dices)
        return strategy
    strategy['choose_first']=False
    perfect_one=False
    global _n_
    for _n_ in range(len(dices)):
        strategy[_n_] = find_the_best_dice(dices)
    return strategy

print(compute_strategy(dices))


