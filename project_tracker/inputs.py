"""
Dictionary and List Inputs for the Dashboard

Author: Robert Surridge
"""

from project_tracker.load_and_clean.load_data import ll_df, hl_df

# Style Dictionaries

header_style = {"text-align": "center",
                "font-family": "Helvetica",
                "color": "#65463E"}

small_dropdown_style = {"display": "inline-block",
                        "text-align": "center",
                        "font-family": "Helvetica",
                        "color": "#65463E",
                        "width": "60%"}

big_dropdown_style = {"display": "inline-block",
                      "text-align": "center",
                      "font-family": "Helvetica",
                      "color": "#65463E",
                      "width": "85%"}

plot_style = {'width': "100%"}

map_dd_style = {"text-align": "center",
                "width": "75%",
                "padding": "2rem 1rem"}

hl_reg_style = {'display': 'inline-block'}

bar_filter = {"width": "40%", 
              "display": "inline-block", 
              "color": "#65463E", 
              "font-family": "Helvetica"}

hl_reg_layout_style = {"width": "100%", 
                       "display": "inline-block"}

hl_data_table_text = {"width": "100px", 
                      "minWidth": "100px", 
                      "maxWidth": "100px", 
                      "textOverflow": "ellipsis", 
                      "font-family": "Helvetica"}

ll_data_table_cell = {"text-align": "left", 
                      "width": 4,
                      "textOverflow": "ellipsis",
                      "font-family": "Helvetica"}

# Column Lists

compare_col = ['Country',
               '2020 GDP Per Capita', 
               '2020 Gain Index', 
               'Project Funding (in Millions)',
               'Climate Change Project Funding (in Millions)']

bottom_table_cols = [{"name": "Project Name", "id": "Project Name"},
                     {"name": "Status", "id": "Status"},
                     {"name": "Commitment Amount", "id": "Commitment Amount"},
                     {"name": "Effective Date", "id": "Effective Date"},
                     {"name": "Project URL", "id": "Project URL"},
                     {"name": "Search Terms", "id": "Tokens"}]

# Filter Options

paris_filter = [{"label": "Pre-Paris Agreement", 
                 "value": "(Pre-Paris Agreement)"}, 
                {"label": "Post-Paris Agreement", 
                 "value": "(Post-Paris Agreement)"}]

source_filter = [{"label": "Source: Asian Development Bank", "value": "ADB"}, 
                 {"label": "Source: World Bank", "value": "World Bank"}]

map_dd_options = ["Project Count", "Climate Change Project Count",
                  "Cumulative Project Funding", 
                  "Climate Change Project Funding"]

bar_options = ["Status", "Pre/Post Paris Agreement"]

country_options = [{"label": country, "value": country} for country in ll_df["Country"].unique()]

hl_data_table_options = [{"name": i, "id": i} for i in hl_df.loc[:, compare_col]]