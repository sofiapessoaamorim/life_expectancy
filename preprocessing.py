"""Module to preprocess data in a DataFrame
"""
from pandas import DataFrame

def preprocess_data(df_raw: DataFrame)-> DataFrame:
    """Preprocesses raw data in a DataFrame by splitting a column and cleaning column names.

    Args:
        df_raw: The input DataFrame containing the raw data.

    Returns:
        df_split: A preprocessed DataFrame with split columns and cleaned column names.
    """
    df_raw[["unit", "sex","age", "region"]] = (
        df_raw["unit,sex,age,geo\\time"].str.split(",", expand=True)
    )
    df_split = df_raw.drop(columns=["unit,sex,age,geo\\time"], inplace=False)
    df_split.columns = df_split.columns.str.strip()
    return df_split

