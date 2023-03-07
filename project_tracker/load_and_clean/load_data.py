"""
Load cleaned data in Pandas dataframes

Author: Robert Surridge
"""

import pandas as pd

# Construct Low Level DataFrames

adb_df = pd.read_csv("project_tracker/data/final_adb.csv")
wb_df = pd.read_csv("project_tracker/data/ll_wb.csv")
adb_df = adb_df[adb_df["Climate-Related"] == "Yes"]

df_lst = [adb_df, wb_df]
ll_df = pd.concat(df_lst)
ll_df = ll_df.sort_values(by = ['Country'])

ll_df["Effective Date"] = pd.to_datetime(ll_df['Effective Date'])
ll_df["Pre/Post Paris Agreement"] = ll_df["Pre/Post Paris Agreement"].map({0: "Pre", 1: "Post"})

#Construct High Level DataFrame

hl_df = pd.read_csv("project_tracker/data/hl_data.csv")
hl_df['Project Funding (in Millions)'] = hl_df["Cumulative Project Funding (Total)"].div(1000000).round(2)
hl_df['Climate Change Project Funding (in Millions)'] = hl_df["Climate Change Project Funding (Total)"].div(1000000).round(2)