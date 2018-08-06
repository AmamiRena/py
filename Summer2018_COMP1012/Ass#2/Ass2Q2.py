# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
COUNT_1,COUNT_2,COUNT_3,COUNT_4,COUNT_5=0,0,0,0,0  #set var for counting
import csv
with open('Triangles.csv',newline='') as tri:
    handle=csv.reader(tri)  #set handle for opening file
    next(handle,None)
    for row in handle:
        if row[0]==row[1]==row[2]:
            COUNT_1+=1
        elif row[0]==row[1]!=row[2]:
            COUNT_2+=1
        elif row[0]!=row[1]==row[2]:
            COUNT_3+=1
        elif row[0]==row[2]!=row[1]:
            COUNT_4+=1
        elif row[0]!=row[1]!=row[2]:
            COUNT_5+=1
    print(' '*5+'Column Names'+' '*6+'|'+' '*2+'Count')
    print('-'*23+'+'+'-'*10)
    print('s1 = s2 = s3'+' '*11+'|'+' '*6+str(COUNT_1))
    print('s1 = s2 != s3'+' '*10+'|'+' '*6+str(COUNT_2))
    print('s1 != s2 = s3'+' '*10+'|'+' '*6+str(COUNT_3))
    print('s1 = s3 != s2'+' '*10+'|'+' '*6+str(COUNT_4))
    print('s1 != s2 != s3'+' '*9+'|'+' '*6+str(COUNT_5))
    print('-'*23+'+'+'-'*10)
    print()
    print(' '*5+'Column Names'+' '*6+'|'+' '*2+'Count')
    print('-'*23+'+'+'-'*10)
    print('Equilateral Triangles  |'+' '*6+str(COUNT_1))
    print('Isosceles Triangles    |'+' '*6+str(COUNT_2+COUNT_3+COUNT_4))
    print('Scalene Triangles      |'+' '*6+str(COUNT_5))


