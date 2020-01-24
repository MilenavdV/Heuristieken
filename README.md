# Heuristieken - All rights reserved

__RAILNL__

Milena van der Velde  
Philip Lankhorst  
Wouter de Boer  

__PROBLEEM__

## Samenvatting

De dienstregeling van de NS voor het treinverkeer in Nederland kan op vele manieren ingevuld worden. Het probleem dat hierbij komt kijken is het vinden van de meest efficiente invulling. De NS heeft een bepaalde scorefunctie die gemaximaliseerd moet worden terwijl alle stations in Nederland met elkaar verbonden moeten zijn binnen een bepaalde tijdsframe. 

## Uitgebreide informatie 

- De lijnvoering: Wat zijn de trajecten waarover de treinen gedurende de dag heen en weer rijden?
- De dienstregeling: hoe laat vertrekken de treinen van de stations over de trajecten?
- Het materieelrooster: welk treinstel en welke wagons zijn op welk moment op welke plaats?
- Het personeelsrooster: zijn alle treinen bemand door tenminste één bestuurder en twee conducteurs?

Deze case gaat over het eerste deel, het maken van de lijnvoering. Meer specifiek: over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn dan het opgegeven tijdsframe.

Voorbeeld: Het traject [Castricum , Zaandam , Hoorn , Alkmaar] is een traject met een duur van 59 minuten, en zou dus binnen het tijdsframe van een uur passen.

  
## Proces

Als eerste stap hebben we een random algoritme geschreven, dit gaf geen geweldige resultaten. In het geval van Holland kregen we nog redelijke scores door het te laten lopen tot we een _p_ van 1 gevonden hadden, dit was bij heel Nederland niet het geval.  
Na random probeerden we een greedy algoritme; de code koos de kortste connectie en zocht steeds de kortste nog ongebruikte connectie vanaf het volgende station.  
Op basis van Minimum Spanning Tree theorie probeerden we met het Kruskal-algoritme een oplossing te vinden, deze had echter een erg lage score. Dit komt doordat Kruskal bedoeld is om de route met de laagste kosten te vinden, zonder daarbij de proportie te maximaliseren. Zo kregen we dus een erg efficiënte route langs alle stations, maar niet een van hoge kwaliteit.  
Om te zorgen dat de stations in de uithoeken (Den Helder, Vlissingen, Enschede) altijd bereikt worden, schreven we vervolgens een algoritme dat steeds het station met de minste connecties koos. Hierdoor kregen we een score van ongeveer 4200. Om deze score te verbeteren schreven we een nieuw algoritme waarbij steeds een aantal stations vooruit gekeken wordt en de route met de hoogste marginale kwaliteit gekozen wordt. Hieronder een boxplot ter vergelijking van de algoritmes, waarbij Greedy Lookahead 2 stations vooruit kijkt. De boxplots zijn gebaseerd op 100 simulaties per algoritme. 

![Vergelijking van vijf methodes.]('/doc/vergelijking.png')

Door later drie stations vooruit te kijken hebben we de score met greedy lookahead nog een stuk omhoog gekregen naar 7175.
