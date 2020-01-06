from readconnections import readConnections
import random

connections = {}
trajecten = {}

class Traject:
    def __init__(self):
        self.connections = []
        self.stops = []
        self.time = 0
        self.timeframe = 120

    def addConnection(self, connection, time):
        # traject van a naar b, met mogelijke tussenstops en totale tijd
        # minimaliseren van functie K= p*10000-(T*100+Min)
        if (self.time + time) < self.timeframe:
            self.connections.append(connection)
            self.time += time
            self.stops.append(connection.origin)
    
    def __str__(self):
        print("")
        print(f"Traject langs {self.stops}")
        print("")
        for i in self.connections: 
            print(i)
        print("")
        return f"Totale reistijd van {self.time} minuten"

class Connection:
    def __init__(self, origin, destination, time):
        self.origin = origin
        self.destination = destination
        self.time = time

    def __str__(self):
        return f"Trein van {self.origin} naar {self.destination} van {self.time} minuten"






""" Function for finding possible connections from given startpoint(origin) 
    while excluding the previous station """

def findConnections(origin, previous_station):
    options = []
    for i in connections:
        if origin == connections[i].origin and connections[i].destination != previous_station:
            options.append(i)
    return options


def main():
    # create Connection objects
    for station in readConnections():
        destinations = readConnections()[station]
        
        for optie in destinations:
            destination = optie[0]
            time = optie[1]
            connection = Connection(station, destination, int(time))
            key = connection.origin + "-" + connection.destination
            connections[key] = connection

    # create Traject departing from Den Helder
    traject = Traject()
    traject.addConnection(connections["Den Helder-Alkmaar"], connections["Den Helder-Alkmaar"].time)

    for i in range(0,50):
        new_origin = traject.connections[-1].destination
        previous_station = traject.connections[-1].origin
        options = findConnections(new_origin, previous_station)

        if len(options) != 0:
            new_connection = random.choice(options)
       
        traject.addConnection(connections[new_connection], connections[new_connection].time)
    
    print(traject)

if __name__ == "__main__":
    main()