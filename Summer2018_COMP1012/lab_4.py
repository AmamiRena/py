# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
num=int(input('Enter the size: '))
for i in range(1,num+1):
    print(' '*(num-i),end='')
    for n in range(1,i):
        print(n,end='')
    print(i)

num=int(input('Enter the size: '))
for i in range(num,0,-1):
    print(' '*(num-i),end='')
    for n in range(1,i):
        print(n,end='')
    print(i)

#%%
count=int(input('Enter an integer here: '))
print(' Element Number  | Value')
fibo_dict={}
for i in range(1,count+1):
    if i==1:
        sum_=0
        fibo_dict[i]=sum_
        print('{:9d}'.format(i)+' '*8+'|'+'{:7d}'.format(sum_))
    elif i==2:
        sum_+=1
        fibo_dict[i]=sum_
        print('{:9d}'.format(i)+' '*8+'|'+'{:7d}'.format(sum_))
    else:
        sum_=fibo_dict[i-2]+fibo_dict[i-1]
        fibo_dict[i]=sum_
        print('{:9d}'.format(i)+' '*8+'|'+'{:7d}'.format(sum_))
    
#%%
domain=int(input('Enter a range to find prime numbers: '))
for n in range(2,domain+1):
    prime=True
    for i in range(2,n):
        if n%i==0:
            prime=False
            break
    if prime==True:
        print(n,'is a prime number.')

