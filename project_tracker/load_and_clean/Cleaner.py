#Functions by by Kayecee Palisoc: clean_data
#Functions by Robert McCormick:  merg_climate_df, climate_tag_token_lst,
#add_climate_tag, make_token_column, final_adb_csv

import pandas as pd
import json
from collections import Counter
import spacy

def clean_data():
    """
    This functions cleans the scraped data from the adb projects jason to the 
    desired format 
    """
    with open('project_tracker/data/raw/adb_projects.json') as f:
        data = json.load(f)

    #remove null rows
    data = list(filter(lambda x: x is not None, data))

    #remove unnecessary fields
    field_list = ['Project Name', 'Project Number', 'Country / Economy', 'Project Status', 'Sector / Subsector', 'Description', 'commitment_date', 'Amount', 'project_url']
    cleaned_list = []
 
    for row in data:
        cleaned_project = {}
        for key in row.keys():
            if key in field_list:
                cleaned_project[key] = row[key]
        cleaned_list.append(cleaned_project)

    #convert to pandas df
    df = pd.DataFrame(cleaned_list)

    #convert amount to float
    df['Amount'] = df['Amount'].str.replace(',', '').astype(float)

    #remove zero Amount
    df.drop(df[df['Amount'] ==0].index, inplace = True)

    #convert amount to millions
    df["Commitment Amount"] = df["Amount"].where(df["Amount"] >= 30000, df["Amount"] * 1000000)

    #remove those with no effectivity date
    df.drop(df[df['commitment_date'] =='-'].index, inplace = True)

    #clean status column
    df['Project Status'] = df['Project Status'].replace('Approved', 'Active')
    
    #clean sector column
    df['Sector'] = (df['Sector / Subsector'].str.split('/').str[0]).str.strip()
    df = df.dropna(subset=['Sector'])

    #change country of multiple country projects to 'Regional'
    df['Country'] = df['Country / Economy'].copy()
    df.loc[df['Country'].str.contains('Regional'), 'Country'] = 'Regional'

    #cleaning country names based on official country_list
    df.loc[df['Country'].str.contains('China'), 'Country'] = "People's Republic of China"
    df.loc[df['Country'].str.contains('Micronesia'), 'Country'] = "Federated States of Micronesia"

    #Add column for Region
    country_list = pd.read_csv('Country_List.csv')
    df = df.merge(country_list[['Country', 'Region']], on='Country', how='left')
    df.loc[df['Country'] == 'Regional', 'Region'] = 'Regional'

    #dropping rows with no corresponding Region --this means the are not in the official Country_List
    df = df.dropna(subset=['Region'])

    #adding pre/post Paris Agreement tag
    target_date = pd.to_datetime('2016-11-04')
    df['Pre/Post Paris Agreement'] = df['commitment_date'].apply(lambda x: 0 if pd.to_datetime(x) < target_date else 1)

    #aligning column names
    df = df.rename(columns={'commitment_date': 'Effective Date', 'project_url': 'Project URL','Project Status' : 'Status', 'Description' : 'Project Description' })
    
    #dropping unnecessary columns
    df = df.drop(columns=["Country / Economy", "Project Number", "Sector / Subsector", "Amount"])

    # adding year column
    df['Year'] = pd.DatetimeIndex(df['Effective Date']).year

    #rearranging columns
    df = df[['Country', 'Region', 'Project Name', 'Project Description', 'Status', 'Project URL', 'Effective Date', 'Commitment Amount', 'Pre/Post Paris Agreement','Year', 'Sector']]

    #convert to csv    
    df.to_csv("project_tracker/data/clean_df.csv", index=False)
    return df


def merg_climate_df():
    """
    mergs known climate data from ADB from csv to pandas data frame

    Returns: Pandas data frame 
    """


    df_2019 = pd.read_csv('project_tracker/data/raw/adb_19-21_climate_data/ADB Climate-2019.csv')
    df_2020 = pd.read_csv('project_tracker/data/raw/adb_19-21_climate_data/ADB Climate-2020.csv')
    df_2021 = pd.read_csv('project_tracker/data/raw/adb_19-21_climate_data/ADB Climate-2021.csv')

    df_2020.dropna(how='all', axis=1, inplace=True)
    new_df_2020 = df_2020.drop(['Other Sector(s) Covered'], axis = 1)
    
    frames = [df_2019, new_df_2020, df_2021]
    climate_df = pd.concat(frames)
    climate_df = climate_df.drop_duplicates(subset='Project Number', keep="first")
    return climate_df



def climate_tag_token_lst(df,top_tokens):
    """
    creates a list of tokens from the known ADB Climate projects 
    Input:
        df(pandas data frame)
        top_tokens(int): desired number of most frequently occuring tokens
    Returns: CSV
    """
    df = merg_climate_df()
    sp = spacy.load("en_core_web_sm")
    token_lst = []
    for _, row in df.iterrows():
        doc = sp(row['Project Name'])

        for token in doc:
            if token.is_stop or token.is_punct or token.like_num:
                continue
            token_lst.append(token.text)

    word_freq = Counter(token_lst)
    top_tokens = word_freq.most_common(top_tokens)
    df = pd.DataFrame(top_tokens) 
    with open('tokens', 'w') as f:
        df.to_csv('tokens.csv')
    
def add_climate_tag(df):

    """
    Creates new column and determines if project is climate realted based off
    of list of Tag words 

    Input:
        df(pandas data frame): data frame

    Return:
        data frame 
    """

    sp = spacy.load("en_core_web_sm")
    tag = pd.read_csv('project_tracker/data/raw/adb_19-21_climate_data/climate_tag_words.csv')
    
    for index, row in df.iterrows():

        doc = sp(row['Project Name'])
        words = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.like_num]
        for word in words:
            if word == '2)-' or word == '1)-':
                continue
            if tag["Tag"].str.contains(word).any():
                df.loc[index,['Climate-Related']] = 'Yes'
                break
            else:
                df.loc[index,['Climate-Related']] = 'No'   
    return df 

def make_token_column(df, name):
    """
    Making tokens from description and making new column to dataframe. Can be
    used for ADB or World bank

    Input:
        df(pandas data frame): data frame
        name(str): str of what user wants to name  CSV 
    Return:
        CSV file 
    """

    sp = spacy.load("en_core_web_sm")
    for index, row in df.iterrows():
            doc = sp(str(row["Project Description"]))
           
            words =[word.lemma_.lower() for word in doc if not word.is_stop and not word.is_punct and not word.like_num]
            
            df.at[index,'Tokens'] = str(words)
            print(words)
    df.to_csv(name, index=False)
    

def final_adb_csv():
    """
    This function takes in the clean data, categorizes the projects as climate 
    related, and then addes a column of tokens based off the project description

    Input:
        name(str): name and path of csv
    Returns(csv) 
    """
    df = clean_data()
    df = add_climate_tag(df)
    return make_token_column(df, 'project_tracker/data/final_adb')


if __name__ == '__main__':
    final_adb_csv()










                

