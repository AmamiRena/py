# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

def generateX(a,b,c):
    xval=np.linspace(a,b,c)
    return xval

def calculateY(xval):
    yval1=xval**2+1
    yval2=xval**3+1
    yval3=xval**4+1
    return yval1,yval2,yval3

def plotGraph(xval,y,funcName):
    y1,y2,y3=y[0],y[1],y[2]
    plt.plot(xval,y1,label=funcName[0][0][0])
    plt.plot(xval,y2,label=funcName[0][1][0])
    plt.plot(xval,y3,label=funcName[0][2][0])
    plt.scatter(xval,y1)
    plt.scatter(xval,y2)
    plt.scatter(xval,y3)
    plt.title(funcName[1][0][0])
    plt.legend(loc='best')
    plt.xlabel(funcName[2][0][0])
    plt.ylabel(funcName[2][1][0])
    plt.show()
    return ''

def main():
    x=generateX(1,5,10)
    y1,y2,y3=calculateY(x)
    assert len(x)==len(y1) and len(x)==len(y2) and len(x)==len(y3)
    y=np.array([y1,y2,y3])
    label1='1+x^2'
    label2='1+x^3'
    label3='1+x^4'
    label=[[label1],[label2],[label3]]
    title='Shapes of Different Functions'
    xla='x values'
    yla='function outputs'
    axi=[[xla],[yla]]
    funcName=[label,[title],axi]
    return plotGraph(x,y,funcName)

print(main())









