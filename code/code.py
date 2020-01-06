'''
pseudocode
'''

Class Trains():
    def __init__(self,stops,total):
        self.p = stops/total

    def traject(self,number):
        # traject van a naar b, met mogelijke tussenstops en totale tijd
        # minimaliseren van functie K= p*10000-(T*100+Min)
        name_traject = number
        stops = {}
        time = int
        

class Connections():
    def __init__(self):
        self.dic = {}
        connections = open('data/ConnectiesHolland.csv')
        self.list = connections.read().splitlines()
        print(self.list)
        for line in self.list:
            p = line.split(",")
            print(p)
            self.dic[line[0]].append([line[1], line[2]])
        connections.close()
    
if __name__ == "__main__":
    dictionary = Connections()
    print(dictionary.dic)
        