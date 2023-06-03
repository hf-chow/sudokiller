from utils.draw import draw
"""
A DFS brute force sovler. But it would take impossibly long to solve
a board if it is purely solved by brute force search
Borrowing idea from Peter Norvig's incredible blog post:
    Generate units and peers for each cells
    Implement the following strategies to eliminate possible solutions:
        -If a cell has only one possible value, then eliminate that value 
        from the peers
        -If a unit has only one possible place for a value, the put the value 
        there
    The two strategies interact with each other. The 2nd strat will trigger 
    the 1st strat to remove a possible value from peers and each peers losing
    a possible value may trigger another a 2nd strat and so on. This is
    constraint propagation.
"""
def flatten(l):
    return [i for j in l for i in j]

def permutate(X, Y):
    return [x+y for x in X for y in Y]

def gen_cells(rows, cols):
    return permutate(rows, cols)

def some(seq):
    for e in seq:
        if e:
            return e
    return False

rows = "ABCDEFGHI"
cols = "123456789"

cells = gen_cells(rows, cols)
unit_list = ([permutate(r, c) for r in ["ABC", "DEF", "GHI"] for c in ["123", "456", "789"]] +
         [permutate(rows, col) for col in cols] +
         [permutate(row, cols) for row in rows])

units = dict([(cell, [unit for unit in unit_list if cell in unit]) for cell in cells])
peers = dict([(cell, set(flatten(units[cell])) - set([cell])) for cell in cells])

def parse_board(board):

    parsed_board = dict(zip(cells, board))
    for cell in parsed_board:
        if parsed_board[cell] == "0":
            parsed_board[cell] = "123456789"

    return parsed_board

def assign(group, cell, to_delete):

    possible_vals_remain = group[cell].replace(to_delete, "")

    if all(elim(group, cell, possible_val) for possible_val in possible_vals_remain):
        return group
    else:
        return False

#    for possible_val in possible_vals_remain:
#        if not elim(group, cell, possible_val):
#            return False
#        else:
#            return group

def elim(group, cell, to_delete):

    if to_delete not in group[cell]:
        return group

    group[cell] = group[cell].replace(to_delete, "")

    if len(group[cell]) == 0:
        return False
    elif len(group[cell]) == 1:
        if not all(elim(group, cell_, group[cell]) for cell_ in peers[cell]):
            return False

    for unit in units[cell]:
        possible_cells = [cell for cell in unit if to_delete in group[cell]]
        if len(possible_cells) == 1:
            if not assign(group, possible_cells[0], to_delete):
                return False
        elif len(possible_cells) == 0:
            return False

    return group

def search(group):

    if group is False:
        return False 

    if all(len(group[cell]) == 1 for cell in cells): 
        return group 

    _, cell = min((len(group[cell]), cell) for cell in cells if len(group[cell]) > 1)

    return some(search(assign(group.copy(), cell, to_delete)) 
		for to_delete in group[cell])

def solve(board):
    board = parse_board(board)
    return search(board)

test = "085923476942576138763418592259841763678395241314267859896154327437682915521739684"

print(solve(test))



#test = "180023000942500008060010092209840000608395040300067850806000027407002900001700004"
