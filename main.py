"""Script to load, clean and save life expectancy data
"""
import argparse
from pandas import DataFrame
from .data import load_data
from .cleaning import clean_data


def load_clean_save_data(region: str) -> None:
    """Main function to load and clean life expectancy data

    Args:
        region: region to filter
    """
    df_raw = load_data()
    df_clean = clean_data(region, df_raw)
    save_data(df_clean)


def save_data(df_clean: DataFrame)-> None:
    """Function to save life expectancy data to csv file

    Args:
        df: dataframe to save
    """
    return save_file_to_csv(df_clean)


def save_file_to_csv(df_melt: DataFrame)-> None:
    """ Save melted and clean dataframe to csv file

    Args:
        df_melt: dataframe to save
    """
    df_melt.to_csv(
        "data/pt_life_expectancy.csv", 
        sep=",",
        index=False
    )


if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description='Example argparse')
    parser.add_argument("--region", "--r", type=str, default="PT", help='Region name')
    args = parser.parse_args()
    main(args.region)