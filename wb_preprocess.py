import pandas as pd
import pathlib
import re


def load_data(input_file):
    """
    Reads a CSV or Excel file, performs basic data cleaning,
    and returns the cleaned data as a pandas DataFrame.

    Args:
    - input_file (str): Path to the input file.

    Returns:
    - df (pandas.DataFrame): Cleaned pandas DataFrame.
    """
    # Determine the file type based on the file extension
    file_extension = input_file.split(".")[-1].lower()
    if file_extension == "csv":
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)
    elif file_extension in ["xls", "xlsx"]:
        # Load the Excel file into a pandas DataFrame
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file type: {}".format(file_extension))
    return df


def clean_wb_data():
    """
    """
    # # Load data from an Excel file
    # df = pd.read_excel("uncleaned consolidated post and pre data - wb_updated.xlsx")

    df = load_data("uncleaned consolidated post and pre data - wb_updated.xlsx")
    #Preprocessing data to remove unnecessary fields
    df = df.drop(['Borrower', 'Environmental Assessment Category', 'Sector '], axis=1)
    df = df[df['Commitment Amount'] != 0]
    df['Year'] = df['Effective Date'].dt.year
    df = df[df['Year'] != 2010]

    # Save the modified data to a CSV file
    df.to_csv('wb_data.csv', index=False)

    # Return the modified data as a DataFrame
    return df

def clean_ndgain_data():
    """
    """
    df = load_data('gain.csv')
    # Drop the "ISO3" column
    df = df.drop(columns=["ISO3","1995", "1996", "1997", "1998", "1999", "2000", 
    "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"], axis=1)
    df.to_csv("gain_cleaned.csv", index=False)
    # Print a message indicating that the function has completed
    print("Data cleaning complete")


def clean_gdpcapita_data():
    """
    Load a CSV file, perform data cleaning operations using pandas, and write the cleaned DataFrame to a new CSV file.

    input_path : str
        Path to the input CSV file.
    output_path : str
        Path to the output CSV file to be created.

    Returns:
        None
        The function writes the cleaned DataFrame to the output CSV file.
    """
    df = load_data('gdp_percapita.csv')
    df = df.loc[:, ['Country Name', 'Indicator Name', '2011', '2012', '2013', '2014', 
    '2015', '2016','2017', '2018', '2019', '2020', '2021']]
    df = df.dropna()
    df[['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', 
    '2021']] = df[['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']].round(0).astype(int)
    countries_to_keep = ['Afghanistan', 'Armenia', 'Bangladesh', 'Bhutan', 'Cambodia', 'Georgia', 'India', 'Indonesia', 'Kiribati', 'Kyrgyz Republic', "Lao People's Democratic Republic", 'Maldives', 'Mongolia', 'Nauru', 'Nepal', 'Pakistan', 'Papua New Guinea', "People's Republic of China", 'Philippines', 'Samoa', 'Solomon Islands', 'Sri Lanka', 'Tajikistan', 'Thailand', 'Tonga', 'Tuvalu', 'Uzbekistan', 'Viet Nam']
    df = df[df['Country Name'].isin(countries_to_keep)]
    df.to_csv("gdp_cleaned.csv", index=False)
    print("Data cleaning complete")


