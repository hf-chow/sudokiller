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

def parse_board(board):
    """
    To parse the board and convert it into a list[list[string]]
    """
    parsed_board = [[board[i*j] for j in range(9)] for i in range (9)]

    return parsed_board

rows = defaultdict(set)
cols = defaultdict(set)
grids = defaultdict(set)
empty = deque()

test = "085923476942576138763418592259841763678395241314267859896154327437682915521739684"

parsed_board = parse_board(test)

for i in range(9):
    for j in range(9):
        if parsed_board[i][j] != "0":
            rows[i].add(parsed_board[i][j])
            cols[j].add(parsed_board[i][j])
            grids[(i//3, j//3)].add(parsed_board[i][j])

print(rows)
print(cols)
print(grids)
