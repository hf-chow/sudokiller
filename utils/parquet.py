import pyarrow.csv 
import pyarrow.parquet

SRC_PATH = "../../data/sudoku.csv"
DST_PATH = "../../data/sudoku_pq/sudoku.parquet"

convert_options = pyarrow.csv.ConvertOptions(
        column_types={"puzzle": pyarrow.string(), "solution": pyarrow.string()})

data = pyarrow.csv.read_csv(SRC_PATH, convert_options=convert_options)
data = pyarrow.parquet.write_table(data, DST_PATH)
