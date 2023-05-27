import pandas as pd

FILE_PATH = "../data/sudoku_pq/sudoku.parquet"

data = pd.read_parquet(FILE_PATH)

print(data.head())
