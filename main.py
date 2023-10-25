"""Script to load, clean and save life expectancy data
"""
import argparse
import pandas as pd
from .load_data import DataLoaderStrategy, Country
from .cleaning_csv import DataProcessorCsv
from .cleaning_zip import DataProcessorZip


class CleanDataPipeline:
    """Class to clean and save data from a csv or zip file
    and save it to a csv file.
    """

    def __init__(self, region: Country, file_type: DataLoaderStrategy):
        self.region = region.value
        self.file_type = file_type

    def load_clean_save_data(self) -> None:  # pragma: no cover
        """Main function to load and clean life expectancy data

        Args:
            region: region to filter
            file_type: data file type
        """
        if self.file_type == "csv":
            data_processor = DataProcessorCsv(
                file_path="data/eu_life_expectancy_raw.tsv"
            )

        if self.file_type == "zip":
            data_processor = DataProcessorZip(
                file_path="data/eurostat_life_expect.zip",
                file_name="eurostat_life_expect.json"
            )

        df_clean = data_processor.clean_data(self.region)

        self.save_file_to_csv(df_clean)

        return df_clean

    def check_if_region_is_valid(self) -> None:
        """Check if region is valid"""
        if self.region not in Country.countries():
            raise ValueError(
                f"Invalid region. Supported regions are: {', '.join(Country.countries())}"
            )

    def check_if_file_type_is_valid(self) -> None:
        """Check if file type is valid"""
        if self.file_type not in ["csv", "zip"]:
            raise ValueError(
                "Invalid data format. Supported formats are 'csv' and 'zip'."
            )

    def save_file_to_csv(self, df_melt: pd.DataFrame) -> None:
        """Save melted and clean dataframe to csv file

        Args:
            df_melt: dataframe to save
        """
        df_melt.to_csv(
            f"data/{str(self.region).lower()}_life_expectancy.csv", sep=",", index=False
        )


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Example argparse")
    parser.add_argument(
        "--region", "-r", type=Country, choices=Country, help="Region name"
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["csv", "zip"],
        default="csv",
        help="Data format (csv or zip)",
    )
    args = parser.parse_args()
    pipeline = CleanDataPipeline(args.region, args.format)
    pipeline.check_if_region_is_valid()
    pipeline.check_if_file_type_is_valid()

    pipeline.load_clean_save_data()
