
import json
import pandas as pd
import locale
from locale import atof

def adb_json_to_df():  
    """
    This function converts the adb json file to a pandas dataframe.
    """ 

    f = open("final_project/adb_projects.json")
    
    data = json.load(f)
    new_data = list(filter(None, data))
    df = pd.DataFrame.from_dict(new_data, orient="columns")   
    
    locale.setlocale(locale.LC_NUMERIC, '')
    df["Amount"] = df["Amount"].map(atof)
    df["Amount"] = df["Amount"].where(df["Amount"] >= 1000, df["Amount"] * 1000000)

    df = df[df.loc[:, "commitment_date"] != "-"]
    df['commitment_date'] = pd.to_datetime(df["commitment_date"], format="%d %b %Y")

    return df

def hl_wb_to_df():
    """
    This function converts the wb high level file to a pandas dataframe. 
    """
    f = open("final_project/wb_hl_data.csv")

    df = pd.read_csv(f)
    return df