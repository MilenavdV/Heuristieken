import csv

connections = {}

with open('data/ConnectiesHolland.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # van a naar b
        if row[0] not in connections:
            connections[row[0]] = []
        thistuple = (row[1], row[2])
        connections[row[0]].append(thistuple)

        # van b naar a 
        if row[1] not in connections:
            connections[row[1]] = []
        thistuple = (row[0], row[2])
        connections[row[1]].append(thistuple)
        
print(connections)