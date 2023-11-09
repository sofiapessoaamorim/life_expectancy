"""Module to clean data of a pandas DataFrame
"""
import pandas as pd
import numpy as np
from life_expectancy.load_data import Country, CSVDataLoader


class DataProcessorCsv:
    """Class to clean data of a pandas DataFrame"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def clean_data(self, region: Country) -> pd.DataFrame:
        """Function to clean life expectancy file, unpivot date column data
        in the input region

        Args:
            region: region to filter

        Returns:
            df_melt: melted dataframe
        """
        data = self.get_data()
        value_cols = data.columns[:62]
        id_cols = data.columns[62:]

        df_clean = self._identify_nans_convert_floats(data, value_cols)
        df_melt = self._melt_dataframe(df_clean, id_cols, value_cols)

        df_melt = df_melt.dropna()
        df_melt = df_melt[df_melt["region"] == region].reset_index(drop=True)
        df_melt["year"] = df_melt["year"].astype("int")

        return df_melt

    def get_data(self) -> pd.DataFrame:
        """Function to load life expectancy data

        Returns:
            df_split: dataframe with split columns
        """
        csv_processor = CSVDataLoader(self.file_path)
        df_raw = csv_processor.load_data()
        return self._preprocess_data(df_raw)

    def _preprocess_data(self, df_raw: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses raw data in a pandas DataFrame
        by splitting a column and cleaning column names.

        Args:
            df_raw: The input pandas DataFrame containing the raw data.

        Returns:
            df_split: A preprocessed pandas DataFrame with split columns and cleaned column names.
        """
        df_raw[["unit", "sex", "age", "region"]] = df_raw[
            "unit,sex,age,geo\\time"
        ].str.split(",", expand=True)
        df_split = df_raw.drop(columns=["unit,sex,age,geo\\time"], inplace=False)
        df_split.columns = df_split.columns.str.strip()
        return df_split

    def _identify_nans_convert_floats(
        self, df_split: pd.DataFrame, value_cols: list
    ) -> pd.DataFrame:
        """Identifies NaN-like values in specified columns of a pandas DataFrame
        and converts them to floats.

        Args:
            df_split: preprocessed dataframe.
            value_cols: list of columns with numerical data.

        Returns:
            df_split: A modified pandas DataFrame with identified NaN-like values replaced and float
            conversions applied.
        """
        for col in value_cols:
            df_split[col] = df_split[col].str.strip()
            df_split[col] = (
                df_split[col]
                .replace(":", np.nan, regex=True)
                .apply(self._convert_value_to_float)
            )
        return df_split

    def _convert_value_to_float(self, value: str) -> float:
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

    def _melt_dataframe(
        self, df_clean: pd.DataFrame, id_cols: list, value_cols: list
    ) -> pd.DataFrame:
        """Melt dataframe to turn all year columns into a single year column

        Args:
            df_clean: dataframe preprocessed
            id_cols: list of columns to maintain
            value_cols: list of all year column

        Returns:
            df_melt: Melted dataframe
        """
        df_melt = pd.melt(
            df_clean, id_vars=id_cols, value_vars=value_cols, var_name="year"
        )
        return df_melt
