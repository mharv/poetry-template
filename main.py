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
    # concat all the dataframes
    final_df = pd.concat(processed_dfs)

    final_df["Rent/SF/Yr(£)"] = final_df["Rent/SF/Yr"].apply(
        lambda x: x.replace("£", "")
    )
    final_df.drop("Rent/SF/Yr", axis=1, inplace=True)

    final_df["Rent/SF/Yr(£)min"] = final_df["Rent/SF/Yr(£)"].apply(
        lambda x: x.split("-")[0].strip()
    )
    final_df["Rent/SF/Yr(£)max"] = final_df["Rent/SF/Yr(£)"].apply(
        lambda x: x.split("-")[1].strip() if "-" in x else x
    )
    final_df.drop("Rent/SF/Yr(£)", axis=1, inplace=True)

    print(final_df.head())


if __name__ == "__main__":
    main()
