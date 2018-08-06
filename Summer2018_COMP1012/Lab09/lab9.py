# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
x1 = np.random.random((5,5))
x2 = np.zeros((10,10),dtype=int)
x3 = np.reshape(np.arange(1,13,dtype=int), (4,3))
print(x1)
print(x2)
print(x3)

#%%
import numpy as np
nums = np.reshape(np.arange(1,13,dtype=int), (4,3))
print("nums:\n{0}".format(nums))    
print(nums.shape)
print(nums[3,2])
print(nums[2,3])

#%%
import numpy as np
nums = np.reshape(np.arange(1,13,dtype=int), (4,3))
print(nums)
nums2 = nums[1:3,1:3]
print(nums2)
nums[1:3,1:3] = np.zeros(nums2.shape)
print(nums)

#%%
import numpy as np
array1=np.zeros([5,5],dtype=int)
print(array1)
array1[1:4,1:4]=np.reshape(np.arange(1,10,dtype=int),(3,3))
print(array1)

array2=np.arange(1,11,dtype=float)
print(array2)
print(np.array(list(array2*i for i in range(1,11))))

#%%
import numpy as np
def det2(m):
    if m.shape!=(2,2):
        return None
    return m[0,0]*m[1,1]-m[0,1]*m[1,0]

def det3(m):
    if m.shape!=(3,3):
        return None
    return m[0,0]*det2(m[1:3,1:3])-m[0,1]*det2(m[1:3,::2])+m[0,2]*det2(m[1:3,0:2])

def areInverses(m1,m2):
    temp1,temp2=m1.shape,m2.shape
    if temp1!=temp2:
        return None
    if temp1[0]!=temp1[1] or temp2[0]!=temp2[1]:
        return None
    r1=np.matmul(m1,m2)
    r2=np.eye(temp1[0])
    result=np.isclose(r1,r2,rtol=1e-10)
    result1=result[result==True]
    if len(result1)==0:
        return False
    return True
a=np.array([[4,7],[2,6]])
b=np.array([[.6,-.7],[-.2,.4]])
print(areInverses(a,b))






