# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
class vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,self_2):
        return vector((self.a*10+self_2.a*10)/10,(self.b*10+self_2.b*10)/10)
    def __sub__(self,self_2):
        return vector((self.a*10-self_2.a*10)/10,(self.b*10-self_2.b*10)/10)
    def __str__(self):
        return '({},{})'.format(self.a,self.b)
    def test(self,self_2):
        if self.a==self_2.a and self.b==self_2.b:
            return 'Same'
        else:
            return 'Not same'

A_=vector(3.5,1.2)
B_=vector(-2.7,-3.2)
C_=vector(4.2,2.8)
print('A=',A_,'B=',B_)
print('B-A=',B_-A_)
print('C-B=',C_-B_)
print('C-A=',C_-A_)
print('(C-B)+(B-A)=',(C_-B_)+(B_-A_))
print('Are they same or not ? ',vector.test(C_-A_,(C_-B_)+(B_-A_)))

#%%
list_1=[]
for i in range(10):
    if i==10: break
    _INPUT=input('Enter sth here: ')
    try:
        _NUM=float(_INPUT)
        i+=1
        list_1.append(_NUM)
    except:
        i+=1
        list_1.append(_INPUT)
    print(list_1)
print()
print(list_1)
print('*'*25)

import random
list_2=[]
list_3=[]
for i in range(5):
    if i==5: break
    list_2.append(random.uniform(0,100))
    list_3.append(random.uniform(0,100))
    i+=1
print(list_2,sum(list_2))
print(list_3)
list_sub=[]
for i in range(len(list_2)):
    list_sub.append(list_2[i]-list_3[i])
print(list_sub)
print('*'*25)

list_4=[]
for i in range(1,11):
    list_4.append(i)
print(list_4)
print('*'*25)

_Count=int(input('Enter an integer: '))
list_5=list()
for i in range(_Count):
    odd_num=1+i*2
    list_5.append(odd_num)
print(list_5)
print('*'*25)

list_coor=[]
for n in range(5):
    X_coor=float(input('Enter x axis: '))
    Y_coor=float(input('Enter y axis: '))
    Coor_=X_coor,Y_coor
    list_coor.append(Coor_)
print(list_coor)

#%%
X_=set('15373592')
Y_=set('247069')
print(X_,Y_)
list_1=list()
list_2=list()
for element in X_&Y_:
    list_1.append(element)
print(list_1)
for i in X_-Y_:
    list_2.append(i)
print(list_2)

#%%
dict_sports={'Winnipeg': ['Jets', 'Blue Bombers', 'Goldeyes' ,'Moose'], 'Vancouver': ['Canucks', 'Lions', 'Whitecaps'], 'Hamilton': ['Tiger Cats', 'Cardinals']} 
dict_sports['Montreal']=['''I don't know''']
check=input('Enter a city: ')
print(dict_sports.get(check, 'Nothing found'))

