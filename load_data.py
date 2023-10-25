"""Module to load data from a csv file into a pandas DataFrame
"""
from enum import Enum
from zipfile import ZipFile
from abc import ABC, abstractmethod
import pandas as pd
import json

class Country(Enum):
    AUSTRIA = "AT"
    BELGIUM = "BE"
    BULGARIA = "BG"
    SWITZERLAND = "CH"
    CYPRUS = "CY"
    CZECHIA = "CZ"
    DENMARK = "DK"
    ESTONIA = "EE"
    GREECE = "EL"
    SPAIN = "ES"
    EUROPEAN_UNION_27_20 = "EU27_2020"
    FINLAND = "FI"
    FRANCE = "FR"
    CROATIA = "HR"
    HUNGARY = "HU"
    ICELAND = "IS"
    ITALY = "IT"
    LIECHTENSTEIN = "LI"
    LITHUANIA = "LT"
    LUXEMBOURG = "LU"
    LATVIA = "LV"
    MALTA = "MT"
    NETHERLANDS = "NL"
    NORWAY = "NO"
    POLAND = "PL"
    PORTUGAL = "PT"
    ROMANIA = "RO"
    SWEDEN = "SE"
    SLOVENIA = "SI"
    SLOVAKIA = "SK"
    DEUTSCHLAND = "DE"
    EAST_WEST_DEUTSCHLAND = "DE_TOT"
    ALBANIA = "AL"
    EUROASIA_18 = "EA18"
    EUROASIA_19 = "EA19"
    EUROPEAN_FREE_TRADE_ASSOC = "EFTA"
    IRELAND = "IE"
    MONTENEGRO = "ME"
    REPUBLIC_OF_NORTH_MACEDONIA = "MK"
    SERBIA = "RS"
    ARMENIA = "AM"
    AZERBAIJAN = "AZ"
    GEORGIA = "GE"
    TURKEY = "TR"
    UKRAINE = "UA"
    BELARUS = "BY"
    EUROPEAN_ECONOMIC_AREA_30= "EEA30_2007"
    EUROPEAN_ECONOMIC_AREA_31 = "EEA31"
    EUROPEAN_UNION_27_07 = "EU27_2007"
    EUROPEAN_UNION_28 = "EU28"
    UNITED_KINGDOM = "UK"
    KOSOVO = "XK"
    FRANCE_METROPOLITAN = "FX"
    MOLDOVA = "MD"
    SAN_MARINO = "SM"
    RUSSIAN_FEDERATION = "RU"

    @classmethod
    def countries(cls):
        agg_countries = {
            "EU27_2020", 
            "DE_TOT",
            "EA18", 
            "EA19", 
            "EFTA", 
            "EEA30_2007", 
            "EEA31", 
            "EU27_2007", 
            "EU28",
            "FX"
        }
        return [country.value for country in cls if country.value not in agg_countries]

class DataLoaderStrategy(ABC):
    """Abstract class to load data from a file."""
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_data(self):
        """Abstract method to load data from a file."""
        pass 


class CSVDataLoader(DataLoaderStrategy):
    """Class to load data from a csv file."""

    def load_data(self):
        return pd.read_csv(self.file_path, sep="\t")


class ZipDataLoader(DataLoaderStrategy): 
    """Class to load data from a zip file."""
    def __init__(self, file_path, file_name):
        self.file_name = file_name
        super().__init__(file_path)

    def load_data(self):
        with ZipFile(self.file_path, "r") as zip_file:
            with zip_file.open(self.file_name, 'r') as json_file:
                return pd.read_json(json_file)
