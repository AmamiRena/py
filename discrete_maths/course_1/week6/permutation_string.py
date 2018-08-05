# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
word='MARINE'
word_goal='AIRMEN'
def sequence():
    word_list=[]
    word_goal_list=[]
    list_count=[]
    for letter in word:
        word_list.append(letter)
    for letter in word_goal:
        word_goal_list.append(letter)
    duplicate_list=word_list[:]

    for i1 in range(len(word)):
        if word_list[i1]==word_goal_list[i1]:
            continue
        for i2 in range(i1+1,len(word)):
            word_list[i1]=duplicate_list[i2]
            word_list[i2]=duplicate_list[i1]
            if word_list[i1]==word_goal_list[i1]:
                list_count.append((i1,i2))
                duplicate_list=word_list[:]
                break
            else:
                word_list=duplicate_list
    return list_count
'''
#neighbour transpositions
word='MARINE'
word_goal='AIRMEN'
def sequence():
    word_list=[]
    word_goal_list=[]
    list_count=[]
    for letter in word:
        word_list.append(letter)
    for letter in word_goal:
        word_goal_list.append(letter)
    duplicate_list=word_list[:]
    for i in range(len(word)):
        letter=word_goal_list[i]
        num=word_list.index(letter)
        if word_list[i]==word_goal_list[i]:
            continue
        elif num>i:
            for n in range(abs(num-i)):
                word_list[num-n]=duplicate_list[num-1-n]
                word_list[num-1-n]=duplicate_list[num-n]
                duplicate_list=word_list[:]
                list_count.append((num-1-n,num-n))
                if word_list[i]==word_goal_list[i]:
                    break
        elif num<i:
            for n in range(abs(num-i)):
                word_list[i-n]=duplicate_list[i-1-n]
                word_list[i-1-n]=duplicate_list[i-n]
                duplicate_list=word_list[:]
                list_count.append((i-1-n,i-n))
                if word_list[i]==word_goal_list[i]:
                    break
    return list_count
        
print(sequence())