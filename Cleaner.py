import pandas as pd
import json

def clean_data():
    with open('adb_projects.json') as f:
        data = json.load(f)

    #remove null rows
    data = list(filter(lambda x: x is not None, data))

    #remove unnecessary fields
    field_list = ['Project Name', 'Project Number', 'Country / Economy', 'Project Status', 'Strategic Agendas', 'Sector / Subsector', 'Description', 'commitment_date', 'Amount', 'project_url']
    cleaned_list = []
    #country_proj ={}
    #proj_id = {}
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

    #remove those with no effectivity date
    df.drop(df[df['commitment_date'] =='-'].index, inplace = True)

    #convert to csv    
    df.to_csv("clean_df.csv", index=False)



                

