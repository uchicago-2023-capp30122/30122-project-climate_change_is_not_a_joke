import os
import pandas as pd
import plotly.express as px


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
    This function loads the uncleaned data file, 
    preprocesses it by removing unnecessary fields, saves the modified data to a CSV file, 
    and returns the modified data as a DataFrame.

    Returns:
    pandas.DataFrame
    """
    data_path = os.path.join('data', 'raw/uncleaned consolidated post and pre data - wb_updated.xlsx')
    df = load_data(data_path)

    #Preprocessing data to remove unnecessary fields
    df = df.drop(['Borrower', 'Environmental Assessment Category', 'Sector '], axis=1)
    df = df[df['Commitment Amount'] != 0]
    df['Year'] = df['Effective Date'].dt.year
    df = df[df['Year'] != 2010]

    # Save the modified data to a CSV file
    df.to_csv(os.path.join('data', 'wb_data.csv'), index=False)

    # Return the modified data as a DataFrame
    return df

def clean_ndgain_data():
    """
    This function loads the uncleaned data file, 
    preprocesses it by removing unnecessary fields 
    and saves the modified data to a CSV file,

    Returns:
        None. The function writes the cleaned DataFrame to the output CSV file.
    """
    data_path = os.path.join('data', 'gain.csv')
    df = load_data(data_path)
    # List of countries to keep
    countries_to_keep = ["Afghanistan", "Armenia", "Bangladesh", "Bhutan", "Cambodia", "Georgia", 
                         "India", "Indonesia", "Kiribati", "Kyrgyzstan", "Lao People's Democratic Republic", 
                         "Maldives", "Mongolia", "Nepal", "Pakistan", "Papua New Guinea", "China", 
                         "Philippines", "Samoa", "Solomon Islands", "Sri Lanka", "Tajikistan", "Thailand", "Tonga", 
                         "Tuvalu", "Uzbekistan", "Viet Nam"]
    # Drop all rows except for those in the list of countries to keep
    df = df[df["Name"].isin(countries_to_keep)]
    # Drop all columns except for "Name" and "2020"
    df = df[["Name", "2020"]]
    # Rename the columns
    df = df.rename(columns={"Name": "Country Name", "2020": "2020 Gain Index"})
    df.to_csv(os.path.join('data', 'gain_cleaned.csv'), index=False)
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
    data_path = os.path.join('data', 'gdp_percapita.csv')
    df = load_data(data_path)
    df = df.loc[:, ['Country Name', '2020']]
    df = df.dropna()
    countries_to_keep = ["Afghanistan", "Armenia", "Bangladesh", "Bhutan", "Cambodia", "Georgia", 
                         "India", "Indonesia", "Kiribati", "Kyrgyz Republic", "Lao PDR", 
                         "Maldives", "Mongolia", "Nepal", "Pakistan", "Papua New Guinea", "China", 
                         "Philippines", "Samoa", "Solomon Islands", "Sri Lanka", "Tajikistan", "Thailand", "Tonga", 
                         "Tuvalu", "Uzbekistan", "Vietnam"]
    df = df[df['Country Name'].isin(countries_to_keep)]
    df = df.rename(columns={"2020": "2020 GDP Per Capita"})
    df.to_csv(os.path.join('data', 'gdp_cleaned.csv'), index=False)
    print("Data cleaning complete")


def calc_avg_commitment_amount_by_year(df):
    """
    Calculate average commitment amount by year.

    Parameters:
    df : pandas.DataFrame
        Input dataframe containing columns 'Year' and 'Commitment Amount'

    Returns:
    pandas.DataFrame - A dataframe containing two columns: 'Year' and 'Average Commitment Amount'


    """
    # create a new dataframe to store the results
    result_df = pd.DataFrame(columns=['Year', 'Average Commitment Amount'])
    
    # loop through each unique year in the 'Year' column of the input dataframe
    for year in df['Year'].unique():
        # filter the dataframe by the current year
        year_df = df[df['Year'] == year]
        
        # calculate the average commitment amount for the current year
        avg_commitment_amount = year_df['Commitment Amount'].mean() / 1000000
        
        # add the year and average commitment amount to the result dataframe
        result_df = result_df.append({'Year': year, 'Average Commitment Amount': avg_commitment_amount}, ignore_index=True)
    
    # return the result dataframe
    return result_df


def avg_commitment_plot():
    """
    Generate a bar plot showing the average commitment amount by year.

    Parameters:
    None

    Returns:
    None. Creates a bar plot
    """
    df = pd.read_csv("project_tracker/data/ll_wb.csv")
    avg_commitment_amount_by_year = calc_avg_commitment_amount_by_year(df)
    # Create a bar plot of the average commitment amount by year using plotly
    fig = px.bar(avg_commitment_amount_by_year, x='Year', y='Average Commitment Amount',
                labels={'Year': 'Year', 'Average Commitment Amount': 'Average Commitment Amount (Millions of Dollars)'})
