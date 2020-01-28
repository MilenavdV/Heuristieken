class Traject:
    """ a traject is one list of continuous connections and stops, 
        representing one train line """
    def __init__(self):
        self.connections = []
        self.stops = []
        self.time = 0

    def addConnection(self, connection, time, timeframe):
        # voegt connectie toe aan traject wanneer tijd nog niet vol
        if (self.time + connection.time) <= timeframe:
            self.connections.append(connection)
            self.time += connection.time
            self.stops.append(connection.origin)
        return self.stops
    
    def __str__(self):
        # add final stop to traject
        self.stops.append(self.connections[-1].destination)
        print("")
        str = f"Traject langs {self.stops}"
        # adds every connection to string
        for i in self.connections: 
            str += i
        # adds travel time
        str += f"\n Totale reistijd van {self.time} minuten"
        return str