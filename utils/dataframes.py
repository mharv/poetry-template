import pandas as pd
from typing import List


def keep_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns]
