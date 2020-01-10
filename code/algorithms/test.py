from statistics import mode
connections = ['Gouda-Den Haag Centraal', 'Den Haag Centraal-Leiden Centraal', 'Leiden Centraal-Heemstede-Aerdenhout', 'Heemstede-Aerdenhout-Haarlem', 'Haarlem-Beverwijk', 'Beverwijk-Castricum', 'Castricum-Zaandam', 'Zaandam-Amsterdam Sloterdijk', 'Amsterdam Sloterdijk-Haarlem', 'Dordrecht-Rotterdam Centraal', 'Rotterdam Centraal-Schiedam Centrum', 'Schiedam Centrum-Delft', 'Delft-Den Haag Centraal', 'Leiden Centraal-Schiphol Airport', 'Schiphol Airport-Amsterdam Zuid', 'Amsterdam Zuid-Amsterdam Amstel', 'Amsterdam Amstel-Amsterdam Centraal', 'Amsterdam Centraal-Amsterdam Sloterdijk', 'Amsterdam Sloterdijk-Amsterdam Zuid', 'Heemstede-Aerdenhout-Leiden Centraal', 'Leiden Centraal-Alphen a/d Rijn', 'Alphen a/d Rijn-Gouda', 'Gouda-Rotterdam Alexander', 'Rotterdam Alexander-Rotterdam Centraal', 'Zaandam-Beverwijk', 'Castricum-Alkmaar', 'Alkmaar-Hoorn', 'Hoorn-Zaandam']
double = []
def changeDirection(verbinding):
    newB = str(verbinding)[:str(verbinding).find("-")]
    newA = str(verbinding)[str(verbinding).find("-") + 1:]
    bToA = newA + "-" + newB
    return bToA

for i in connections:
    double.append(i)
    double.append(changeDirection(i))
    
print(mode(double))
print(double)