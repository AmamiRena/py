# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def printCSVResults(headings, means, stdDevs, mins, maxs,passed, failed):
    assert type(headings)==tuple
    assert type(means)==list
    assert type(stdDevs)==list
    assert type(mins)==list and type(maxs)==list
    assert type(passed)==int and type(failed)==int
    print(' Column Names |'+' '*5+'Mean'+' '*6+'|'+' Std Deviation |',end='')
    print(' Highest Score |'+' Lowest Score')
    print('-'*14+'+'+'-'*15+'+'+'-'*15+'+'+'-'*14+'-'+'+'+'-'*15)
    for n_ in range(len(headings)):
        print(' '*(14-len(headings[n_]))+headings[n_]+'|'+' '*(15-len('{:.2f}'.format(means[n_])))+'{:.2f}'.format(means[n_])+'|'+' '*(15-len('{:.2f}'.format(stdDevs[n_])))+'{:.2f}'.format(stdDevs[n_])+'|'+' '*(15-len('{:.2f}'.format(maxs[n_])))+'{:.2f}'.format(maxs[n_])+'|'+' '*(15-len('{:.2f}'.format(mins[n_])))+'{:.2f}'.format(mins[n_]))
        print('-'*14+'+'+'-'*15+'+'+'-'*15+'+'+'-'*14+'-'+'+'+'-'*15)
    print('Total number of students: {}'.format(passed+failed))
    print('Passed in the exam: {}'.format(passed))
    print('FAILed in the exam: {}'.format(failed))
    return '\nProgrammed by Amami Rena\nActuarial Maths'

import csv
def readCSVFile(fileName):
    total_LIST=[]#create a total list for containing tons of sub lists
    with open(fileName,'r',newline='') as handle:#open the file with read mode
        headings=tuple(handle.readline().strip().split(','))
        for n_ in range(len(headings)):
            total_LIST.append(list())
        content=csv.reader(handle)#content of the file deprived of headings
        for row in content:
            for n_ in range(len(headings)):
                total_LIST[n_].append(float(row[n_]))
        assert type(total_LIST)==list
        assert type(total_LIST[0])==list
        return headings,total_LIST

