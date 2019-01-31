# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import datetime as dt
import time as tm
print(tm.time())
dtnow=dt.datetime.fromtimestamp(tm.time())
print(dtnow)
print(dtnow.year,dtnow.month,dtnow.day,dtnow.hour,dtnow.minute,dtnow.second)
#print(dtnow.now)
delta=dt.timedelta(days=100)
print(delta)
today=dt.date.today()
print(today-delta)
print(today>today-delta)

#%%
class Person:
    department='law school'
    def set_name(self,new_name):
        self.name=new_name
    def set_location(self,new_location):
        self.location=new_location

p1,p2=Person(),Person()
p1.set_name('Jeanne darc')
p1.set_location('Orlean, France')
p2.set_name('Iskandar')
p2.set_location('Pella, Greece')
list1=[p1,p2]
print(list('{} lives in {} and is in {}'.format(p.name,p.location,p.department) for p in list1))

#%%
from functools import reduce

store1=[10.00,11.00,12.34,2.34]
store2=[9.00,11.10,12.34,2.01]
nearest=list(map(min,store1,store2))
print(nearest)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]
for person in people:
    print(split_title_and_name(person))
print([(lambda person:person.split()[0] + ' ' + person.split()[-1])(person) for person in people])
#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person:person.split()[0] + ' ' + person.split()[-1])(person))
#option 2
print()
print(list(map(split_title_and_name,people))==list(map(lambda person:person.split()[0] + ' ' + person.split()[-1],people)))
print()
def f(x): return x%2!=0 and x%3!=0
print(list(filter(f,range(2,25))))
def f(x): return x!='a'
print(list(filter(f,'abcdef')))
def add(x,y): return x+y
print(reduce(add,range(1,11),20))
print(reduce(lambda x,y:x+y, range(1,11)))

#%%
import numpy as np
mylist=[1,2,3]
x=np.array(mylist)
y=np.array([4,5,6])
print(x,y)
m=np.array([[1],[3]])
print(m.shape)
n=np.arange(0,30,2)
print(n)
print(n.reshape(3,5))
o=np.linspace(0,4,9)
print(o)
print(np.resize(o,(3,3)))
o.resize(3,3)
print(o)
print('eye',np.eye(3))
print('diag',np.diag(x))
print('diag',np.diag(y))
print(np.ones((3,2)))
print(np.zeros((2,3)))
print()
print(np.array([1,2,3]*3))
print(np.repeat(mylist,3))
print(np.repeat(y,3))
print(np.repeat(['a','b'],3))
p=np.ones((2,3),int)
print(p)
print(np.vstack((p,2*p)))
print(np.hstack([p,2*p]))
#operations
print('*'*20)
print('operations')
print(x+y)
print(x*y)
print(x**2)
print(x.dot(y)) #further
z=np.array([y,y**2])
print(z)
print(z.shape)
print(z.T)
print(z.T.shape)
print()
print(z.dtype)
z=z.astype('f')
print(z.dtype)
a=np.array([-4,-2,1,3,5])
print(a.sum())
print(a.max())
print(a.mean())
print(a.std())
print(a.argmax())
print(a.argmin())
#indexing/slicing
print('indexing/slicing')
s=np.arange(13)**2
print('s =',s)
print(s[0],s[4],s[0:3],s[1:5],s[-4:-1],s[-5::-2])
r=np.arange(36)
r.resize((6,6))
print('r =',r)
print('r[2,2]',r[2,2])
print('r[3,3:6]',r[3,3:6])
print('r[:2,:-1]',r[:2,:-1])
print('r[-1,::2]',r[-1,::2])
print('r[r>30]',r[r>30])
print(r.reshape(36)[::7])
print(r[2:4,2:4])
r[r>30]=30
print(r)
r2=r[:3,:3]
print(r2)
r2[:]=0
print(r2)
print(r)
print()
r_copy=r.copy()
print(r_copy)
#iterating over arrays
test=np.random.randint(0,10,(4,3))
print(test)
for row in test:
    print(row)
for i in range(len(test)):
    print(test[i])
for i,row in enumerate(test):
    print(i,row)
test2=test**2
print(test2)
for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)


