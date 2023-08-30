"""Module to clean data in a DataFrame
"""
import pandas as pd
from pandas import DataFrame
import numpy as np


def clean_data(region:str, data: DataFrame)-> DataFrame:
    """Function to clean life expectancy file, unpivot date column data 
    in the input region
    
    Args:
        region: region to filter
        data: dataframe to clean
    
    Returns:
        df_melt: melted dataframe
    """

    value_cols = data.columns[:62]
    id_cols = data.columns[62:]

    df_clean = identify_nans_convert_floats(data, value_cols)
    df_melt = melt_dataframe(df_clean, id_cols, value_cols)
    df_melt = df_melt.dropna()
    df_melt = df_melt[df_melt["region"]==region].reset_index(drop=True)
    df_melt["year"] = df_melt["year"].astype("int")

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
