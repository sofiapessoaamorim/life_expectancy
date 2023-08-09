"""Script to load and clean life expectancy data
"""
import argparse
import pandas as pd
from pandas import DataFrame
import numpy as np


def clean_data(region: str)-> DataFrame:
    """Function to clean and save life expectancy file, unpivot date column data 
    in the PT region"""
    df_raw = load_csv_file()
    df_split = preprocess_data(df_raw)

    value_cols = df_split.columns[:62]
    id_cols = df_split.columns[62:]

    df_clean = identify_nans_convert_floats(df_split, value_cols)
    df_melt = melt_dataframe(df_clean, id_cols, value_cols)
    df_melt = df_melt.dropna()
    df_melt = df_melt[df_melt["region"]==region].reset_index(drop=True)
    df_melt["year"] = df_melt["year"].astype("int")

    save_file_to_csv(df_melt)


def save_file_to_csv(df_melt: DataFrame):
    """ Save melted and clean dataframe to csv file
    """
    df_melt.to_csv(
        "data/pt_life_expectancy.csv", 
        sep=",",
        index=False
    )


def melt_dataframe(df_clean: DataFrame, id_cols: list, value_cols: list)-> DataFrame:
    """Melt dataframe to turn all year columns into a single year column
    
    Args:
        df_clean: dataframe preprocessed
        id_cols: list of columns to maintain
        value_cols: list of all year column
    
    Returns:
        df_melt: Melted dataframe 
    """
    df_melt = pd.melt(
        df_clean,
        id_vars=id_cols,
        value_vars=value_cols,
        var_name="year"
    )
    return df_melt


def identify_nans_convert_floats(df_split: DataFrame, value_cols: list)-> DataFrame:
    """Identifies NaN-like values in specified columns of a DataFrame and converts them to floats.

    Args:
        df_split: preprocessed dataframe.
        value_cols: list of columns with numerical data.
    
    Returns:
        df_split: A modified DataFrame with identified NaN-like values replaced and float 
        conversions applied.
    """
    for col in value_cols:
        df_split[col] = df_split[col].str.strip()
        df_split[col] = (
            df_split[col]
                .replace(":", np.nan, regex=True)
                .apply(convert_value_to_float)
        )
    return df_split


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


def load_csv_file()-> DataFrame:
    """Load a csv file into a DataFrame

    Returns: a DataFrame containing the data from the csv file.
    """
    file_path = "data/eu_life_expectancy_raw.tsv"
    return pd.read_csv(file_path, sep="\t")


def convert_value_to_float(value: str)-> float:
    """Convert values to float type
    
    Args:
        value : column values

    Returns: extract first value and convert it into float.   
    """
    try:
        return float(value)
    except ValueError:
        parts = value.split(" ")
        return float(parts[0])


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='Example argparse')
    parser.add_argument("--region", "--r", type=str, default="PT", help='Region name')
    args = parser.parse_args()
    clean_data(args.region)
