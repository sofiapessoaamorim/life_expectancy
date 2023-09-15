"""Tests for the cleaning module"""
import pandas as pd
import unittest
from unittest.mock import patch, MagicMock

from ..cleaning import clean_data
from ..main import save_file_to_csv
from ..load_data import load_csv_file

def test_clean_data(pt_life_expectancy_expected: pd.DataFrame)-> None:
    """Run the `clean_data` function and compare the output to the expected output
    
    Args:
        pt_life_expectancy_expected: expected output of the `clean_data` function
    """
    pt_life_expectancy_actual = clean_data(region="PT")
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )


@patch('pandas.DataFrame.to_csv')
def test_save_file_to_csv(mock_to_csv: MagicMock, pt_life_expectancy_expected)-> None:
    """Test that the `save_file_to_csv` function saves the file as expected

    Args:
        mock_to_csv: mock object for pandas.DataFrame.to_csv
    """
    mock_region = 'TestRegion'
    mock_df = pt_life_expectancy_expected

    save_file_to_csv(mock_df, mock_region)

    expected_file_name = f"data/{mock_region.lower()}_life_expectancy.csv"
    mock_to_csv.assert_called_once_with(
        expected_file_name, sep=",", index=False
    )

@patch('pandas.read_csv')
def test_load_csv(mock_read_csv, pt_life_expectancy_expected):
    mock_df = pt_life_expectancy_expected
    mock_read_csv.return_value = mock_df

    result = load_csv_file()

    mock_read_csv.assert_called_once_with("data/eu_life_expectancy_raw.tsv", sep="\t")

    assert result.equals(mock_df)