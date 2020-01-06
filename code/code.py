'''
pseudocode
'''
from readconnections import readConnections

class Trains:
    def __init__(self,stops,total):
        self.p = stops/total

    def traject(self,number):
        # traject van a naar b, met mogelijke tussenstops en totale tijd
        # minimaliseren van functie K= p*10000-(T*100+Min)
        name_traject = number
        stops = {}
        time = int
        

class Connections:
    def __init__(self, origin, destination, time):
        
        # open connecties bestand

        # lees regels in

        # loop door regel
        self.origin = origin
        self.destination = destination
        self.time = time

    def __str__(self):
        return f"trein van {self.origin} naar {self.destination} van {self.time} minuten"

for station in readConnections():
    destinations = readConnections()[station]
    
    for optie in destinations:
        destination = optie[0]
        time = optie[1]
        connection = Connections(station, destination, time)
        print(connection)