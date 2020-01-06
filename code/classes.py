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
