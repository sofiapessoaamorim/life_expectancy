"""Module to load data from a csv file into a DataFrame
"""
import pandas as pd
from pandas import DataFrame
from .preprocessing import preprocess_data

def load_data()-> DataFrame:
    """Function to load life expectancy data
    
    Returns:
        df_split: dataframe with split columns
    """
    df_raw = load_csv_file()
    df_split = preprocess_data(df_raw)
    return df_split


def load_csv_file()-> DataFrame:
    """Load a csv file into a DataFrame

    Returns: a DataFrame containing the data from the csv file.
    """
    file_path = "data/eu_life_expectancy_raw.tsv"
    return pd.read_csv(file_path, sep="\t")

