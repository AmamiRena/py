# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

def readData(filename):
    '''
    read data from reducedDim.csv and return a 2d array
    '''
    with open(filename) as handle:
        FILE=csv.reader(handle) #entry of the csv file
        DATA=[] #initial storage list
        BOOLEAN=0 #works as on/off
        for row in FILE:
            if BOOLEAN==0:
                BOOLEAN=1
                for ii in range(len(row)):
                    DATA.append(list())
                DATA[0].append(float(row[0]))
                DATA[1].append(float(row[1]))
            else:
                DATA[0].append(float(row[0]))
                DATA[1].append(float(row[1]))
        DATA=np.asarray(DATA)
    return DATA

def readLabels(filename):
    '''
    read label names from conds.csv and return a list of array
    '''
    with open(filename) as handle:
        FILE=csv.reader(handle) #entry of label csv file
        CONDS=[] #initial storage list for label names
        for row in FILE:
            CONDS.append(''.join(row))
    return np.array(CONDS)

def plotByGroup(data,conds,fmtstrings):
    '''
    using the parameters the function takes and plot a graph
    '''
    assert data.shape==(2, 16377)
    assert conds.shape==(16377,)
    assert len(fmtstrings)==2
    XVAL,YVAL=data[0],data[1] #set values for x,y axis
    colordict,shapedict={},{} #set dict for color and shape
    labels=np.unique(conds)
    for i_,j_,k_ in zip(labels,fmtstrings[0],fmtstrings[1]):
        colordict[i_]=j_
        shapedict[i_]=k_
    colors=np.vectorize(colordict.get)(conds) #colors of corresponding labels
    fig=plt.figure(figsize=(24,20),dpi=60) #dpi of the pictures
    plt.clf()
    for ii in labels:
        plt.scatter(XVAL[conds==ii],YVAL[conds==ii],c=colors[conds==ii],label=ii,marker=shapedict[ii])
    plt.title('Distribution of SNP Data for Wheats in Two Dimensional Space')
    plt.xlabel('Most Significant Dimension')
    plt.ylabel('Second Most Significant Dimension')
    plt.legend(loc='best') #location of the labels
    fig.savefig('FangzhouXuAss5.png')
    fig.show()
    return ''

def main():
    '''
    combine those 3 functions together
    '''
    data=readData('reducedDim.csv')
    conds=readLabels('conds.csv')
    fmtstrings=[['b','g','c','r','m','y','k','b'],['.','o','v','x','*','^','P','+']]
    return plotByGroup(data,conds,fmtstrings)
    
print(main())



