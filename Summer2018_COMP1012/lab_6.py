# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
mark_list=[]
print('Enter 5 marks: ')
for n in range(5):
    mark=int(input())
    mark_list.append(mark)
result=sum(mark_list)/len(mark_list)
print('You get ',end='')
if result>=90:
    print('A')
elif result>=80:
    print('B')
elif result>=70:
    print('C')
elif result>=60:
    print('D')
elif result>=40:
    print('E')
else:
    print('F')

#%%
def gcd(a,b):
    assert type(a)==int and type(b)==int
    if a<b:
        return gcd(b,a)
    assert a>b
    c=a%b
    if c!=0:
        return gcd(b,c)
    else:
        return b
values = [(13, 3), (25, 5), (112,56), (20, 232)]
for i in range(len(values)):
    print('GCD of',values[i][0],'and',values[i][1],'is',gcd(values[i][0],values[i][1]))

#%%
valueList = ['Bill', 'billy', 'Doll', 'cold', 'Hot']
print(valueList)
for xx in range(len(valueList)-1):
    for yy in range(xx+1, len(valueList)):
        if valueList[xx] > valueList[yy]:
                valueList[xx], valueList[yy] = valueList[yy], valueList[xx]
print(valueList)
valueList.sort()
print(valueList)
