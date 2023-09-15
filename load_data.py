"""Module to load data from a csv file into a pandas DataFrame
"""
import pandas as pd


def load_csv_file() -> pd.DataFrame:
    """Load a csv file into a pandas DataFrame

    Returns: a pandas DataFrame containing the data from the csv file.
    """
    file_path = "data/eu_life_expectancy_raw.tsv"
    return pd.read_csv(file_path, sep="\t")
