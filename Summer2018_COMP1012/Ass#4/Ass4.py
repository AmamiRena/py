# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def generatePoints(aa,bb,interval):
    '''
    generate numpy array
    starts with aa, ends with bb, step interval
    '''
    return np.arange(aa,bb,interval)

def evalFunction(xx):
    '''
    get y value for from input array
    '''
    YY=(xx-1)**(5/2)*(2/3) #calculate y axis
    assert len(YY)==len(xx)
    return YY

def calculateSegmentDists(xx,yy):
    '''
    calculate segment distances between consecutive points
    '''
    EUCLID_DIS=[np.sqrt((xx[i_]-xx[i_+1])**2+(yy[j_]-yy[j_+1])**2) for i_,j_ in zip(range(len(xx)-1),range(len(yy)-1))]  #distance
    EUCLID_DIS=np.array(EUCLID_DIS)
    assert len(xx)==len(EUCLID_DIS)+1
    return EUCLID_DIS

def calculateCurveLen(segDists):
    '''
    calculate sum of curve lengths
    '''
    return sum(segDists)

def calculateArea(segDists,yy):
    '''
    calculate areas of segments and sum it up
    '''
    assert len(segDists)+1==len(yy)
    area=[np.pi*(yy[i_]+yy[i_+1])*segDists[j_] for i_,j_ in zip(range(len(yy)-1),range(len(segDists)))]
    area=np.array(area)
    return sum(area)

def main():
    '''
    processing function
    '''
    STARTLIST=[i_ for i_ in range(1,100,10)] #generate starting list
    XVAL=np.array([generatePoints(x_,x_+10,1) for x_ in STARTLIST]) # 'x's
    YVAL=np.array([evalFunction(x_) for x_ in XVAL]) #array of 'y's
    SEGMEN=np.array([calculateSegmentDists(x_,y_) for x_,y_ in zip(XVAL,YVAL)]) #segments of distances
    CURLEN=np.array([calculateCurveLen(seg) for seg in SEGMEN]) #array of len
    CURAREA=np.array([np.array(calculateArea(seg,y_)) for seg,y_ in zip(SEGMEN,YVAL)]) #array of areas
    printValues(1,100,CURLEN,CURAREA)
    return plotFunction(XVAL[0],YVAL[0])
    
def printValues(starts,ends,lengths,areas):
    '''
    print dataframe
    '''
    assert starts==1 and ends==100
    assert len(lengths)==len(areas)
    print('start/end |length (m)|area (m^2)')
    print('-'*11+'+'+'-'*10+'+'+'-'*10)
    for i_ in range(len(lengths)):
        print(('{:2d}'+' ... '+'{:3d}'+' |'+'{:.3E}'+' |'+'{:.3E}').format(i_+1,i_+10,lengths[i_],areas[i_]))
        print('-'*11+'+'+'-'*10+'+'+'-'*10)

def plotFunction(xx,yy):
    '''
    use pyplot to plot one of the graph
    '''
    fig = plt.figure()
    plt.clf()
    plt.plot(xx,yy,'b')
    plt.plot((xx[-1],xx[-1]),(0,yy[-1]),'b')
    plt.scatter(xx,yy)
    plt.title('Shape of the function')
    plt.xlabel('x value')
    plt.ylabel('2/3 X (x-1) ^ (5/2)')
    plt.xlim(-10,20)
    plt.ylim(0,185)
    plt.yticks(range(0,186,25))
    plt.show()
    fig.savefig('AmamiAss4.png')
    return ''

print(main())



