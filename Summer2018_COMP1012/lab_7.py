# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import time
def printInformation():
    return 'Programmed By: AmamiRena \nID: 888888 \nDate: '+time.strftime('%m/%d/%Y', time.localtime())
print(printInformation())

#%%
def multiplication(a,b):
    print(a*b)
print(multiplication(2,3))

#%%
def multiplication(a,b):
    return a*b
print(multiplication(2,3))

#%%
LIST=[5, 10, 100, 25, 200]
def findSquaredDiff(a):
    meanValue=sum(a)/len(a)
    listPrint=list()
    for l_ in a:
        sqDF=0
        sqDF+=(l_-meanValue)**2
        listPrint.append(sqDF)
    return listPrint
print(findSquaredDiff(LIST))