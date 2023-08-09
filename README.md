# Life Expectancy Data Cleaning
[![CI/CD Workflow](https://github.com/sofiapessoaamorim/life_expectancy/actions/workflows/run-tests.yaml/badge.svg?branch=ci)](https://github.com/sofiapessoaamorim/life_expectancy/actions/workflows/run-tests.yaml)

This project is designed to load and clean life expectancy data from a provided CSV file. The main purpose of the script is to process the data, convert it into a more usable format, and save the cleaned data as a CSV file. 
The structure of this project is as it follows:
```bash
assignments
├── life_expectancy    
| ├── data             
| └── tests            
|                      
├── pyproject.toml     
|                      
└── README.md          
```
The cleaning.py script focuses on the data for a specific region.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Functionality](#functionality)
- [Requirements](#requirements)
- [Installation](#installation)

## Introduction

Life expectancy data often comes in messy formats, and it's important to preprocess and clean the data before performing any analysis. This script provides a solution for loading, cleaning, and saving life expectancy data for a specific region. It handles tasks like handling missing values, converting data types, and reshaping the data for easier analysis.

## Usage

To use the script, follow these steps:

1. Make sure you have the necessary requirements installed (see [Requirements](#requirements)).
2. Download the raw life expectancy data file (`eu_life_expectancy_raw.tsv`) and place it in the `data` directory.
3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Run the script using the following command, replacing `REGION_NAME` with the desired region's name (e.g., "PT" for Portugal):

```bash
python script.py --region REGION_NAME
```

## The cleaned and processed data will be saved as `pt_life_expectancy.csv` in the `data` directory.

## Functionality

The script performs the following tasks:

1. **Loading Data**: The script loads the raw life expectancy data from a provided CSV file (`eu_life_expectancy_raw.tsv`).

2. **Data Cleaning**: It preprocesses the data by splitting a combined column and cleaning column names.

3. **NaN Handling and Conversion**: The script identifies NaN-like values in specified columns and converts them to floats. It also removes any rows with missing data.

4. **Data Reshaping**: The script melts the DataFrame to turn all year columns into a single year column for easier analysis.

5. **Region Selection**: It filters the data to retain only the rows corresponding to the specified region.

6. **Saving Data**: The cleaned and reshaped data is saved as `pt_life_expectancy.csv` in the `data` directory.

## Requirements

- Python 3.x
- pandas
- numpy

## Installation

1. Clone or download this repository.

```bash
git clone https://github.com/sofiapessoaamorim/life_expectancy.git
```