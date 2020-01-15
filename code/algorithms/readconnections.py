import csv
from ..classes.connection import Connection

def readConnections(file):
    stations = {}

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            # van a naar b
            if row[0] not in stations:
                stations[row[0]] = []
            thistuple = (row[1], row[2])
            stations[row[0]].append(thistuple)

            # van b naar a 
            if row[1] not in stations:
                stations[row[1]] = []
            thistuple = (row[0], row[2])
            stations[row[1]].append(thistuple)

    # create Connection objects
    connections = {}

    connectionlist2 = []
    for station in stations:
        # find all connections from station
        destinations = stations[station]
        for destination in destinations:
            connectionlist2.append([station, destination[0], int(destination[1])])

        for option in destinations:
            destination = option[0]
            time = option[1]
            # create Connection object
            connection = Connection(station, destination, int(time))
            key = connection.origin + "-" + connection.destination
            # add Connection to dictionary
            connections[key] = connection


    
    # initialise list
    connectionslist = []
    
    for i in connections:
        # create list of all connections
        connectionslist.append(i)

    return stations, connections, connectionslist, connectionlist2