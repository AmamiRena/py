# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def findArmStrongNumber(num):
    '''
    test whether the input number is a armstrong number
    '''
    assert type(num)==int
    D_SUM=0 #sum of cube of different digits
    for l_ in str(num):
        D_SUM+=int(l_)**3
    if num==D_SUM: 
        return True
    else: 
        return False

import random
def selectArmstrong(armstrongs):
    '''
    generate a random number from the given list
    '''
    assert type(armstrongs)==list
    return random.choice(armstrongs)

def predictArmstrong(selectedArmstrong):
    '''
    check whether the input if a armstrong number or not.
    If not continue the loop forever
    '''
    assert type(selectedArmstrong)==int
    INPUT_NUM=int(input('Make a prediction: '))
    assert INPUT_NUM>0 and INPUT_NUM<=1000
    COUNT_=0 #number of attempts
    RECORD_HIGH,RECORD_LOW=1000,0 #record high/low bound of input
    while True:
        if INPUT_NUM>selectedArmstrong:
            RECORD_HIGH=INPUT_NUM
            print('Your predict armstrong number is too high')
            INPUT_NUM=int(input('Enter a value between {} and {}: '.format(RECORD_LOW,RECORD_HIGH)))
        elif INPUT_NUM<selectedArmstrong:
            RECORD_LOW=INPUT_NUM
            print('Your predict armstrong number is too low')
            INPUT_NUM=int(input('Enter a value between {} and {}: '.format(RECORD_LOW,RECORD_HIGH)))
        else:
            print('Your prediction is correct!!!')
            COUNT_+=1
            return 'You need {} attempts'.format(COUNT_)
        COUNT_+=1
    
def main():
    '''
    contructed to connect all functions
    '''
    ARM_LIST=[] #create list for containing armstrong number
    for n_ in range(1000):
        if findArmStrongNumber(n_)==True:
            ARM_LIST.append(n_)
    SELECT_=selectArmstrong(ARM_LIST) #generate selected armstrong number
    return predictArmstrong(SELECT_)

print(main())
    



