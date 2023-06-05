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

test = "180023000942500008060010092209840000608395040300067850806000027407002900001700004"

parsed_board = [[test[i*j] for j in range(9)] for i in range (9)]

rows = defaultdict(set)
cols = defaultdict(set)
grids = defaultdict(set)
tracker = deque([])

for i in range(9):
    for j in range(9):
        if parsed_board[i][j] != "0":
           rows[i].add(parsed_board[i][j])
           cols[j].add(parsed_board[i][j])
           grids[(i//3, j//3)].add(parsed_board[i][j])
        else:
           tracker.append((i, j))

def dfs_search():

    if len(tracker) == 0:
        return True

    i, j = tracker[0]

    for n in [str(x) for x in range(1, 10)]:
        if (n not in rows[i]) and (n not in cols[j]) and (n not in grids[(i//3, j//3)]):
            rows[i].add(n)
            cols[j].add(n)
            grids[(i//3, j//3)].add(n)
            tracker.popleft()
            
            if dfs_search():
                return True
            else:
                rows[i].discard(n)
                cols[j].discard(n)
                grids[(i//3, j//3)].discard(n)
                tracker.appendleft((i,j))

    return False



dfs_search()

print(rows)

