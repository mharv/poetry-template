from typing import List
import pandas as pd


def read_excel_file(file_path) -> pd.DataFrame:
    return pd.read_excel(file_path)


def read_excel_files(file_paths) -> List[pd.DataFrame]:
    return [read_excel_file(file_path) for file_path in file_paths]
