__ALGORITHMS__

In this file you can find descriptions of the algorithms used in the project.

- Random: randomize.py
- Greedy: greedy.py
- Kruskal: kruskal.py
- Least Connections Method: connectioncount.py
- Iterative deepening search: iterativedeepening.py

The algorithms all have a similar set up, yet different methods and approaches have been used to determine which connection to use next. 

**Random**

*Creates a random solution for the timetable of the Dutch Railway*

Necessary arguments: connections file, maximum trains allowed, timeframe

- First of all the algorithms decides randomly how many trajectories it is going to use
- Secondly it starts off by creating a trajectory and choosing a random starting connection
- It then changes to the new origin
- With the new origin it finds the possible connections that can be added from there
- Then it chooses and adds a random new connection while adding "None" to the possibilities which represents a chance of ending the trajectory and not adding a new connection; it does this until either there are zero possible connections or when "None" is drawn from the possibilities

**Greedy**

*Creates a solution by choosing the connection with the least amount of minutes*

Necessary arguments: connections file, maximum trains allowed, timeframe

- Starts off by choosing a random starting connection which has not been used in a traject before
- Changes to the new origin
- Finds new possible connections while excluding the previous connection (to prevent the trajectory going back and forth over the same connection) and chooses the fastest connection out of the possibilities to add it to the trajectory
- It keeps on doing this until the trajectory reaches its timeframe or when it reaches a station that only has the previous added connection as possibility

**Kruskal**

*Creates a solution based on the method described by Kruskal:
Start off by picking the shortest unused connection and connect this with the shortest adjacent connection *

Necessary arguments: connections file, maximum trains allowed, timeframe

- Starts off by choosing the shortest unused connection
- Changes to the new origin
- Finds new possible connections while excluding the previous connection (to prevent the trajectory going back and forth over the same connection) and chooses the fastest connection out of the possibilities to add it to the trajectory
- It keeps on doing this until the trajectory reaches its timeframe or when it reaches a station that only has the previous added connection as possibility

**Least Connections Method**

*Creates a solution by choosing the connection with the least amount of connections as starting point*

Necessary arguments: connections file, maximum trains allowed, timeframe

- Starts off by creating a trajectory that starts with an unused connection that has the least amount of follow-up connections  
- Changes to the new origin and searches new possibilities 
- Continues the trajectory by adding the fastest *unused* option out of the possibilities: unused means it has not been used in any other trajectories before
- This keeps on going until it runs out of possibilities or whenever the fastest unused option is already used in the current track

**Iterative deepening search**

*Creates a solution by using a three step down iterative deepening method combined with a hillclimber*

Necessary arguments: connections file, maximum trains allowed, timeframe, failed_attemps

- Starts off by choosing a random starting connection which has not been used in a trajectory before
- Changes to new origin and finds the possible follow-up connections
- For every possible follow up connection it looks into their follow-up connections and also in the follow-up follow-up follow-ups connections; does this sentence make sense?
- While doing the previous explained step the algorithm keeps track of the added score for every combination of the three step follow-up 
- It then chooses out of the first follow up the one that allows to find our highest found added score in the previous step
- The algorithm keeps on doing this until it cannot find any follow up options (since the trajectory reached its timeframe) or whenever all possible added scores found are all negative: meaning it would bring the score down
- Whenever a trajectory is finished the new total score is calculated, if this new score is higher than the previous total score (before this trajectory was created) it gets accepted, otherwise the trajectory will be deleted/ignored and the variable "failed_attemps" increases

This process runs until a given treshold of failed attempts is reached
