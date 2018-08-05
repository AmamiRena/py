# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import networkx as nx
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g

def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    return sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + g[cycle[0]][cycle[-1]]['weight']
# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    t = nx.minimum_spanning_tree(g)
    sort_t=list(nx.dfs_preorder_nodes(t,0))
    print(sort_t)
    
    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # which returns a Minimum Spanning Tree of the graph g
#    list(nx.dfs_preorder_nodes(t, 0))
    # You also might want to use the command "list(nx.dfs_preorder_nodes(graph, 0))"
    # which gives a list of vertices of the given graph in depth-first preorder.

    return cycle_length(g,sort_t)
g=get_graph([(162, 137), (122, 177), (249, 49), (37, 127), (13, 277), (164, 293), (270, 42), (135, 123)])
print(approximation(g))


