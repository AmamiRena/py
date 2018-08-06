# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
file=input('Enter file name: ')  #type the file name
file='Grades.csv'
LIST=[]  #whole list for overall storage
NUM_,NUM_FAIL=0,0 #counting total/FAIL students
print(' Column Names |'+' '*5+'Mean'+' '*6+'|'+' Std Deviation |',end='')
print(' Highest Score |'+' Lowest Score')
print('-'*14+'+'+'-'*15+'+'+'-'*15+'+'+'-'*14+'-'+'+'+'-'*15)
import csv
with open(file,newline='') as grade: #for simplicity
    headings = tuple(grade.readline().strip().split(',')) #read the first line
    for n_ in range(len(headings)):
        LIST.append(list())
    handle=csv.reader(grade) #read the followings
    for row in handle:
        for n_ in range(len(headings)):            
            LIST[n_].append(float(row[n_]))
        NUM_+=1
    for n_ in range(len(headings)):
        AVG_=sum(LIST[n_])/len(LIST[n_])  #average for iteration
        SUM_=0   #value count for iteration
        for NUMM_ in range(len(LIST[n_])):
            SUM_+=(LIST[n_][NUMM_]-AVG_)**2
        STD_=(SUM_/len(LIST[n_]))**(1/2)  #standard deviations
        print(' '*(14-len(headings[n_]))+headings[n_]+'|'+' '*(15-len('{:.2f}'.format(AVG_)))+'{:.2f}'.format(AVG_)+'|'+' '*(15-len('{:.2f}'.format(STD_)))+'{:.2f}'.format(STD_)+'|'+' '*(15-len('{:.2f}'.format(max(LIST[n_]))))+'{:.2f}'.format(max(LIST[n_]))+'|'+' '*(15-len('{:.2f}'.format(min(LIST[n_]))))+'{:.2f}'.format(min(LIST[n_])))
        print('-'*14+'+'+'-'*15+'+'+'-'*15+'+'+'-'*14+'-'+'+'+'-'*15)
    SUM_=0
    for n_ in range(NUM_):
        for i_ in range(len(headings)):
            SUM_+=LIST[i_][n_]
        if SUM_<51:
            NUM_FAIL+=1
        SUM_=0
    print('Total number of students: {}'.format(NUM_))
    print('Passed in the exam: {}'.format(NUM_-NUM_FAIL))
    print('FAILed in the exam: {}'.format(NUM_FAIL))
    print()
    print('Programmed by Amami Rena')
    print('Department of Actuarial Mathematics')






