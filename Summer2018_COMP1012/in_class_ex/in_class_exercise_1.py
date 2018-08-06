# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
def findSumOfSameDigits(numVec):
    vector=np.unique(np.array(numVec))
    vector_count=list(numVec.count(i) for i in vector)
    total=[i*j for i,j in zip(vector,vector_count)]
    result=[(i,j) for i,j in zip(vector,total)]
    return result


def findBiggestSum(sumOfSameDigitsVec):
    total_list=[i[1] for i in sumOfSameDigitsVec]
    maximum=max(total_list)
    inde=total_list.index(maximum)
    return sumOfSameDigitsVec[inde]

temp1=[5,5,2,3]
print(findSumOfSameDigits(temp1))
print(findBiggestSum(findSumOfSameDigits(temp1)))

