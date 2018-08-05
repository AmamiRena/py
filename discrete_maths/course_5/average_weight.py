# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import networkx as nx
from itertools import permutations
import math

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    Result=[]
    count=0
    store={}
    # Iterate through all permutations of n vertices
    #for p in permutations(range(n)):
        # Write your code here.
    for paths_ in permutations(range(n)):
        count+=1
        length_=0
        for n in range(len(paths_)):
            if n==max(range(len(paths_))):
                length_+=g[paths_[n]][paths_[0]]['weight']
                break
            length_+=g[paths_[n]][paths_[n+1]]['weight']
        Result.append(length_)
        store[paths_]=length_
    print(store)
    print(min(Result))
    return [sum(Result)/count]
def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g

def average1(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))
    average_weight=2*sum_of_weights/(n-1)
    return average_weight

#g1=get_graph([(178, 212), (287, 131), (98, 156)])
#print(average(g1))
#print(average1(g1))
g2=get_graph([(231, 91), (7, 21), (226, 276), (11, 266)])
#print(average(g2))
g3=get_graph([(162, 137), (122, 177), (249, 49), (37, 127), (13, 277), (164, 293), (270, 42), (135, 123)])
print(average(g3))


