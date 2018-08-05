# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def dg(g):
    n=g.number_of_nodes()
    t=[[float('inf')]*(1<<n)for _ in range(n)]
    t[0][1]=0
    for s in range(1<<n):
        if sum(((s>>j)&1)for j in range(n))<=1 or not (s&1):
            continue
        for i in range(1,n):
            if not ((s>>1)&1):
                continue
            for j in range(n):
                if j==i or not((s>>j)&1):
                    continue
                t[i][s]=min(t[i][s],t[j][s^(1<<n)]+g[i][j]['weight'])
    return min(t[i][(1<<n)-1]+g[0][i]['weight']for i in range(1,n))
    

