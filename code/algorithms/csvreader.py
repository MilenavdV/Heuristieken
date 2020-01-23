import csv
from code.algorithms.functions import formula

def checkScore(file, connections):
    connections = connections
    used_connections = []
    trains = 0
    total_minutes = 0

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row == []:
                continue
            if 'Traject' not in row[0] and 'Total' not in row[0]:
                aToB = row[0] + '-' + row[1]
                bToA = row[1] + '-' + row[0]
                total_minutes += int(row[6])
                if aToB not in used_connections:
                    used_connections.append(aToB)
                    used_connections.append(bToA)
                
            elif 'Traject' in row[0]:
                trains += 1
    p = len(used_connections) / len(connections)
    score = formula(p, trains, total_minutes)
    print(p)
    return score

