"""Script to load, clean and save life expectancy data
"""
import argparse
import pandas as pd
from .cleaning import clean_data


def load_clean_save_data(region: str) -> None:
    """Main function to load and clean life expectancy data

    Args:
        region: region to filter
    """
    df_clean = clean_data(region)
    save_file_to_csv(df_clean, region)


def save_file_to_csv(df_melt: pd.DataFrame, region: str)-> None:
    """ Save melted and clean dataframe to csv file

    Args:
        df_melt: dataframe to save
        region: data region
    """
    df_melt.to_csv(
        f"data/{region.str.lower()}_life_expectancy.csv", 
        sep=",",
        index=False
    )


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='Example argparse')
    parser.add_argument("--region", "--r", type=str, default="PT", help='Region name')
    args = parser.parse_args()
    load_clean_save_data(args.region)