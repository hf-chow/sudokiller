import utils.coord
"""
Visualization function to draw the board
Importing coord.py to enable the draw function to work on both grid and board

Feels bad to use two count in a single function
The amount of loops in this function also makes me uncomfortable
Revisit this function
"""

def draw(grid):
    if type(grid) == "dict":
        grid = strip(grid)

    rows = [[] for i in range(9)]
    hor_sep = "---"*3 + "+" + "---"*3 + "+" + "---"*3

    for i in range(0, 81, 9):
        vals = [" " + j + " " for j in grid[i:i+9]]
        rows[int(i/9)] = ""

        count = 0
        for val in vals:
            rows[int(i/9)] += val   
            count += 1
            if count == 3 or count == 6:
                rows[int(i/9)] += "|"

    count = 0
    for row in rows:
        print(row)
        count += 1
        if count == 3 or count == 6:
            print(hor_sep)
