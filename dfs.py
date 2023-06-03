from collections import defaultdict, deque

"""
The strategy is to use DFS and backtracking to solve the puzzle.
Three hashmaps are created for rows, cols, and grids three units will keep
track of all the position that are already on the board. A deque will keep 
track of all the empty cells.

We will use DFS to recursively using the seen list and try to assign a value 1 
to 9 in a way that it is not inside any of the hashmaps. If success, we will
pop the cell from the list and go to the next one. Once we ran into a 
contradiction, we need to backtrack and put the value back in the list and 
delete the latest key from hashmaps.

This strategy will ensure a correct solution, since this is a smarter version
of brute force search. But this could take extremely long for very hard puzzles.
"""
