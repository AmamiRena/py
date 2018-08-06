# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import numpy as np
'''
E1
'''
print(list(range(15)))
print(np.arange(15))
print(np.arange(100,111))
print(np.random.random(4))
print(np.zeros(5))
print(np.ones(5,int))

xa=np.arange(0.1,0.91,0.05)
x1=np.linspace(0.1,0.9,17)
print(xa,'\n',x1)
print(xa==x1)
print(xa[0]-x1[0],xa[2]-x1[2])

#%%
import numpy as np
'''
E2
'''
xx=np.arange(1,51)
print(1/xx)
oo=np.ones(1)
zz=np.zeros(1)
print(np.hstack((zz,oo)*50))
aa=np.arange(5)
bb=np.random.random(5)
print(aa**2+bb**2)
degree=np.arange(0,91)
print(degree)
print(np.sin(degree*np.pi/180))
odd_num=np.arange(1,26,2)
print(odd_num.cumsum())

#%%
import numpy as np
'''
E3
'''
two_h=np.zeros(200,dtype=int)
one_h=np.zeros(100,dtype=int)
hh=np.arange(0,201)
print(np.hstack((two_h,hh,one_h)))

def dynamic(x,y=np.array(()),z=0):
    assert type(x)==int
    temp=np.array(list(map(lambda i:i, [i for i in range(z+1)])))
    z+=1
    y=np.append(y,temp)
    if len(y)>=x:
        return y[:x]
    return dynamic(x,y,z)
print(dynamic(100))

xx=np.arange(1,11)
xx=1/xx
print(np.hstack((xx,xx[::-1])))




