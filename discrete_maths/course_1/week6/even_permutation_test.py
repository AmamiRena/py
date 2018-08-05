# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
test_list=[0,3,2,4,5,6,7,1,9,8]
def is_even(x):
    goal_list=[]
    for i in range(len(x)):
        goal_list.append(i)
    num_count=0
    duplicate_list=x[:]

    for i1 in range(len(x)):
        if x[i1]==goal_list[i1]:
            continue
        for i2 in range(i1+1,len(x)):
            x[i1]=duplicate_list[i2]
            x[i2]=duplicate_list[i1]
            if x[i1]==goal_list[i1]:
                num_count+=1
                duplicate_list=x[:]
                break
            else:
                x=duplicate_list[:]
    if num_count%2==0:
        return True
    else:
        return False
print(is_even(test_list))
'''
test_puzzle=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 14, 13, 0] #impossible to find solution
def solution(x):
    standard=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    duplicate_puzzle=test_puzzle[:]
    for i in range(16):
        position=standard[i]
        num=test_puzzle.index(position)
        if test_puzzle[i]==standard[i]:
            continue
        elif num>i:
            for n in range(abs(num-i)):
                test_puzzle[num-n]=duplicate_puzzle[num-1-n]
                test_puzzle[num-1-n]=duplicate_puzzle[num-n]
                duplicate_puzzle=test_puzzle[:]
                if test_puzzle[i]==standard[i]:
                    break
        elif num<i:
            for n in range(abs(num-i)):
                test_puzzle[i-n]=duplicate_puzzle[i-1-n]
                test_puzzle[i-1-n]=duplicate_puzzle[i-n]
                duplicate_puzzle=test_puzzle[:]
                if test_puzzle[i]==standard[i]:
                    break
    if test_puzzle==standard:
        return test_puzzle
    return False
print(solution(test_puzzle))

def zero_position():
    standard=[]
    for n in range(size**2):
        standard.append(n)
    corner=[0,size-1,size*(size-1),size**2-1]
    side=[]
    inside=[]
    for i in range(1,size-1):
        side.append(i)
    for i in range(size*(size-1)+1,size**2-1):
        side.append(i)
    for i in range(size,size*(size-1),size):
        side.append(i)
    for i in range(size+3,size**2-1,size):
        side.append(i)
    side.sort()
    for n in set(standard)-set(corner+side):
        inside.append(n)
    inside.sort()

size=4
