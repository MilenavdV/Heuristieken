from code.algorithms.readconnections import readConnections


class Station:
    def __init__(self, file):
        self.stations, self.connections, self.connectionlist, self.connectionslist2 = readConnections(file)
        

    def findConnections(self,station):
        pass
        

    def __str__(self):
        return f"{self.stations}"
            