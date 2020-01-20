from functions import formula
import csv

total_minutes=0
connections = []
i = 1
with open('dienstregeling-1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row == []:
            continue
        if f'Traject {i}' in row:
            i +=1
            # print(row)
            continue
        if 'Total' in row[0]:
            # print(int(row[1]))
            total_minutes +=int(row[1])
            # print(total_minutes)
            continue
        if f"{row[0]}-{row[1]}" not in connections:
            # print(f"{row[0]}-{row[1]}")
            connections.append(f"{row[0]}-{row[1]}")

            # pass
        # print(row[0])

        p = 88/89
# print(total_minutes)

print(formula(p,12,total_minutes))

        

