'''
pseudocode
'''

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
        