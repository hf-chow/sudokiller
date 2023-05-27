import pandas as pd

"""
TO DO:
    - Implement col, row, grid check
    - Wrap into a class Checker
"""

PQ_PATH = "../../data/sudoku_pq/sudoku.parquet"

data = pd.read_parquet(PQ_PATH)

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

    for i in range(0, 9):
        for key, val in grid_ky:
            if key%9 == i:
                nine.append(val)
        if len(nine) == 9:
            if check_9(nine):
                nine = []
            else:
                return False
    return True
                

