import csv
from code.algorithms.functions import formula

def checkScore(file, connections):
    """ Calculates the score of a csv file. """
    # initialize objects
    connections = connections
    used_connections = []
    trains = 0
    total_minutes = 0

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            # skips empty rows
            if row == []:
                continue
            # adds connections to used connections item and adds time to total time
            if 'Traject' not in row[0] and 'Total' not in row[0]:
                aToB = row[0] + '-' + row[1]
                bToA = row[1] + '-' + row[0]
                total_minutes += int(row[6])
                if aToB not in used_connections:
                    used_connections.append(aToB)
                    used_connections.append(bToA)
                
            # adds 1 train upon finding new train
            elif 'Traject' in row[0]:
                trains += 1
    # calculates p
    p = len(used_connections) / len(connections)
    
    # calculates score
    score = formula(p, trains, total_minutes)
    return score

