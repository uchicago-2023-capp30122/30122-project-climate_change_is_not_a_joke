'''
Dashboard Constructor

Climate Change Investment Tracker
'''

import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

#from final_project.plots.map import project_map 
from final_project.dashboard import app
from final_project.clean_data import hl_wb_to_df as hl

# Construct Dataframes
f = open("final_project/clean_data.csv")
df = pd.read_csv(f)
df_hl = hl()

country_options = [{"label": country, "value": country} for country in df["Country / Economy"].unique()]

# Build Figures

map_fig = px.choropleth(df_hl,
                        locations = "Country", 
                        locationmode="country names",
                        color="Climate Change Project Total Proportion",
                        color_continuous_scale=px.colors.diverging.BrBG,
                        color_continuous_midpoint=0.2,
                        range_color = [0, 0.5],
                        scope = 'asia')
                            


scatter_fig = px.scatter(df, 
                         x = "commitment_date", 
                         y = "Amount",
                         hover_name = "Project Name",
                         hover_data = ["Country / Economy", "project_url"],
                         title = "Commitment Amount Over Time in",
                         labels = {"Amount": "Commitment Amount"},
                         trendline = "ols")

bar_fig = px.bar(df, 
                 x = "Project Status", 
                 y = "Amount",
                 color = "Project Type / Modality of Assistance",
                 title = "Commitment Amount per Project Type in",
                 labels = {"Amount": "Commitment Amount"})

# App Layout

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker"), 
                    justify = 'center'),
    
    html.Br(),
    dbc.Row(dcc.Dropdown(id="country_dd",
                         options=country_options,
                          multi = False),
                          justify="center"),
    html.Br(),
    dbc.Row(dcc.Graph(id = 'map',
                      figure = map_fig,
                      style = {'display': 'inline-block', 'width': '80vh', 'height': '80vh'}),
                      justify = 'center'),

    html.Br(),
    dbc.Row(html.Br()),
    dbc.Row(html.H3("Scatter"), style = {'text-align': 'center'}, 
                                         justify = 'center'),
    dbc.Row(html.Br()),

    dbc.Row(dcc.Graph(id = 'scatter',
                      figure = scatter_fig,
                      style = {'display': 'inline-block', 
                               'width': '100vh', 
                               'height': '80vh'}),
                      justify = 'center'),
    
    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(dcc.Graph(id = 'bar', 
                      figure = bar_fig,
                      style = {'display': 'inline-block',
                               'width': '80vh', 
                               'height': '60vh'}),
                          justify = 'center'),

    html.Br(),
    dbc.Row("Sources: World Bank Open Data and\
             the Asian Development Bank Data Library")],

fluid=True)

# Update Figures
@app.callback(Output("scatter", "figure"),
              Input("country_dd", "value"))

def update_scatter(country):

    scatter_data_filter = df[df["Country / Economy"] == country]

    fig = px.scatter(scatter_data_filter, 
                     x = "commitment_date", 
                     y = "Amount",
                     hover_name = "Project Name",
                     hover_data = ["Country / Economy", "project_url"],
                     title = f"Commitment Amount Over Time in {country}",
                     labels = {"Amount": "Commitment Amount"},
                     trendline = "ols")
    return fig

@app.callback(Output("bar", "figure"),
              Input("country_dd", "value"))

def update_bar(country):

    bar_data_filter = df[df["Country / Economy"] == country]

    fig = px.bar(bar_data_filter, 
                 x = "Project Status", 
                 y = "Amount",
                 color = "Project Type / Modality of Assistance",
                 title = f"Commitment Amount per Project Type in {country}",
                 labels = {"Amount": "Commitment Amount"})
    
    return fig

#def update_options(search_value):
 #   if not search_value:
  #      raise PreventUpdate
   # return [o for o in country_options if search_value in o]

if __name__ == "__main__":
    app.run_server()