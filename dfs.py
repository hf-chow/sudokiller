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
    parsed_board = [[board[i*j] for j in range(9)] for i in range (9)]

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

    return rows, cols, grids, tracker

def dfs_search(rows, cols, grids, tracker):

    if len(tracker) == 0:
        return rows, cols, grids, tracker

    i, j = tracker[0]

    for n in [str(x) for x in range(1, 10)]:
        if (n not in rows[i]) and (n not in cols[j]) and (n not in grids[(i//3, j//3)]):
            rows[i].add(n)
            cols[j].add(n)
            grids[(i//3, j//3)].add(n)
            tracker.popleft()
            
            if dfs_search(rows, cols, grids, tracker):
                return rows, cols, grids, tracker
            else:
                rows[i].discard(n)
                cols[j].discard(n)
                grids[(i//3, j//3)].discard(n)
                tracker.appendleft((i,j))

    return False

def solve(board):
    rows, cols, grids, tracker = parse_board(board)

    dfs_search(rows, cols, grids, tracker)

    return rows, cols, grids, tracker


test = "180023000942500008060010092209840000608395040300067850806000027407002900001700004"

rows, cols, grids, tracker = solve(test)

print(rows)

