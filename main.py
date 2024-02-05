from utils import functions, files, dataframes
from typing import List
import pandas as pd


def get_files() -> List[pd.DataFrame]:
    return files.read_excel_files(
        [
            "./data/Export 1.xlsx",
            "./data/Export 2.xlsx",
            "./data/Export 3.xlsx",
            "./data/Export 4.xlsx",
        ]
    )


def main() -> None:

    cols = [
        "Property Address",
        "PropertyType",
        "Rent/SF/Yr",
        "Total Available Space (SF)",
        "Longitude",
        "Latitude",
    ]

    processed_dfs = list(map(lambda x: dataframes.keep_columns(x, cols), get_files()))

    print(processed_dfs[0].head())
    print(processed_dfs[1].head())
    print(processed_dfs[2].head())
    print(processed_dfs[3].head())


if __name__ == "__main__":
    main()
