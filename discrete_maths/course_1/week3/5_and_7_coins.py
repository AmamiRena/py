# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
list_no=[6,8,9,11,13]
list_yes=[5,7,10,12,14]
def test_fs():
    for i in range(15,100):
        test_if=False
        for n in range(5):
            test_num=i-list_yes[n]
            if test_num in list_yes:
                list_yes.append(i)
                test_if=True
                break
        if test_if==False:
            list_no.append(i)
    return max(list_no)
print(test_fs())
print(list_yes)
print(list_no)

amount=int(input('Enter an integer 24~1000: '))
def change(amount):
    list_comp=[]
    for n_5 in range(201):
        for n_7 in range(143):
            if 5*n_5+7*n_7>=amount:
                break
        if 5*n_5+7*n_7==amount:
            break            
    for n in range(n_5):
        list_comp.append(5)
    for n in range(n_7):
        list_comp.append(7)
    return list_comp

print(change(amount))