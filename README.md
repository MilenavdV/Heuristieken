# Heuristieken - All rights reserved

__RAILNL__

Milena van der Velde  
Philip Lankhorst  
Wouter de Boer  

__PROBLEEM__

*Summary*

De dienstregeling van de NS voor het treinverkeer in Nederland kan op vele manieren ingevuld worden. Het probleem dat hierbij komt kijken is het vinden van de meest efficiente invulling. De NS heeft een bepaalde scorefunctie die gemaximaliseerd moet worden terwijl alle stations in Nederland met elkaar verbonden moeten zijn binnen een bepaalde tijdsframe. 

*Extended Info*

- De lijnvoering: Wat zijn de trajecten waarover de treinen gedurende de dag heen en weer rijden?
- De dienstregeling: hoe laat vertrekken de treinen van de stations over de trajecten?
- Het materieelrooster: welk treinstel en welke wagons zijn op welk moment op welke plaats?
- Het personeelsrooster: zijn alle treinen bemand door tenminste één bestuurder en twee conducteurs?

Deze case gaat over het eerste deel, het maken van de lijnvoering. Meer specifiek: over de lijnvoering van intercitytreinen. Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn dan het opgegeven tijdsframe.

Voorbeeld: Het traject [Castricum , Zaandam , Hoorn , Alkmaar] is een traject met een duur van 59 minuten, en zou dus binnen het tijdseframe van een uur passen.
