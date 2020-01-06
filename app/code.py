'''
pseudocode
'''

Class Trains():
    def __init__(self,stops,total,maxtime):
        self.p = stops/total
        self.time = maxtime

        
    def traject(self,number):
        # traject van a naar b, met mogelijke tussenstops en totale tijd
        # minimaliseren van functie K= p*10000-(T*100+Min)
        name_traject = number
        stops = {}
        time = int
        
