Create a program in the language of your preference that:

Accepts three inputs (Brewers (B), Beer Drinkers (D), and Boat Capacity (C)), and
Outputs a series of boat trips and passengers to allow all brewers and beer drinkers to traverse to the opposite bank, if such a series exists.


B brewers and D beer drinkers must cross the Grand River using a boat, in order to bring the beer to a shop where the beer drinkers can legally purchase it. However, you must maintain the following constraints:

The boat can only carry C people at a time.
The boat cannot cross the river without someone to row it.
The number of beer drinkers (D) can never outnumber the brewers (B) on either bank or in the boat. Otherwise the beer drinkers will steal the beer and drink it without purchasing it.


The boat and all people start on the side of the river without the store.

Output should list the number of brewers and beer drinkers in each boat trip. For example, given three boat trips:

1 Brewer and 1 Beer Drinker ride to the other side.
0 Brewers and 1 Beer Drinker ride to the other side.
2 Brewers and 0 Beer Drinkers ride to the other side.


The output must be as follows:

B=1, D=1

B=0, D=1

B=2, D=0
