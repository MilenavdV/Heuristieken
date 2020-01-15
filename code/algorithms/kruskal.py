from code.algorithms.readconnections import readConnections
from code.classes.traject import Traject
from code.classes.connection import Connection
from code.classes.station import Station

import random
import csv

def union(parent, rank, x, y): 
    station1 = Station("data/ConnectiesHolland.csv")
    xroot_str = station1.findConnections(parent, x) 
    xroot = parent.index(xroot_str)
    yroot_str = station1.findConnections(parent, y) 
    yroot = parent.index(yroot_str)

    if rank[xroot] < rank[yroot]: 
        parent[xroot] = yroot_str 
    elif rank[xroot] > rank[yroot]: 
        parent[yroot] = xroot_str 
    else: 
        parent[yroot] = xroot_str
        rank[xroot] += 1
    return rank



def kruskal(file):
    stations, connections, connectionlist, connectionlist2 = readConnections(file)
    # print(stations,connections,connectionlist, connectionlist2)
    connectionlist3 =[]

    with open("data/ConnectiesHolland.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            connectionlist3.append([row[0],row[1],row[2]])
 
    station1 = Station(file)
    result = []
    graph = sorted(connectionlist3, key=lambda item: item[2])

    i = 0
    e = 0
    parent = []
    rank = []
    for station in stations:
        parent.append(station)
        rank.append(0) 

    while e < len(stations) - 1:
        u,v,w =  graph[i]
        i = i + 1
        x = station1.findConnections(parent, u)
        y = station1.findConnections(parent, v)
        
        if x != y: 
            e = e + 1     
            result.append([u,v,w])
            rank = union(parent, rank, x, y) 
            print(result,rank) 

    for u,v,weight  in result: 
        #print str(u) + " -- " + str(v) + " == " + str(weight) 
        print ("%d -- %d == %d" % (u,v,weight)) 


