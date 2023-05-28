test = "679518243543729618821634957794352186358461729216897534485276391962183475137945862"

"""
Nomenclatures:
    A grid is a string of 81 len; reading a sudoku board from left to right
    and top to bottom. A "0" represent an empty cell.
    Coordinates read from A to I as rows and 1 to 9 as columns.
    Each number occupies a cell. And a grid with coordinates assign is a board.
"""

def assign_coord(grid):
    cols = "12345689"
    rows = "ABCDEFGHI"

    cells = []
    for row in rows:
        for col in cols:
           cells.append(row+col)

    return dict(zip(cells, grid))

print(assign_coord(test))

def strip_coord(board):
    """
    Helper function to reverse the coordinates assignment
    """
    grid = ""

    for val in board.values():
        grid += val
    
    return grid

print(strip_coord(assign_coord(test)))
