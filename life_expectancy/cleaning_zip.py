"""Module to clean data of a pandas DataFrame
"""
import pandas as pd
from life_expectancy.load_data import Country, ZipDataLoader


class DataProcessorZip:
    """Class to clean data of a pandas DataFrame"""

    def __init__(self, file_path: str, file_name: str):
        self.file_path = file_path
        self.file_name = file_name

    def clean_data(self, region: Country) -> pd.DataFrame:
        """Function to clean life expectancy file, unpivot date column data
        in the input region

        Args:
            region: region to filter

        Returns:
            df_melt: melted dataframe
        """
        df_split = self.get_data()
        df_split = df_split.dropna()
        df_split = df_split[df_split["region"] == region].reset_index(drop=True)
        df_split["year"] = df_split["year"].astype("int")

        return df_split

    def get_data(self) -> pd.DataFrame:
        """Function to load life expectancy data in zip format"""
        zip_processor = ZipDataLoader(self.file_path, self.file_name)
        df_raw = zip_processor.load_data()
        return self._preprocess_data(df_raw)

    def _preprocess_data(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses raw data in a pandas DataFrame
        by selecting a subset of columns and renaming some column names.

        Args:
            df_raw: The input pandas DataFrame containing the raw data.

        Returns:
            df_split: A preprocessed pandas DataFrame with specific columns and clear column names.
        """
        df_raw = df_raw[["unit", "sex", "age", "country", "year", "life_expectancy"]]
        df_raw = df_raw.rename(
            columns={"country": "region", "life_expectancy": "value"}
        )
        return df_raw
