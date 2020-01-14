from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.classes.station import Station

import random

def test(file):
    stations, connections, connectionlist, connectionlist2 = readConnections(file)
    # print(stations)

def kruskal(file):
    stations, connections, connectionlist, connectionlist2 = readConnections(file)
    station1 = Station(file)
    result = []
    graph = []
    graph = sorted(connectionlist2, key=lambda item: item[2])

    # print(graph)

    i = 0
    e = 0
    parent = []
    rank = []
    for station in stations:
        parent.append(station)
        rank.append(0) 
    # print(parent)
    while e < len(graph) - 1:
        # print(i)
        u,v,w =  graph[i] 
        i = i + 1
        # print(station1)
        x = station1.findConnections(parent, u)
        x = parent[x]
        y = station1.findConnections(parent, v)
        y = parent[y]

        if x != y: 
            print(x,y)
            e = e + 1     
            result.append([u,v,w]) 
            union(parent, rank, x, y)   

    for u,v,weight  in result: 
        #print str(u) + " -- " + str(v) + " == " + str(weight) 
        print ("%d -- %d == %d" % (u,v,weight)) 


def union(parent, rank, x, y): 
    station1 = Station("data/ConnectiesHolland.csv")
    xroot = station1.findConnections(parent, x) 
    yroot = station1.findConnections(parent, y) 
    # xroot = parent.index(xroot_str)
    # yroot = parent.index(yroot_str)
    # Attach smaller rank tree under root of  
    # high rank tree (Union by Rank) 
    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot 

    # If ranks are same, then make one as root  
    # and increment its rank by one 
    else : 
        parent[yroot] = xroot 
        rank[xroot] += 1

