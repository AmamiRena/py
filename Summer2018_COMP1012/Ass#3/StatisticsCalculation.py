# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def calculateMean(data):
    '''
    find mean values here
    '''
    assert type(data)==list
    LIST_MEAN=[] #list of mean values of different columns
    for n_ in data:
        assert type(n_)==list
        AVG_=sum(n_)/len(n_) #mean value
        LIST_MEAN.append(AVG_)
    return LIST_MEAN

def calculateStdDev(data, mean):
    '''
    calculate standard deviations here
    '''
    assert type(data)==list and type(mean)==list
    LIST_STD=[] #list of std values of different columns
    for n_ in range(len(data)):
        SUM_=0 #sum of numerators of stds
        for i_ in data[n_]:
            assert type(i_)==float
            SUM_+=(i_-mean[n_])**2
        STD_=(SUM_/len(data[n_]))**(1/2) #standard deviations here
        LIST_STD.append(STD_)
    return LIST_STD

def findMin(data, mean):
    '''
    find minimum values here
    '''
    assert type(data)==list and type(mean)==list
    LIST_MIN=[] #list of minimum values of different columns
    for n_ in range(len(data)):
        LIST_MIN.append(min(data[n_]))
    return LIST_MIN

def findMax(data, mean):
    '''
    find maximum values here
    '''
    assert type(data)==list and type(mean)==list
    LIST_MAX=[] #list of maximum values of different columns
    for n_ in range(len(data)):
        LIST_MAX.append(max(data[n_]))
    return LIST_MAX

def findPassedFailed(data, cutoffMark):
    '''
    find number of pass/fail students
    '''
    assert type(data)==list and type(cutoffMark)==int
    TOTAL_,FAILNUM=0,0 #sum of midterm and final marks, number of fail students
    for i_ in range(len(data[0])):
        for n_ in range(len(data)):
            TOTAL_+=data[n_][i_]
        if TOTAL_<cutoffMark:
            FAILNUM+=1
        TOTAL_=0
    return len(data[0])-FAILNUM,FAILNUM

