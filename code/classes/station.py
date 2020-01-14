from code.algorithms.readconnections import readConnections


class Station:
    def __init__(self, file):
        self.stations, self.connections, self.connectionlist, self.connectionslist2 = readConnections(file)
        
    def findConnections(self,parent,station):
        index = parent.index('Schiedam Centrum')
        # print(index)
        try:
            if parent[index] == station:
            # if station == 'Schiedam Centrum':
            #     print(station)
                return index
        except:
            pass   
        return self.findConnections(parent, parent[index])  
        # return self.stations[station]

    def __str__(self):
        return f"{self.stations}"
            