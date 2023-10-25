"""Tests for the cleaning module"""
from unittest.mock import patch, MagicMock
import pandas as pd

from ..cleaning_csv import DataProcessorCsv
from ..main import CleanDataPipeline
from ..load_data import CSVDataLoader, Country


def test_clean_data(pt_life_expectancy_expected: pd.DataFrame) -> None:
    """Run the `clean_data` function and compare the output to the expected output

    Args:
        pt_life_expectancy_expected: expected output of the `clean_data` function
    """
    
    region = Country("PT")
    data_processor = DataProcessorCsv("data/eu_life_expectancy_raw.tsv")
    pt_life_expectancy_actual = data_processor.clean_data(region)
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


@patch("pandas.DataFrame.to_csv")
# @patch("CleanDataPipeline.save_file_to_csv")
def test_save_file_to_csv(mock_to_csv: MagicMock, pt_life_expectancy_expected) -> None:
    """Test that the `save_file_to_csv` function saves the file as expected

    Args:
        mock_to_csv: mock object for pandas.DataFrame.to_csv
    """
    def _print_success_message(*args, **kwargs):
        print('File successfully saved')
    
    mock_region = Country("BE")
    mock_df = pt_life_expectancy_expected

    mock_to_csv.side_effect= _print_success_message
    mock_Class = CleanDataPipeline(mock_region, "csv")
    mock_Class.save_file_to_csv(mock_df)

    expected_file_name = f"data/{str(mock_region.value).lower()}_life_expectancy.csv"
    print(expected_file_name)
    mock_to_csv.assert_called_once_with(expected_file_name, sep=",", index=False)


@patch("pandas.read_csv")
def test_load_csv(mock_read_csv, pt_life_expectancy_expected):
    """Test that the `load_csv_file` function loads the file as expected

    Args:
        mock_read_csv: mock object for pandas.read_csv
        pt_life_expectancy_expected: expected output of the `load_csv_file` function

    """
    mock_df = pt_life_expectancy_expected
    mock_read_csv.return_value = mock_df
    loader_type = CSVDataLoader("data/eu_life_expectancy_raw.tsv")
    result = loader_type.load_data()

    mock_read_csv.assert_called_once_with("data/eu_life_expectancy_raw.tsv", sep="\t")

    assert result.equals(mock_df)

# TODO: fix this test
# @patch('zipfile.ZipFile') 
# @patch('pandas.read_json')
# def test_load_zip_file(mock_zip_file, mock_read_json):
#     """Test that the `ZipDataLoader` function loads the file as expected"""

#     file_path = "data/eurostat_life_expect.zip"
#     file_name = "eurostat_life_expect.json"
#     mock_context = MagicMock()
#     mock_zip_file.return_value = mock_context
    
#     # Mock the context manager functionality of zip_file.open
#     mock_file_in_zip = MagicMock()
#     mock_context.open.return_value = mock_file_in_zip
#     mock_file_in_zip.closed = False

#     zip_loader = ZipDataLoader(file_path, file_name)
    
#     # When
#     zip_loader.load_data()
    
#     # Then
#     mock_zip_file.assert_called_once_with(file_path, 'r')

#     mock_zip_file.__enter__.assert_called_once()
#     mock_zip_file.__enter__.return_value.open.assert_called_once_with(file_name, 'r')
#     mock_read_json.assert_called_once_with(mock_json_file)
#     assert zip_loader.load_data() == mock_file_in_zip


def test_true_countries():
    actual_countries = Country.countries()
    expected_actual_countries = [
        Country.AUSTRIA.value,
        Country.BELGIUM.value,
        Country.BULGARIA.value,
        Country.SWITZERLAND.value,
        Country.CYPRUS.value,
        Country.CZECHIA.value,
        Country.DENMARK.value,
        Country.ESTONIA.value,
        Country.GREECE.value,
        Country.SPAIN.value,
        Country.FINLAND.value,
        Country.FRANCE.value,
        Country.CROATIA.value,
        Country.HUNGARY.value,
        Country.ICELAND.value,
        Country.ITALY.value,
        Country.LIECHTENSTEIN.value,
        Country.LITHUANIA.value,
        Country.LUXEMBOURG.value,
        Country.LATVIA.value,
        Country.MALTA.value,
        Country.NETHERLANDS.value,
        Country.NORWAY.value,
        Country.POLAND.value,
        Country.PORTUGAL.value,
        Country.ROMANIA.value,
        Country.SWEDEN.value,
        Country.SLOVENIA.value,
        Country.SLOVAKIA.value,
        Country.DEUTSCHLAND.value,
        Country.ALBANIA.value,
        Country.IRELAND.value,
        Country.MONTENEGRO.value,
        Country.REPUBLIC_OF_NORTH_MACEDONIA.value,
        Country.SERBIA.value,
        Country.ARMENIA.value,
        Country.AZERBAIJAN.value,
        Country.GEORGIA.value,
        Country.TURKEY.value,
        Country.UKRAINE.value,
        Country.BELARUS.value,
        Country.UNITED_KINGDOM.value,
        Country.KOSOVO.value,
        Country.MOLDOVA.value,
        Country.SAN_MARINO.value,
        Country.RUSSIAN_FEDERATION.value
    ]
    assert actual_countries == expected_actual_countries
