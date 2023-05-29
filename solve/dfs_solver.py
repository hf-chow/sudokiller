"""
A DFS brute force sovler. But it would take impossibly long to solve
a board if it is purely solved by brute force search
Borrowing idea from Peter Norvig's incredible blog post:
    Generate units and peers for each cells
    Implement the following strategies to eliminate possible solutions:
        -If a square has only one possible value, then eliminate that value 
        from the peers
        -If a unit has only one possible place for a value, the put the value 
        there
    The two strategies interact with each other. The 2nd strat will trigger 
    the 1st strat to remove a possible value from peers and each peers losing
    a possible value may trigger another a 2nd strat and so on. This is
    constraint propagation.
"""

def permutate(X, Y):
    return [x+y for x in X for y in Y]

def gen_cells(rows, cols):
    return permutate(rows, cols)


rows = "ABCDEFGHI"
cols = "123456789"

cells = gen_cells(rows, cols)
units = [permutate(r, c) for r in ["ABC", "DEF", "GHI"] for c in ["123", "456", "789"]] 
unit_list = []

for cell in cells:
    for unit in units:
        if cell in unit:
            unit_list.append((cell, unit))

unit_dict = dict(unit_list)

