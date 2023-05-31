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

rows = "ABCDEFGHI"
cols = "123456789"

cells = gen_cells(rows, cols)
unit_list = ([permutate(r, c) for r in ["ABC", "DEF", "GHI"] for c in ["123", "456", "789"]] +
         [permutate(rows, col) for col in cols] +
         [permutate(row, cols) for row in rows])

units = dict([(cell, [unit for unit in unit_list if cell in unit]) for cell in cells])
peers = dict([(cell, set(flatten(units[cell])) - set([cell])) for cell in cells])

def assign_n_check(group, cell, to_delete):
    """
    Assign the value to a cell and the delete the value from the other members'
    possible values list. Check all the other member of its unit or 
    its peer for the remaining possible values, whether the value is the only
    possible value in any of the cell of the group,. group can be either 
    unit or peer.
    """

    possible_vals_remain = group[cell].replace(to_delete, "")

    for possible_val in possible_vals_remain:
        for to_check in possible_val:
            elim_n_check(group, cell, to_check) 

def elim_n_check(group, cell, to_delete):
    """
    Delete the value that is taken by another cell of the group. Check if the
    remaining possible values reduce to zero. If so, call assign_n_check to 
    assign and to recursively check the other members
    """

    possible_vals_remain = group[cell].replace(to_delete, "")

    if len(group[cell]) == 1:
        assign_n_check(group, cell, group[cell][0])

    for peer in peers[cell]:
        elim_n_check(group, peer, group[cell][0])

    for unit in units(cell):
        elim_n_check(group, unit, group[cell][0])

