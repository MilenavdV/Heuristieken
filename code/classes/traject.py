class Traject:
    def __init__(self):
        self.connections = []
        self.stops = []
        self.time = 0


    def addConnection(self, connection, time, timeframe):
        # traject van a naar b, met mogelijke tussenstops en totale tijd
        # minimaliseren van functie K= p*10000-(T*100+Min)
        if (self.time + connection.time) < timeframe:
            self.connections.append(connection)
            self.time += connection.time
            self.stops.append(connection.origin)
        return self.stops
    
    def __str__(self):
        print("")
        print(f"Traject langs {self.stops}")
        print("")
        for i in self.connections: 
            print(i)
        print("")
        return f"Totale reistijd van {self.time} minuten"