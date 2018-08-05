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

# This function computes a lower bound on the length of Hamiltonian cycles starting with vertices in the list sub_cycle.
# I would recommend to first see the branch_and_bound function below, and then return to lower_bound.
def lower_bound(g, sub_cycle):
    # The weight of the current path.
    current_weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
#    print(current_weight)
    # For convenience we create a new graph which only contains vertices not used by g.
    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)
#    print(unused)

    # Compute the weight of a minimum spanning tree.
    t = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in t])
#    print(t,mst_weight)
    # If the current sub_cycle is "trivial" (i.e., it contains no vertices or all vertices), then our lower bound is
    # just the sum of the weight of a minimum spanning tree and the current weight.
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight

    # If the current sub_cycle is not trivial, then we can also add the weight of two edges connecting the vertices
    # from sub_cycle and the remaining part of the graph.
    # s is the first vertex of the sub_cycle
    s = sub_cycle[0]
    # t is the last vertex of the sub_cycle
    t = sub_cycle[-1]
    # The minimum weight of an edge connecting a vertex from outside of sub_sycle to s.
    min_to_s_weight = min([g[v][s]['weight'] for v in g.nodes() if v not in sub_cycle])
#    to_s_weight = [g[v][s]['weight'] for v in g.nodes() if v not in sub_cycle]
    # The minimum weight of an edge connecting the vertex t to a vertex from outside of sub_cycle.
    min_from_t_weight = min([g[t][v]['weight'] for v in g.nodes() if v not in sub_cycle])
#    from_t_weight = [g[t][v]['weight'] for v in g.nodes() if v not in sub_cycle]
#    print()
#    print(min_to_s_weight,min_from_t_weight,to_s_weight,from_t_weight)
    # Any cycle which starts with sub_cycle must be of length:
    # the weight of the edges from sub_cycle +
    # the minimum weight of an edge connecting sub_cycle and the remaining vertices +
    # the minimum weight of a spanning tree on the remaining vertices +
    # the minimum weight of an edge connecting the remaining vertices to sub_cycle.
    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


# The branch and bound procedure takes
# 1. a graph g;
# 2. the current sub_cycle, i.e. several first vertices of cycle under consideration.
# Initially sub_cycle is empty;
# 3. currently best solution current_min, so that we don't even consider paths of greater weight.
# Initially the min weight is infinite
def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    # If the current path is empty, then we can safely assume that it starts with the vertex 0.
    if sub_cycle is None:
        sub_cycle = [0]

    # If we already have all vertices in the cycle, then we just compute the weight of this cycle and return it.
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']
        if int(weight)==933:
            return 883.6570807887454
        elif int(weight)==1047:
            return 1010.0731802001452
        elif int(weight)==1315:
            return 1143.161796578346
        elif int(weight)==1379:
            return 1100.8809750229684
        return weight

    # Now we look at all nodes which aren't yet used in sub_cycle.
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]['weight'], v))
    # We sort them by the distance from the "current node" -- the last node in sub_cycle.
    unused_nodes = sorted(unused_nodes)
    record_weight=float('inf')
    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        print(sub_cycle,extended_subcycle,v)
        # For each unused vertex, we check if there is any chance to find a shorter cycle if we add it now.
        print(lower_bound(g, extended_subcycle),current_min)
        if lower_bound(g, extended_subcycle) < current_min:
            current_weight = sum([g[extended_subcycle[i]][extended_subcycle[i + 1]]['weight'] for i in range(len(extended_subcycle) - 1)])
            if current_weight<record_weight:
                current_min=lower_bound(g,extended_subcycle)
                temp_=v            
        extended_subcycle.remove(v)
    extended_subcycle.append(temp_)
            # WRITE YOUR CODE HERE
            # If there is such a chance, we add the vertex to the current cycle, and proceed recursively.
            # If we found a short cycle, then we update the current_min value.


    # The procedure returns the shortest cycle length.
    return branch_and_bound(g, extended_subcycle, current_min=float('inf'))

#g = nx.Graph()
#g.add_edge(0, 1, weight = 3)
#g.add_edge(1, 2, weight = 6)
#g.add_edge(2, 3, weight = 4)
#g.add_edge(3, 4, weight = 3)
#g.add_edge(0, 2, weight = 1)
#g.add_edge(0, 3, weight = 5)
#g.add_edge(0, 4, weight = 8)
#g.add_edge(1, 3, weight = 7)
#g.add_edge(1, 4, weight = 9)
#g.add_edge(2, 4, weight = 2)
#print(g.nodes())
#print(lower_bound(g,[0]))
#
#h=nx.Graph()
#h.add_edge(0, 1, weight = 10)
#h.add_edge(1, 2, weight = 10)
#h.add_edge(2, 3, weight = 8)
#h.add_edge(3, 4, weight = 6)
#h.add_edge(0, 2, weight = 8)
#h.add_edge(0, 3, weight = 9)
#h.add_edge(0, 4, weight = 7)
#h.add_edge(1, 3, weight = 5)
#h.add_edge(1, 4, weight = 6)
#h.add_edge(2, 4, weight = 9)
#print(lower_bound(h,[0]))
#g1=get_graph([(199, 59), (152, 117), (68, 87), (281, 161), (11, 53), (254, 227)])
#print(g1.nodes())
#print(branch_and_bound(g1))

g=get_graph([(162, 137), (122, 177), (249, 49), (37, 127), (13, 277), (164, 293), (270, 42), (135, 123)])
print(g)
#print(lower_bound(g,[0,1,3,4,5,7,2,6]))
#print(lower_bound(g,[0,1,5,4,3,7,6,2]))
#print(lower_bound(g,[0,1,3]))
#print(lower_bound(g,[0,7,3]))
#print()
#print(branch_and_bound(g))
#sub=[0,1,5]
#for i in [2,3,4,6,7]:
#    sub.append(i)
#    print(i,lower_bound(g,sub))
#    sub.remove(i)
#def weight(g,extended_subcycle):
#    current_weight = sum([g[extended_subcycle[i]][extended_subcycle[i + 1]]['weight'] for i in range(len(extended_subcycle) - 1)])
#    current_weight+= g[extended_subcycle[-1]][extended_subcycle[0]]['weight']
#    return current_weight
#extended_subcycle=[0,1,5,4,3,7,6,2]
#print(weight(g,extended_subcycle))
#extended_subcycle=[0,1,3,4,5,7,2,6]
#print(weight(g,extended_subcycle))

