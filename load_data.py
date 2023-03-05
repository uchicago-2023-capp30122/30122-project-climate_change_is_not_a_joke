"""
Load cleaned data in Pandas dataframes
"""

import pandas as pd

# Construct Low Level DataFrames
ll_adb = open("final_project/ll_adb.csv")
ll_wb = open("final_project/ll_wb.csv")
adb_df = pd.read_csv(ll_adb)
wb_df = pd.read_csv(ll_wb)

ll_wb_2 = open("final_project/ll_wb.csv")
wb_df_2 = pd.read_csv(ll_wb_2)

adb_df = adb_df.loc[:, ['Country', 'Region', 'Project Name', 'Project Description', 
                        'Status', 'Project URL', 'Effective Date', 'Commitment Amount',
                        'Pre/Post Paris Agreement']]

wb_df = wb_df.loc[:, ['Country', 'Region', 'Project Name', 'Project Description', 
                      'Status', 'Project URL', 'Effective Date', 'Commitment Amount',
                      'Pre/Post Paris Agreement']]
compare_col = ['Country','2020 GDP Per Capita', '2020 Gain Index']

df_lst = [adb_df, wb_df]
ll_df = pd.concat(df_lst)
ll_df = ll_df.sort_values(by = ['Country'])

ll_df["Effective Date"] = pd.to_datetime(ll_df['Effective Date'])
ll_df["Pre/Post Paris Agreement"] = ll_df["Pre/Post Paris Agreement"].map({0: "Pre", 
                                                                     1: "Post"})

#Construct High Level DataFrame
hl_f = open("final_project/hl_data.csv")
hl_df = pd.read_csv(hl_f)