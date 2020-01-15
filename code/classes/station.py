from code.algorithms.readconnections import readConnections


class Station:
    def __init__(self, file):
        self.stations, self.connections, self.connectionlist, self.connectionslist2 = readConnections(file)
        

    def findConnections(self,parent,station):
        # print(station,parent)
        index = parent.index(station)
        if parent[index] == station:
            return station
        return self.findConnections(parent, parent[index])  


    def __str__(self):
        return f"{self.stations}"
            