import pandas as pd

def check_board(grid):
    if check_row(grid) & check_col(grid) & check_grid(grid):
        print("Correct solution!")
        return True
    else:
        print("Incorrect!")
        return False

def check_9(seq):
    if set(seq) == set("123456789"):
        if len(set(seq))==9:
            return True
    return False

def check_row(grid):
    nine = []
    
    for i in grid:
        nine.append(i)

        if len(nine) == 9:
            if check_9(nine):
                nine = []
            else:
                return False
    return True

def check_col(grid):
    grid_ky = enumerate(grid)
    nine = []

    for i in range(9):
        for key, val in grid_ky:
            if key%9 == i:
                nine.append(val)
        if len(nine) == 9:
            if check_9(nine):
                nine = []
            else:
                return False
    return True
                
def check_grid(grid):
    """
    Horrible implementation, but it works.
    NEED to visit this lol
    """
    grid_ky = enumerate(grid)
    nines = [[] for i in range(9)]

    for key, val in grid_ky:
        for i in range(3):
            if (key//3 == i) or (key//3 == i+3) or (key//3 == i+6):
                if len(nines[i]) != 9:
                    nines[i].append(val)

        for j in range(3, 6):
            if (key//3 == j+6) or (key//3 == j+9) or (key//3 == j+12):
                if len(nines[j]) != 9:
                    nines[j].append(val)

        for k in range(6, 9):
            if (key//3 == k+12) or (key//3 == k+15) or (key//3 == k+18):
                if len(nines[k]) != 9:
                    nines[k].append(val)
            
    for nine in nines:
        if not check_9(nine):
            return False
    return True
