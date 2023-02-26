
import json
import pandas as pd
import locale
from locale import atof

#  if "Project Status" in i.keys():
#      df["Project Status"] = i["Project Status"]
#  if "Project Type / Modality of Assistance" in i.keys():
#       df["Project Type / Modality of Assistance"] = i["Project Type / Modality of Assistance"]
#   if "Description" in i.keys():
#       df["Description"] = i["Description"]

df = pd.DataFrame(columns=["Project Name", "Project Number", "Country / Economy",
                           "Project Status", "Project Type / Modality of Assistance",
                           "Strategic Agendas", "Sector / Subsector", "Description",
                           "commitment_date", "Amount", "project_url"])

f = open("final_project/adb_projects.json")
    
data = json.load(f)
for i in data:
    if i is None:
        continue
    df1 = pd.DataFrame({"Project Name": i["Project Name"],
                        "Country / Economy": i["Country / Economy"],
                        "Strategic Agendas" : i["Strategic Agendas"],
                        "Sector / Subsector": i["Sector / Subsector"],
                        "commitment_date": i["commitment_date"],
                        "Amount": i["Amount"],
                        "project_url": i["project_url"]},
                        index = [i["Project Number"]])
    df = df.append(df1)
    
locale.setlocale(locale.LC_NUMERIC, '')
df["Amount"] = df["Amount"].map(atof)
df["Amount"] = df["Amount"].where(df["Amount"] >= 1000, df["Amount"] * 1000000)

df = df[df.loc[:, "commitment_date"] != "-"]
df['commitment_date'] = pd.to_datetime(df["commitment_date"], format="%d %b %Y")